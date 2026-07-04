import cv2
import numpy as np

width, height = 260, 360

img = cv2.imread('resources/cards.jpg')  # Read the image from the specified path
print("Image shape:", img.shape)  # Print the shape of the image

pts1 = np.float32([[752, 118], [1120, 265], [540, 668], [871, 830]])  # Define the source points for perspective transformation

pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # Define the destination points for perspective transformation   

matrix = cv2.getPerspectiveTransform(pts1, pts2)  # Compute the perspective transformation matrix       
imgOutput = cv2.warpPerspective(img, matrix, (width, height))  # Apply the perspective transformation to the image  
cv2.imshow('Image', img)  # Display the original image
cv2.imshow('Output', imgOutput)  # Display the transformed image

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows

