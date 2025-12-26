"""Entry point for tray app. Use .pyw to avoid console on Windows."""
from tray_icon import TrayApp

if __name__ == '__main__':
    app = TrayApp()
    app.run()
