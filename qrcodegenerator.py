import qrcode
import image

qr = qrcode.QRCode(
    version= "05",
    box_size= "10",
    border= "4"
)

data = "https://snowwisdom.com"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="white")
img.save("code.png")