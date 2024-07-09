import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


# Read the image
img = mpimg.imread('./dog.jpeg')

# Convert to grayscale using the Average method
gray_img_01 = np.mean(img[:, :, :3], axis=2)
print(gray_img_01[0, 0]) # 107.66666666666667 -> Answer A

# Display the original and grayscale images
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img)
ax[0].set_title("Original Image")
ax[1].imshow(gray_img_01, cmap='gray')
ax[1].set_title("Grayscale Image (Average)")
for a in ax:
    a.axis('off')
plt.show()