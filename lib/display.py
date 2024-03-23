# Helper function for creating cv2 windows
import cv2 
import numpy as np

def display(image, image_name):
  image = np.array(image, dtype=float)/float(255)
  shape = image.shape
  height = int(shape[0]/3)
  width = int(shape[1]/3)
  image = cv2.resize(image, (width, height))
  window = cv2.namedWindow(image_name)
  cv2.imshow(window, image)
  cv2.waitKey(0)