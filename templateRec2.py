import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import numpy as np
from PIL import Image

img_grey = cv2.imread('cap.jpg')
color_threshold = 190
main_pane = img_grey[55:356, 12:310]
cv2.imshow('img', main_pane)
cv2.waitKey(0)
main_pane[main_pane<color_threshold] = 0
main_pane[main_pane>=color_threshold] = 255
cv2.imshow('img', main_pane)
cv2.waitKey(0)
main_pane = cv2.blur(main_pane, (5, 5))
main_pane = cv2.cvtColor(main_pane, cv2.COLOR_BGR2GRAY)

ret3, main_pane = cv2.threshold(main_pane,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
main_pane = cv2.adaptiveThreshold(main_pane, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 1)
cv2.imshow('img', main_pane)
cv2.waitKey(0)