import cv2
import numpy as np

# Increases the contrast of the original image
def contrast_strect(image):
  in_min = np.percentile(image, 5)
  in_max = np.percentile(image, 95)

  out_min = 0.0
  out_max = 255.0

  out = image - in_min
  out *= ((out_min - out_max) / (in_min - in_max))
  out += in_min

  return out


def calc_ndvi(image):
  b, g, r = cv2.split(image)
  bottom = (r.astype(float) + b.astype(float))
  bottom[bottom==0] = 0.01
  ndvi = (b.astype(float) - r) / bottom
  return ndvi
