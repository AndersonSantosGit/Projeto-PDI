'''
Created on 14 de nov de 2015

@author: Anderson Santos
@email: anderson.bcc.uag@gmail.com
Universidade Federal Rural de Pernambuco - UFRPE/UAG

'''

import numpy as np
import matplotlib.image as mpimg
import scipy.stats as SCI
import matplotlib.pyplot as plt
import cv2

from numpy import str
from skimage import filters
from numpy import size
from skimage.segmentation import slic,mark_boundaries
from scipy.stats.mstats_basic import kurtosis
from scipy.spatial import distance
from sklearn.naive_bayes import GaussianNB
from scipy.stats.stats import pearsonr
from skimage.morphology.misc import skimage2ndimage
from matplotlib.image import imsave

conceito = 10
n        = 2
img  = mpimg.imread(str(conceito) + '_' + str(n) +'.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold = filters.threshold_otsu(imgGray)

imLim = imgGray >= threshold

plt.imshow(imLim,cmap='binary')
plt.xticks([]), plt.yticks([])
plt.show()

imsave('..\\Imagens Segmentadas\\' + str(conceito) + '_' + str(n) + '_.jpg',imLim,cmap='binary')
