import numpy as np
from skimage.io import imread, imshow
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Circle, Rectangle
from skimage import transform
from skimage.color import rgb2gray
from skimage.feature import match_template
from skimage.feature import peak_local_max
import skimage
import cv2 as cv


leuven = cv.imread('cap.jpg')
leuven_gray = cv.cvtColor(leuven, cv.COLOR_BGR2GRAY)
leuven_gray = cv.adaptiveThreshold(leuven_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
search = leuven_gray[50:, 1:]
search = cv.adaptiveThreshold(search, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 5)
ftemplate = leuven_gray[5:33, 191:216]
template = cv.resize(ftemplate, None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
cv.imshow('img', template)
cv.waitKey(0)
w, h = template.shape[::-1]
resulting_image = cv.matchTemplate(search, ftemplate, cv.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where( resulting_image >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(search, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)
#imshow(resulting_image, cmap='magma')
cv.imshow('img', search)
cv.waitKey(0)



