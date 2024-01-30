#colored image, RGB split channel images

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("image.jpg")
img=img.resize((1024,1024))
M = np.asarray(img)

plt.figure(figsize=(12, 12))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('on')

plt.subplot(2, 2, 2)
plt.imshow(M[:, :, 0], cmap='Reds', vmin=0, vmax=255)
plt.title("Red Channel")
plt.axis('on')

plt.subplot(2, 2, 3)
plt.imshow(M[:, :, 1], cmap='Greens', vmin=0, vmax=255)
plt.title("Green Channel")
plt.axis('on')

plt.subplot(2, 2, 4)
plt.imshow(M[:, :, 2], cmap='Blues', vmin=0, vmax=255)
plt.title("Blue Channel")
plt.axis('on')



w, h = img.size
print(w,h)

plt.show()