#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join

import cv2
import numpy as np
from numpy import str
from matplotlib import pyplot as plt
from matplotlib.mlab import entropy
import matplotlib.image as mpimg
from skimage.util import img_as_ubyte
from skimage import data
from skimage.morphology import disk
from skimage.util import img_as_ubyte
from skimage.color import rgb2gray
import scipy.stats as sci


path = "path_concepts_here"
fig = plt.figure(figsize=(5, 2))
for conceito in [2]:  # [1:10]
    my_path = path + str(conceito) + '/Background Facil/'
    # for n in range(10):
    #    print path + str(conceito) + '\Background Facil\\' + str(n)
    #    onlyfiles = [f for f in listdir(unicode(my_path, 'utf-8')) if isfile(join(unicode(my_path, 'utf-8'), f))]
    #    print onlyfiles
    print '\t \n Conceito: ' + str(conceito) + '\n'
    print unicode(my_path, 'utf-8')
    print listdir(unicode(my_path, 'utf-8'))
    i = 1
    features = np.zeros([len(listdir(unicode(my_path, 'utf-8')))-1, 5])
    radius = 220
    selem = disk(radius)
    for f in listdir(unicode(my_path, 'utf-8')):
        if isfile(join(unicode(my_path, 'utf-8'), f)):
            if f != "desktop.ini":
                # print unicode(my_path, 'utf-8')+f
                img = mpimg.imread(unicode(my_path, 'utf-8')+f)
                # img_gray = rgb2gray(img)
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # plt.imshow(img_gray, cmap='gray')
                # plt.show()
                threshold = filters.threshold_otsu(img_gray)
                # threshold = filters.threshold_isodata(img_gray)
                # threshold = filters.threshold_yen(img_gray)
                if conceito in [7]:
                    if i in [4, 5, 7, 10]:
                        im_lim = img_gray < threshold
                    else:
                        im_lim = img_gray >= threshold
                elif conceito in [8]:
                    if i in [2, 4, 6, 10]:
                        im_lim = img_gray < threshold
                    else:
                        im_lim = img_gray >= threshold
                else:
                    im_lim = img_gray >= threshold

                # im_lim = rank.otsu(cv2.convertScaleAbs(img_gray), selem)
                ax1 = fig.add_subplot(5, 2, i)
                plt.subplot(ax1), plt.imshow(im_lim, cmap='binary')
                plt.title(f), plt.xticks([]), plt.yticks([])

                color = np.array(img)
                color[:, :, 0] = np.multiply(color[:, :, 0], im_lim)
                color[:, :, 1] = np.multiply(color[:, :, 1], im_lim)
                color[:, :, 2] = np.multiply(color[:, :, 2], im_lim)

                region_r = color[color[:, :, 0] > 0, 0]
                region_g = color[color[:, :, 1] > 0, 1]
                region_b = color[color[:, :, 2] > 0, 2]

                mean = np.mean(region_r) + np.mean(region_g) + np.mean(region_b)
                variance = np.var(region_r) + np.var(region_g) + np.var(region_b)
                skewness = sci.skew(region_r) + sci.skew(region_g) + sci.skew(region_b)
                kurtosis = sci.kurtosis(region_r) + sci.kurtosis(region_g) + sci.kurtosis(region_b)
                entropy = sci.entropy(region_r) + sci.entropy(region_g) + sci.entropy(region_b)

                features[i-1, 0] = mean
                features[i-1, 1] = variance
                features[i-1, 2] = skewness
                features[i-1, 3] = kurtosis
                features[i-1, 4] = entropy

                print features[i-1, :]
                i = i + 1

    plt.show()
    np.save(('space_feature\features_' + str(conceito)), features)
