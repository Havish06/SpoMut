# tray_icon.py
import os
import webbrowser
import threading
from typing import Optional

import pystray
from PIL import Image, ImageDraw

from watcher import SpotifyWatcher
from audio_control import set_spotify_mute
from utils import log, toast

print("tray_icon loaded")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, 'resources', 'icon.png')
SETTINGS_SCRIPT = os.path.join(BASE_DIR, 'settings_tk.py')
LOG_DIR = os.path.join(BASE_DIR, 'logs')


class TrayApp:
    def __init__(self):
        # self.icon: Optional[pystray.Icon] = None
        self.watcher = SpotifyWatcher()

    # ---------------- ICON ----------------
    def _make_icon(self):
        try:
            if os.path.exists(ICON_PATH):
                return Image.open(ICON_PATH).convert("RGBA")
        except:
            pass

        # fallback green circle
        img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.ellipse((8, 8, 56, 56), fill=(30, 215, 96, 255))
        return img

    # ---------------- MENU ACTIONS ----------------
    def _start(self, icon, item):
        if not self.watcher.is_alive():
            self.watcher = SpotifyWatcher()
            self.watcher.start()
            log("Watcher started")
        else:
            log("Watcher already running")

    def _stop(self, icon, item):
        if self.watcher.is_alive():
            self.watcher.stop()
            log("Watcher stopped")
        else:
            log("Watcher not running")

    def _mute(self, icon, item):
        set_spotify_mute(True, verbose=True)

    def _unmute(self, icon, item):
        set_spotify_mute(False, verbose=True)

    def _settings(self, icon, item):
        try:
            import subprocess
            subprocess.Popen(["python", SETTINGS_SCRIPT])
        except Exception as e:
            log(f"Settings failed: {e}")

    def _logs(self, icon, item):
        os.makedirs(LOG_DIR, exist_ok=True)
        f = os.path.join(LOG_DIR, "spotify_title_log.txt")
        if not os.path.exists(f):
            open(f, "a").close()
        os.startfile(f)

    def _quit(self, icon, item):
        log("Exiting tray...")
        if self.watcher.is_alive():
            self.watcher.stop()
        icon.stop()

    # ---------------- BUILD MENU ----------------
    def _menu(self):
        return pystray.Menu(
            pystray.MenuItem("Start Watching", self._start),
            pystray.MenuItem("Stop Watching", self._stop),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Mute Spotify", self._mute),
            pystray.MenuItem("Unmute Spotify", self._unmute),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Settings", self._settings),
            pystray.MenuItem("Show Logs", self._logs),
            pystray.MenuItem("Quit", self._quit),
        )

    # ---------------- RUN ----------------
    def run(self):
        print("attempting to start tray icon")

        self.watcher.start()

        # WORKING TRAY START — identical logic to test_tray.py
        self.icon = pystray.Icon(
            "spotify-tray",
            self._make_icon(),
            "Spotify Tray",
            menu=self._menu()
        )

        self.icon.run()

        print("icon.run() returned")

if __name__ == "__main__":
    app = TrayApp()
    app.run()
