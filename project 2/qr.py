import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4)

qr.add_data("https://www.netguru.com/blog/django-apps-examples#:~:text=Social%20media%20platforms%20or%20streaming,with%20the%20Python%20programming%20language.")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("yo.png")