# Copypaste from docs
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from PIL import Image


#resize the image to 28x28 pixels
basewidth = 28
img = Image.open('data/fashion/1test.jpeg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,28), Image.ANTIALIAS)
img.save('data/fashion/1test.jpeg')

img=mpimg.imread('data/fashion/1test.jpeg', 'r')
#imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.figure()
plt.imshow(img)
#plt.imshow(imgGrey)
plt.colorbar()
plt.grid(False)
plt.show()