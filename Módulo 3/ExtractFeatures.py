#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 14 de nov de 2015

@author: Anderson Santos
@email: anderson.bcc.uag@gmail.com
Universidade: Federal Rural de Pernambuco - UFRPE/UAG

'''
import numpy as np
import matplotlib.image as mpimg 
import scipy.stats as SCI
import cv2

from skimage.util import img_as_ubyte
from numpy import str
from os import listdir
from os.path import isfile, join
from matplotlib import pyplot as plt
from matplotlib.axes._subplots import Subplot
from skimage import filters
from skimage import data
from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage.util import img_as_ubyte
from skimage.color import rgb2gray
from sympy.strategies.core import switch
from matplotlib.mlab import entropy


path = "C:\\Users\\Anderson Santos\\Google Drive\\8º Período\\PDI\\Base\\Conceito "
fig = plt.figure(figsize=(5,2))
for conceito in [2]: # [1:10]
    mypath =  path + str(conceito) + '\\Background Facil\\'
    #for n in range(10): 
    #print path + str(conceito) + '\Background Facil\\' + str(n)   
    #onlyfiles = [ f for f in listdir(unicode(mypath,'utf-8')) if isfile(join(unicode(mypath,'utf-8'),f)) ]
    #print onlyfiles
    print '\t \n Conceito: ' + str(conceito) + '\n'
    
    print unicode(mypath,'utf-8')
    print listdir(unicode(mypath,'utf-8'))
    i = 1;
    FEATURES = np.zeros([len(listdir(unicode(mypath,'utf-8')))-1,5])
    radius = 220
    selem = disk(radius)
                
    for f in listdir(unicode(mypath,'utf-8')):
        
        if isfile(join(unicode(mypath,'utf-8'),f)):
            if f != "desktop.ini":
                #print unicode(mypath,'utf-8')+f;
                img  = mpimg.imread(unicode(mypath,'utf-8')+f)
                #imgGray  = rgb2gray(img)
                imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                #plt.imshow(imgGray,cmap='gray')
                #plt.show()
                threshold = filters.threshold_otsu(imgGray) 
                #threshold = filters.threshold_isodata(imgGray)
                #threshold = filters.threshold_yen(imgGray)
                if conceito in [7]:
                    if i in [4,5,7,10]:
                        imLim = imgGray < threshold
                    else:
                        imLim = imgGray >= threshold
                elif conceito in [8]:
                    if i in [2,4,6,10]:
                        imLim = imgGray < threshold
                    else:
                        imLim = imgGray >= threshold
                else:
                    imLim = imgGray >= threshold

                #imLim = rank.otsu(cv2.convertScaleAbs(imgGray), selem)
                
                ax1 = fig.add_subplot(5, 2, i)                
                plt.subplot(ax1); plt.imshow(imLim,cmap='binary')
                plt.title(f), plt.xticks([]), plt.yticks([])
                
                color = np.array(img)
                
                color[:,:,0] = np.multiply(color[:,:,0],imLim)
                color[:,:,1] = np.multiply(color[:,:,1],imLim)
                color[:,:,2] = np.multiply(color[:,:,2],imLim)
                
                regionR = color[color[:,:,0]>0,0]
                regionG = color[color[:,:,1]>0,1]
                regionB = color[color[:,:,2]>0,2]
                
                MEAN     = np.mean(regionR)      + np.mean(regionG)      + np.mean(regionB)
                VARIANCE = np.var(regionR)       + np.var(regionG)       + np.var(regionB)
                SKEWNESS = SCI.skew(regionR)     + SCI.skew(regionG)     + SCI.skew(regionB)
                KURTOSIS = SCI.kurtosis(regionR) + SCI.kurtosis(regionG) + SCI.kurtosis(regionB)
                ENTROPY  = SCI.entropy(regionR)  + SCI.entropy(regionG)  + SCI.entropy(regionB)
                
                FEATURES[i-1,0] = MEAN
                FEATURES[i-1,1] = VARIANCE
                FEATURES[i-1,2] = SKEWNESS
                FEATURES[i-1,3] = KURTOSIS
                FEATURES[i-1,4] = ENTROPY
                
                
                print FEATURES[i-1,:]
                i = i + 1
                
    plt.show()
    np.save(('SpaceFeature\FEATURES_'+ str(conceito)),FEATURES)
    print 'FIM'
    