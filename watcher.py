"""
Spotify-only watcher: monitors Spotify window title and mutes/unmutes Spotify
based on playback context.

Design principles:
- One title change = one decision = one log
- No API calls, OS-level only
- No noisy logs, no polling spam
"""

import threading
import time
import os
import json
from typing import Optional

import pygetwindow as gw
from utils import log, now_ts

WATCH_NAME = "Spotify"
POLL_INTERVAL = 1.5
CFG_FILE = "config.json"


def is_music_title(title: str) -> bool:
    if not title:
        return False

    t = title.strip().lower()

    if t in ("spotify", "spotify free", "Advertisement"):
        return False

    return " - " in title


class SpotifyWatcher(threading.Thread):
    def __init__(self, poll_interval: float = POLL_INTERVAL):
        super().__init__(daemon=True)
        self.poll_interval = poll_interval
        self._stop_event = threading.Event()
        self.last_title: Optional[str] = None
        self.running_since = now_ts()
        self.config = self._load_config()
        self._cfg_mtime = os.path.getmtime(CFG_FILE) if os.path.exists(CFG_FILE) else 0

    def _load_config(self):
        try:
            with open(CFG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _check_reload_config(self):
        if os.path.exists(CFG_FILE):
            mtime = os.path.getmtime(CFG_FILE)
            if mtime != self._cfg_mtime:
                self.config = self._load_config()
                self._cfg_mtime = mtime
                log("[CONFIG] Reloaded")

    def _find_spotify_title(self) -> Optional[str]:
        try:
            import win32process
            import psutil

            for w in gw.getAllWindows():
                if not w.title:
                    continue

                hwnd = w._hWnd
                _, pid = win32process.GetWindowThreadProcessId(hwnd)

                try:
                    proc = psutil.Process(pid)
                    if proc.name().lower() == "spotify.exe":
                        return w.title
                except psutil.NoSuchProcess:
                    continue

        except Exception as e:
            log(f"[ERROR] Window scan failed: {e}")

        return None

    def run(self):
        log("[SYSTEM] SpotifyWatcher started")

        from audio_control import set_spotify_mute

        while not self._stop_event.is_set():
            self._check_reload_config()
            title = self._find_spotify_title()

            if title and title != self.last_title:
                prev = self.last_title
                self.last_title = title

                action = "UNMUTE" if is_music_title(title) else "MUTE"
                set_spotify_mute(action == "MUTE")

                log(f"[EVENT] '{prev}' -> '{title}' | ACTION={action}")

                if self.config.get("webhook_enabled") and self.config.get("webhook_url"):
                    try:
                        import requests
                        requests.post(
                            self.config.get("webhook_url"),
                            json={"timestamp": now_ts(), "title": title, "action": action},
                            timeout=2,
                        )
                    except Exception as e:
                        log(f"[WEBHOOK ERROR] {e}")

            time.sleep(self.poll_interval)

        log("[SYSTEM] SpotifyWatcher stopped")

    def stop(self):
        self._stop_event.set()
