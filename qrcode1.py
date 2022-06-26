import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=50, border=6)
qr.add_data("https://github.com/Pradeep-81/")
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="pink")
img.save("MyGithubprofile.jpg")
