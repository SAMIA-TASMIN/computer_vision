import cv2
import numpy as np

img = cv2.imread('resources/lena.png')  # Read the image from the specified path

img_hor = np.hstack((img, img))  # Horizontally stack the image with itself
img_ver = np.vstack((img, img))  # Vertically stack the image with itself


cv2.imshow('Horizontal', img_hor)  # Display the horizontally stacked image
cv2.imshow('Vertical', img_ver)  # Display the vertically stacked image
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows
