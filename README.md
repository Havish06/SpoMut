# SpoMut

SpoMut is a Python utility for automatically muting and unmuting Spotify Desktop on Windows.

## What SpoMut Does

SpoMut runs in the background and controls Spotify audio based on playback state.

Rules:
* music playing → unmute *
** advertisement or idle state → mute **
*** no Spotify API, OAuth, or cloud services ***

---

## Installation

Install dependencies using pip:

```bash
pip install pygetwindow psutil pywin32 pystray pillow requests
```

## Clone the repository:

```git clone https://github.com/Havish06/SpoMut.git
cd SpoMut
```

## Usage
Run SpoMut from the project directory:

```
python tray_icon.py
```
SpoMut will start in the system tray and monitor Spotify automatically.

Example Log Output

[EVENT] 'Spotify Free' -> 'Song Name - Artist' | ACTION=UNMUTE <br>
[EVENT] 'Song Name - Artist' -> 'Advertisement' | ACTION=MUTE


**How It Works**
1. Detects the Spotify window owned by spotify.exe
2. Reads the window title
3. Classifies playback state as music or non-music
4. Applies mute or unmute locally
5. Logs a single event per change

**Requirements**
- Windows 10 or Windows 11
- Spotify Desktop application
- Python 3.9 or higher

**Privacy**
SpoMut does not:

access Spotify accounts
** collect user data
*** send data over the network ***

All processing is done locally.
