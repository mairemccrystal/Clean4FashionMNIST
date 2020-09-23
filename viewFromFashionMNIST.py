import gzip
from random import random


#code from : https://stackoverflow.com/questions/40427435/extract-images-from-idx3-ubyte-file-or-gzip-via-python
import gzip
f = gzip.open('data/fashion/train-images-idx3-ubyte.gz','r')

image_size = 28
num_images = 300

import numpy as np
f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size, image_size, 1)

import matplotlib.pyplot as plt



for i in range(160,165):
    import matplotlib.pyplot as plt
    image = np.asarray(data[i]).squeeze()
    plt.imshow(image)
    plt.show()
    plt.close()


