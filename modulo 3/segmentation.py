import numpy as np
from numpy import size
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.stats as SCI
from scipy.spatial import distance
from scipy.stats.stats import pearsonr
from scipy.stats.mstats_basic import kurtosis
from skimage.segmentation import slic, mark_boundaries
from sklearn.naive_bayes import GaussianNB

conceito = 7
n = 2

img = mpimg.imread('imagens/' + str(conceito) + '_' + str(n) + '.jpg')
plt.imshow(img)
plt.show()

# SLIC
segments_slic = slic(img, n_segments=200, compactness=10.0, sigma=3.0)
plt.imshow(mark_boundaries(img, segments_slic))
plt.show()

features = np.zeros([len(np.unique(segments_slic)), 4])
image_seg = np.array(img)
for j in range(len(np.unique(segments_slic))):

    color = np.array(img)
    indices = np.equal(segments_slic, j)

    color[:, :, 0] = np.multiply(color[:, :, 0], indices)
    color[:, :, 1] = np.multiply(color[:, :, 1], indices)
    color[:, :, 2] = np.multiply(color[:, :, 2], indices)

    region_r = color[color[:, :, 0] > 0, 0]
    region_g = color[color[:, :, 1] > 0, 1]
    region_b = color[color[:, :, 2] > 0, 2]

    # plt.imshow(color, cmap='gray')
    # plt.title('SLIC'), plt.xticks([]), plt.yticks([])
    # plt.show()

    f_mean = np.mean(region_r) + np.mean(region_g) + np.mean(region_b)
    f_variance = np.var(region_r) + np.var(region_g) + np.var(region_b)
    f_skewness = SCI.skew(region_r) + SCI.skew(region_g) + SCI.skew(region_b)
    f_kurtosis = kurtosis(region_r) + kurtosis(region_g) + kurtosis(region_b)
    f_entropy = SCI.entropy(region_r) + SCI.entropy(region_g) + SCI.entropy(region_b)
    img_features = [f_mean, f_variance, f_skewness, f_kurtosis]
    features = np.load('space_feature/features_' + str(conceito) + '.npy')
    dist_euclidian = 0
    target = np.ones([np.size(features, 0), 1])
    pearson = []
    for m in range(size(features, 0)):
        # amostra = features[m, :]
        amostra = features[m, 0:4]
        # dist_euclidian += distance.euclidean(img_features, amostra)
        person = pearsonr(img_features, amostra)
        # print person
        if (person[1] < 0.05):
            pearson.append(person[0])
        # else:
        #    pearson.append(0)
    # print np.mean(pearson)
    # print dist_euclidian

    # gnb = GaussianNB()
    # y_pred = gnb.fit(features, target).predict(img_features)

    # if dist_euclidian >= 51000 or dist_euclidian <= 40000:
    # if y_pred == 1:
    # if dist_euclidian <= 36000:
    # print np.mean(np.abs(pearson))
    if np.mean(np.abs(pearson)) > 0.99:
        image_seg[indices, 0] = 255
        image_seg[indices, 1] = 255
        image_seg[indices, 2] = 255
    else:
        image_seg[indices, 0] = 0
        image_seg[indices, 1] = 0
        image_seg[indices, 2] = 0


a = np.array(img)
a[:, :, 0] = np.multiply(img[:, :, 0], np.double(image_seg[:, :, 0])/255.0)
a[:, :, 1] = np.multiply(img[:, :, 1], np.double(image_seg[:, :, 1])/255.0)
a[:, :, 2] = np.multiply(img[:, :, 2], np.double(image_seg[:, :, 2])/255.0)

plt.subplot(131), plt.imshow(mark_boundaries(img, segments_slic))
plt.title(''), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(image_seg, cmap='binary')
plt.title(''), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(a, cmap='gray')
plt.title(''), plt.xticks([]), plt.yticks([])

plt.show()

"""
EUCLIDIAN DISTANCE
for i in range(10):
    features = np.load('SpaceFeature/FEATURES_' + str(i) + '.npy')
    dist_euclidian = 0
    for j in range(size(features, 1)):
        amostra = features[j, :]
        dst = distance.euclidean(img_features, amostra)
"""
