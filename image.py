from PIL import Image

img = Image.open('cut.jpg')

img = img.rotate(180)
w, h = img.size
img = img.resize((int(w/2), int(h/2)))

img.save('img2.jpg')