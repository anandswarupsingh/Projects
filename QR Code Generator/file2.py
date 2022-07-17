import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://www.linkedin.com/in/anandswarupsingh/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.svg" 
url.svg("myLinkedInProfile.svg", scale = 8) 
