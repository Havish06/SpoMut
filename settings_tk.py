# settings_tk.py
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

CFG_FILE = "config.json"
DEFAULT = {
    "start_on_boot": False,
    "notifications": True,
    "webhook_enabled": False,
    "webhook_url": "http://127.0.0.1:8000/event",
}


def load_cfg():
    if os.path.exists(CFG_FILE):
        try:
            with open(CFG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return DEFAULT.copy()
    return DEFAULT.copy()


def save_cfg(cfg):
    with open(CFG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


class SettingsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spotify Tray - Settings")
        self.geometry("480x240")
        self.resizable(False, False)
        self.cfg = load_cfg()
        self._build_ui()

    def _build_ui(self):
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        self.var_start = tk.BooleanVar(value=self.cfg.get("start_on_boot", False))
        self.var_notify = tk.BooleanVar(value=self.cfg.get("notifications", True))
        self.var_webhook = tk.BooleanVar(value=self.cfg.get("webhook_enabled", False))
        self.var_url = tk.StringVar(value=self.cfg.get("webhook_url", ""))

        ttk.Checkbutton(frm, text="Start on boot", variable=self.var_start).grid(column=0, row=0, sticky="w", pady=6)
        ttk.Checkbutton(frm, text="Notifications", variable=self.var_notify).grid(column=0, row=1, sticky="w", pady=6)
        ttk.Checkbutton(frm, text="Webhook enabled", variable=self.var_webhook).grid(column=0, row=2, sticky="w", pady=6)

        ttk.Label(frm, text="Webhook URL:").grid(column=0, row=3, sticky="w", pady=(12, 2))
        ttk.Entry(frm, textvariable=self.var_url, width=60).grid(column=0, row=4, sticky="w")

        btn_frame = ttk.Frame(frm)
        btn_frame.grid(column=0, row=5, pady=14, sticky="w")

        ttk.Button(btn_frame, text="Save", command=self._on_save).grid(column=0, row=0, padx=6)
        ttk.Button(btn_frame, text="Close", command=self.destroy).grid(column=1, row=0, padx=6)

    def _on_save(self):
        self.cfg["start_on_boot"] = self.var_start.get()
        self.cfg["notifications"] = self.var_notify.get()
        self.cfg["webhook_enabled"] = self.var_webhook.get()
        self.cfg["webhook_url"] = self.var_url.get().strip()
        save_cfg(self.cfg)
        messagebox.showinfo("Saved", "Settings saved to config.json")


if __name__ == "__main__":
    app = SettingsApp()
    app.mainloop()
