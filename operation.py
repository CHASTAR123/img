import cv2
import numpy as np

image1 = cv2.imread('images/dorae.png')
image2 = cv2.imread('images/flower.png')

print(image1.shape,image2.shape)

image2 = cv2.resize(image2,(172, 129))
cv2.imwrite('flower.png', image2)
image2 = cv2.imread('flower.png')
weighted = cv2.addWeighted(image1, 0.2, image2, 0.8, 0 )
cv2.imshow('Addition', weighted)
cv2.imwrite('doraflr.png', weighted)
cv2.waitKey()

sub = cv2.subtract(image1, image2)
cv2.imshow('Subtraction', sub)
cv2.imwrite('doraflrsub.png', sub)
cv2.waitKey()

image3 = cv2.imread('spideyman.jpg')
#erosion
kernel = np.ones((9,9), np.uint8)
print(kernel)

erosion = cv2.erode(image3, kernel)
cv2.imshow('Erosion', erosion)
cv2.imwrite('dog.png', erosion)
cv2.waitKey()

