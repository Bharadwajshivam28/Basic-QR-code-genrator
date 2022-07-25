import qrcode

img = qrcode.make("https://www.youtube.com/") #paste your link in the box for which you want to make qr
img.save("youtube.png") #Give your specific name of qr code by which you want to save it