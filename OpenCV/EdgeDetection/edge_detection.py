import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('11731931_807558992685584_4664935311061701518_o.jpg', 0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# another laplacian kernel
laplacian2_ker = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
laplacian2_ker = np.asanyarray(laplacian2_ker, np.float32)
laplacian2 = cv2.filter2D(img, -1, laplacian2_ker)

plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('default laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(laplacian2,cmap = 'gray')
plt.title('another laplacian'), plt.xticks([]), plt.yticks([])

plt.show()
