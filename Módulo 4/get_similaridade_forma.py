'''
Created on 22 de nov de 2015

@author: Anderson Santos
@email: anderson.bcc.uag@gmail.com
Universidade Federal Rural de Pernambuco - UFRPE/UAG

'''

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

from scipy.spatial import distance
from skimage.measure import perimeter
from skimage.color import rgb2gray
from skimage.segmentation import clear_border
from cv2 import mean
from scipy.stats.stats import pearsonr
from numpy import str
from scipy.spatial.distance import euclidean


def getMedoid(descritor):
    matrizCorrelacao = np.corrcoef(descritor)
    
    soma = 0;
    indice = 0;
    
    for i in range(len(matrizCorrelacao)):
        if (sum(matrizCorrelacao[i]) > soma):
            soma = sum(matrizCorrelacao[i])
            indice = i

    return indice, descritor[indice]


conceito_1 = 2
conceito_2 = 2

n_1        = 1
n_2        = 2

img1 = cv2.imread('Imagens Segmentadas\\'+ str(conceito_1) + '_' + str(n_1) +'_.jpg',0)
img2 = cv2.imread('Imagens Segmentadas\\'+ str(conceito_2) + '_' + str(n_2) +'_.jpg',0)

#img1 = mpimg.imread('Imagens Segmentadas\\'+ str(conceito_1) + '_' + str(n_1) +'_.jpg',0) 
#img2 = mpimg.imread('Imagens Segmentadas\\'+ str(conceito_2) + '_' + str(n_2) +'_.jpg',0)


sift = cv2.SIFT()
#kp = sift.detect(gray,None)
kp1, descritores1 = sift.detectAndCompute(img1,None)
kp2, descritores2 = sift.detectAndCompute(img2,None)

imgKp1=cv2.drawKeypoints(img1,kp1)
plt.subplot(121),plt.imshow(imgKp1, cmap = 'gray')
plt.title('Pontos SIFT IM1'), plt.xticks([]), plt.yticks([])

imgKp2=cv2.drawKeypoints(img2,kp2)
plt.subplot(122),plt.imshow(imgKp2, cmap = 'gray')
plt.title('Pontos SIFT IM2'), plt.xticks([]), plt.yticks([])
plt.show()

[IDX_1,D1] = getMedoid(descritores1)
[IDX_2,D2] = getMedoid(descritores2)

dist_1 = 0
dist_2 = 0
M_1 = kp1[IDX_1].pt
M_2 = kp2[IDX_2].pt
for l in range(len(kp1)):
    dist_1 += euclidean(M_1,kp1[l].pt) 
for l in range(len(kp2)):
    dist_2 += euclidean(M_2,kp2[l].pt) 
    
    
'''
flann_params = dict(algorithm=1, trees=4)
flann = cv2.flann_Index(descritores1, flann_params)
idx, dist = flann.knnSearch(descritores2, 1, params={})
del flann

print np.sum(dist)
if (np.sum(dist)==0):
    print 100
else:
    print (np.sum(dist)/np.max(dist))/100.0

plt.show()
'''

'''
ret1,thresh1 = cv2.threshold(img1,0,255,0)
ret2,thresh2 = cv2.threshold(img2,0,255,0)

contours1,hierarchy1 = cv2.findContours(thresh1, 1, 2)
contours2,hierarchy2 = cv2.findContours(thresh2, 1, 2)

cnt1 = contours1[1]
cnt2 = contours2[0]

M1 = cv2.moments(cnt1)
M2 = cv2.moments(cnt2)

print M1
print M2

cx1 = int(M1['m10']/M1['m00'])
cy1 = int(M1['m01']/M1['m00'])


cx2 = int(M2['m10']/M2['m00'])
cy2 = int(M2['m01']/M2['m00'])

area1      = cv2.contourArea(cnt1)
area2      = cv2.contourArea(cnt2)

perimetro1 = cv2.arcLength(cnt1,True)
perimetro2 = cv2.arcLength(cnt2,True)

epsilon1 = 0.1*cv2.arcLength(cnt1,True)
epsilon2 = 0.1*cv2.arcLength(cnt2,True)

approx1 = cv2.approxPolyDP(cnt1,epsilon1,True)
approx2 = cv2.approxPolyDP(cnt2,epsilon2,True)

hull1 = cv2.convexHull(cnt1)
hull2 = cv2.convexHull(cnt2)

k1 = cv2.isContourConvex(cnt1)
k2 = cv2.isContourConvex(cnt2)
'''

'''
                        # EXTRACAO DE CARACTERISTICAS

'''

F_1 = [0,0,0]
F_2 = [0,0,0]
 
img1 = np.divide(img1,255.0)
img2 = np.divide(img2,255.0)

prop1 = img1.shape[0]*img1.shape[1]
prop2 = img2.shape[0]*img2.shape[1]

#AREAS
F_1[0] = np.sum(img1)/prop1
F_2[0] = np.sum(img2)/prop2

#PERIMETROS
F_1[1] = perimeter(img1)/prop1
F_2[1] = perimeter(img2)/prop2

F_1[2] = dist_1/prop1
F_2[2] = dist_2/prop2

print F_1
print F_2

P = pearsonr(F_1,F_2)
#print P
#print (F_1[0]/F_1[1])
#print (F_2[0]/F_2[1])
d = (distance.euclidean(F_1,F_2))*100
#print d

print np.abs((P[0]*100)-d)

#P = pearsonr(d1,d2)
#print P

plt.subplot(121),plt.imshow(img1,cmap='gray')
plt.title('Image 1'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img2,cmap='gray')
plt.title('Image 2'), plt.xticks([]), plt.yticks([])

plt.show()
