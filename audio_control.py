"""pycaw-based audio control for Spotify Desktop (spotify.exe)."""
import traceback
from typing import Optional
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from utils import log

def list_audio_sessions():
    sessions = AudioUtilities.GetAllSessions()
    infos = []
    for i, s in enumerate(sessions):
        proc_name = '<no process>'
        pid = None
        try:
            if s.Process:
                proc_name = s.Process.name()
                pid = s.Process.pid
        except Exception:
            proc_name = '<error>'
        infos.append((i, proc_name, pid))
    return infos

def get_spotify_session(verbose: bool = False):
    sessions = AudioUtilities.GetAllSessions()
    for i, session in enumerate(sessions):
        try:
            if session.Process:
                pname = session.Process.name()
                if verbose:
                    log(f'session[{i}] -> {pname}')
                if pname and pname.lower() == 'spotify.exe':
                    return session
        except Exception:
            continue
    return None

def set_spotify_mute(state: bool, verbose: bool = False) -> bool:
    try:
        session = get_spotify_session(verbose=verbose)
        if not session:
            if verbose:
                log('Spotify session not found.')
            return False
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        mute_flag = 1 if state else 0
        volume.SetMute(mute_flag, None)
        if verbose:
            log('Spotify muted.' if state else 'Spotify unmuted.')
        return True
    except Exception:
        traceback.print_exc()
        return False
