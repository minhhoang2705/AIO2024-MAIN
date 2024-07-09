import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


# Read the image
img = mpimg.imread('./dog.jpeg')

# convert to grayscale using luminosity method
gray_img = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
print(gray_img[0, 0]) # 126.26666666666667 -> Answer C

# Display the original and grayscale images
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img)
ax[0].set_title("Original Image")
ax[1].imshow(gray_img, cmap='gray')
ax[1].set_title("Grayscale Image (Average)")
for a in ax:
    a.axis('off')
plt.show()