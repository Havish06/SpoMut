import pystray
from PIL import Image

img = Image.new("RGBA", (64, 64), (30, 215, 96, 255))
icon = pystray.Icon("test", img, "Test Tray")
icon.run()
