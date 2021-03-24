

# *** Encode


import qrcode
data='hello iam najah said ahmed '

# img=qrcode.make(data)
# img.save('img.png')



qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color='red',back_color='white')

img.save('img2.png')




#*** Decode 

from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open('img2.png')
result=decode(img)
print(result)