import time
import os

LOG_FILE = os.path.join("logs", "spotify_title_log.txt")

print("📜 SpoMut Live Logs\n")

last_size = 0
while True:
    if os.path.exists(LOG_FILE):
        size = os.path.getsize(LOG_FILE)
        if size > last_size:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                f.seek(last_size)
                print(f.read(), end="")
            last_size = size
    time.sleep(0.5)
