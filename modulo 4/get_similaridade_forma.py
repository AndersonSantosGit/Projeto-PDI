import cv2
from cv2 import mean
import numpy as np
from numpy import str
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from scipy.spatial import distance
from scipy.spatial.distance import euclidean
from skimage.color import rgb2gray
from skimage.measure import perimeter
from scipy.stats.stats import pearsonr
from skimage.segmentation import clear_border


def get_medoid(descritor):
    soma = 0
    indice = 0
    matriz_correlacao = np.corrcoef(descritor)
    for i in range(len(matriz_correlacao)):
        if (sum(matriz_correlacao[i]) > soma):
            soma = sum(matriz_correlacao[i])
            indice = i

    return indice, descritor[indice]

conceito_1 = 1
conceito_2 = 2

n_1 = 1
n_2 = 2

img_1 = cv2.imread('imagens_segmentadas/' + str(conceito_1) + '_' + str(n_1) + '_.jpg', 0)
img_2 = cv2.imread('imagens_segmentadas/' + str(conceito_2) + '_' + str(n_2) + '_.jpg', 0)
# img_1 = mpimg.imread('imagens_segmentadas/' + str(conceito_1) + '_' + str(n_1) + '_.jpg', 0)
# img_2 = mpimg.imread('imagens_segmentadas/' + str(conceito_2) + '_' + str(n_2) + '_.jpg', 0)

orb = cv2.ORB_create()
kp_1, descritores_1 = orb.detectAndCompute(img_1, None)
kp_2, descritores_2 = orb.detectAndCompute(img_2, None)
# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(descritores_1, descritores_2)
# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)
img_3 = cv2.drawMatches(img_1, kp_1, img_2, kp_2, matches, None, flags=2)
plt.imshow(img_3)
plt.show()

[idx_1, d_1] = get_medoid(descritores_1)
[idx_2, d_2] = get_medoid(descritores_2)

dist_1 = 0
dist_2 = 0
m_1 = kp_1[idx_1].pt
m_2 = kp_2[idx_2].pt
for l in range(len(kp_1)):
    dist_1 += euclidean(m_1, kp_1[l].pt)
for l in range(len(kp_2)):
    dist_2 += euclidean(m_2, kp_2[l].pt)

# EXTRACAO DE CARACTERISTICAS
f_1 = [0, 0, 0]
f_2 = [0, 0, 0]

img_1 = np.divide(img_1, 255.0)
img_2 = np.divide(img_2, 255.0)

prop1 = img_1.shape[0]*img_1.shape[1]
prop2 = img_2.shape[0]*img_2.shape[1]

# AREAS
f_1[0] = np.sum(img_1)/prop1
f_2[0] = np.sum(img_2)/prop2

# PERIMETROS
f_1[1] = perimeter(img_1)/prop1
f_2[1] = perimeter(img_2)/prop2

f_1[2] = dist_1/prop1
f_2[2] = dist_2/prop2

person = pearsonr(f_1, f_2)
dist = (distance.euclidean(f_1, f_2))*100

print np.abs((person[0]*100)-dist)

plt.subplot(121), plt.imshow(img_1, cmap='gray')
plt.title(''), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(img_2, cmap='gray')
plt.title(''), plt.xticks([]), plt.yticks([])

plt.show()
