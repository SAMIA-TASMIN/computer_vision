import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # Create a black image of size 512x512 pixels
print("Image shape:", img.shape)  # Print the shape of the image

img[:] = (0, 255, 0)  # Fill the image with blue color (BGR format)
# cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # Draw a blue diagonal line

# Draw a rectangle
# cv2.rectangle(img, (100, 100), (400, 400), (0, 0, 255), 3)  # Draw a green rectangle
# cv2.circle(img, (256, 256), 100, (255, 0, 0), 4)  # Draw a filled red circle

cv2.putText(img, 'OpenCV', (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)  # Add text to the image 
cv2.imshow('Image ', img)  # Display the image
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows