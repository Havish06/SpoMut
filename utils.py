# utils.py
import os
from datetime import datetime

import sys
import os

import sys

import sys

class SilentStderr:
    def write(self, msg):
        if not msg:
            return
        if "WNDPROC return value cannot be converted" in msg:
            return
        if "WPARAM is simple" in msg:
            return
        if msg.strip() == "":
            return
        sys.__stderr__.write(msg)

    def flush(self):
        sys.__stderr__.flush()

sys.stderr = SilentStderr()


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "spotify_title_log.txt")

try:
    from win10toast import ToastNotifier
    TOASTER = ToastNotifier()
except Exception:
    TOASTER = None


def now_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(msg, level="INFO"):
    os.makedirs(LOG_DIR, exist_ok=True)
    line = f"[{now_ts()}] [{level}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def toast(msg: str):
    if TOASTER:
        try:
            TOASTER.show_toast("Spotify Tray", msg, duration=3, threaded=True)
        except Exception:
            pass
