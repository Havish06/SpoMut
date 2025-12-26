SpoMut 🎧🔇
A silent Windows utility that automatically mutes and unmutes Spotify

SpoMut runs quietly in the background and controls Spotify’s audio based on what’s playing — music or ads — without using Spotify’s API.

No OAuth.
No cloud.
No tracking.
Just local, OS-level control.

🚀 Overview

SpoMut is a lightweight Windows background utility designed for one purpose:

Automatically mute Spotify when ads or idle states play, and unmute when real music starts.

It integrates directly with the operating system instead of Spotify’s servers, making it fast, private, and reliable.

✨ Core Features

🎵 Detects real music playback

🔇 Automatically mutes ads and idle states

🔊 Restores audio when songs resume

🖥️ Runs as a system tray application

🧾 Logs one clean event per song change

🔒 Fully local — no Spotify login required

🚫 What SpoMut Is Not

SpoMut intentionally avoids feature bloat.

❌ No Spotify Web API usage

❌ No OAuth or account access

❌ No playlist or recommendation control

❌ No data collection or analytics

❌ No mobile or web support

Spotify Desktop on Windows only.

🧠 How It Works

At a high level, SpoMut follows a simple and deterministic flow:

Periodically scans open Windows

Identifies the window belonging to spotify.exe

Reads the Spotify window title

Classifies the title:

Music → Song Name - Artist

Non-music → Spotify, Spotify Free, Advertisement

Applies mute or unmute locally

Logs a single atomic event

No noisy polling.
No redundant actions.

🧪 Example Log Output
[EVENT] 'Spotify Free' -> 'Boom Boom - Sai Abhyankkar' | ACTION=UNMUTE
[EVENT] 'Boom Boom - Sai Abhyankkar' -> 'Advertisement' | ACTION=MUTE


Readable. Calm. Intentional.

🖥️ System Requirements

Windows 10 / 11

Spotify Desktop application

Python 3.9 or higher

📦 Dependencies

Install required Python packages:

pip install pygetwindow psutil pywin32 pystray pillow requests

▶️ Running SpoMut

From the project directory:

python tray_icon.py


Once started:

SpoMut runs silently in the background

A tray icon appears in the system tray

Right-click the tray icon to:

Start / Stop the watcher

Manually mute / unmute Spotify

Open logs

Quit SpoMut

🧾 Logging

Logs are written to:
logs/spotify_title_log.txt

Only meaningful events are logged

Windows tray noise is filtered out

Designed for clarity, not verbosity

🔐 Privacy & Security

SpoMut is privacy-first by design.

No Spotify account access

No external API calls

No personal data storage

No network communication
(unless a webhook is explicitly enabled)

Everything runs locally.

⚠️ Known Limitations

Relies on Spotify exposing window titles
(Spotify may change this behavior in future updates)

Works only when Spotify Desktop is running

Ad detection is heuristic-based and may vary by region

🎯 Why SpoMut Exists

Spotify doesn’t let users decide when sound should play — only what should play.

SpoMut restores that control.

No algorithm.
No negotiation.
Just silence when you want it.