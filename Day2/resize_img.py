import cv2

#Resizing an image
# img = cv2.imread('resources/lambo.png')  # Replace 'lambo.png' with your image file path
# print("Original image shape:", img.shape)  # Print the original image dimensions to the console 
# resized_img = cv2.resize(img, (300, 300))  # Resize the image to 300x300 pixels 

# print("Resized image shape:", resized_img.shape)  # Print the shape of the resized image
# cv2.imshow('Original Image', img)  # Display the original image
# cv2.imshow('Resized Image', resized_img)  # Display the resized image
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()  # Close all OpenCV windows

# Cropping an image
img = cv2.imread('resources/lambo.png')  # Replace 'lambo.png' with your image file path
cropped_img = img[100:400, 200:500]  # Crop the image (y1:y2, x1:x2)

print("Original image shape:", img.shape)  # Print the original image dimensions to the console 
print("Cropped image shape:", cropped_img.shape)  # Print the shape of the cropped image
cv2.imshow('Original Image', img)  # Display the original image
cv2.imshow('Cropped Image', cropped_img)  # Display the cropped image
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows



