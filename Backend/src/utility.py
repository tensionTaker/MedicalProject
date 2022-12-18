import cv2
from PIL import Image
import numpy as np

def preprocess_image(img):
    gray=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
    resized=cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    processed_img = cv2.adaptiveThreshold(
    resized,255,                       # source image, max value
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, # threshold value using gaussian method
    cv2.THRESH_BINARY,              # format
    61,                             # block size
    11
    )
    return processed_img
