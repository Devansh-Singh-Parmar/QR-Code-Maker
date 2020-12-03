import pyqrcode
import png
from pyqrcode import QRCode
QRstr = "https://iblogarticlesplace.netlify.app/"
url = pyqrcode.create(QRstr)
url.png('C:\\Users\\user\\Desktop\\Main Folder\\Private\\QR Codes\\Iblog.jpg', scale= 8)