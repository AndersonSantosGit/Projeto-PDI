import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cow.jpg', 0)
orb = cv2.ORB_create()
kp, descriptors = orb.detectAndCompute(img, None)
img_keypoints = cv2.drawKeypoints(img, kp, None, flags=2)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Imagem original'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img_keypoints, cmap='gray')
plt.title('Imagem com descritores'), plt.xticks([]), plt.yticks([])

plt.show()
