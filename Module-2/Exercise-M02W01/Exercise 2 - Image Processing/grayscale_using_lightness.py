# # Download image
# !gdown 1i9dqan21DjQqG5Q_VEvmOLrVwAIXD0vB
# Question 12: Convert image to grayscale using the Lightness method

import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = mpimg.imread('./dog.jpeg')

# Convert to grayscale using the Lightness method
gray_img_01 = np.mean([np.max(img[:, :, :3], axis=2), np.min(img[:, :, :3], axis=2)], axis=0)
print(gray_img_01[0, 0]) # 102.5 -> Answer A
# Display the original and grayscale images
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img)
ax[0].set_title("Original Image")
ax[1].imshow(gray_img_01, cmap='gray')
ax[1].set_title("Grayscale Image (Lightness)")
for a in ax:
    a.axis('off')
plt.show()
