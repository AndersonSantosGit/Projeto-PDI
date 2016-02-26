'''
Created on 21 de out de 2015

@author: Anderson Santos
'''

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('horse.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
#kp = sift.detect(gray,None)
kp, descritores =sift.detectAndCompute(gray,None)

imgKp=cv2.drawKeypoints(gray,kp)
plt.imshow(imgKp, cmap = 'gray')
plt.title('Pontos SIFT'), plt.xticks([]), plt.yticks([])
plt.show()
img=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.imshow(img, cmap = 'gray')

plt.show()

