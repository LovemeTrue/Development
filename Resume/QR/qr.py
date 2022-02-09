from PIL import Image, ImageDraw
import qrcode

data = "https://www.youtube.com/watch?v=DDxCQ7oJJZ8"

filename = "qrcode.png"

img = qrcode.make(data)

img.save(filename)