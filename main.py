import cv2
import numpy as np
import fastiecm
from lib import display
from lib import ndvi 

def display(image, image_name):
  image = np.array(image, dtype=float)/float(255)
  shape = image.shape
  height = int(shape[0]/3)
  width = int(shape[1]/3)
  image = cv2.resize(image, (width, height))
  window = cv2.namedWindow(image_name)
  cv2.imshow(window, image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

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


image = cv2.imread("./park.png")
display(image, 'Original')
constrast = contrast_strect(image)
display(constrast, 'Contrasted')
ndvi = calc_ndvi(constrast)
display(ndvi, 'NDVI')
ndvi_con = contrast_strect(ndvi)
display(ndvi_con, 'NDVI Contrasted')
cv2.imwrite('ndvi_contrasted.png', ndvi_con)
color_mapped_prep = ndvi_con.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm.fastiecm)
display(color_mapped_image, 'Color mapped')
cv2.imwrite('color_mapped_image.png', color_mapped_image)
cv2.destroyAllWindows()