#Did you know that images can be represented as matrices and tensors? In this case, two grayscale images are used. The idea in this code is to merge both images into one using NumPy.
#Matrices are used instead of tensors since both images are two-dimensional, with rows and columns of the matrix representing their pixels in a single channel. If we were working with color images, we would need to use tensors to represent the RGB channels in the third dimension.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


#Print the complete matrix
np.set_printoptions(threshold=np.inf)

print("Image 1:")
img1 = Image.open('img1.png').convert("L")

img1 = img1.resize((56, 28))

#The image is converted to a Numpy array, in this case a matrix.
img1 = np.array(img1)

print(img1)
print(img1.shape)

#The NumPy matrix is plotted using Matplotlib, and the original image is observed.
plt.figure()
plt.imshow(img1, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()

print("Imagen 2:")

img2 = Image.open('img2.png').convert("L")

img2 = img2.resize((56, 28))

#The image is converted to a Numpy array, in this case a matrix.
img2 = np.array(img2)

print(img2)
print(img2.shape)

#The NumPy matrix is plotted using Matplotlib, and the original image is observed.
plt.figure()
plt.imshow(img2, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()

#suma = img1 + img2

#The image is normalized to have values between 0 and 1 instead of 0 and 255 to correct the color. Otherwise, the blacks will be whites and vice versa.
img1 = img1/255
img2 = img2/255

#The images converted to matrices are summed.
suma = np.add(img1, img2)

#Other method
#suma = img1 + img2

#The matrices representing the images have already been summed and plotted using Matplotlib, resulting in a new image that merges image 1 and image 2.
plt.figure()
plt.imshow(suma, cmap=plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()
