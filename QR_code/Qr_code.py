# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode



# String which represents the QR code
# s = "https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME"

s = input()
name = input()
# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg((name+".svg"), scale = 8)

# Create and save the png file naming "myqr.png"
url.png((name+".png"), scale = 6)
