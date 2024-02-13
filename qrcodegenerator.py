import qrcode

qr = qrcode.QRCode(
    version= "05",
    box_size= "10",
    border= "4"
)

data = "https://egwimcodes.dev" # YOu can change the link here to what ever you want

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="white") # set the look here
img.save("code.png") # saving the image to this file name