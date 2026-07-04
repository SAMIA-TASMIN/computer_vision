import cv2


# ### 1.Convert color images to grayscale
# img = cv2.imread('resources/lena.png')  # Replace 'lena.png' with your image file path
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert

# print(img.shape)  # Print the original image dimensions to the console
# print(gray_img.shape)  # Print the shape of the grayscale image

# cv2.imshow('Original Image', img)  # Display the original image
# cv2.imshow('Grayscale Image', gray_img)  # Display the grayscale image
# cv2.waitKey(0)  # Wait for a key press to close the window

# cv2.destroyAllWindows()  # Close all OpenCV windows
# cv2.imwrite('resources/lena_gray.png', gray_img)  # Save the grayscale image to a file

# #### 2. Convert to blur image
# img = cv2.imread('resources/lena.png')  # Replace 'lena.png' with your image file path
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
# blur_img = cv2.GaussianBlur(img_gray, (15, 15), 0)  # Apply Gaussian blur    

# print(img.shape)  # Print the original image dimensions to the console
# print(img_gray.shape)  # Print the shape of the grayscale image
# print(blur_img.shape)  # Print the shape of the blurred image

# cv2.imshow('Original Image', img)  # Display the original image
# cv2.imshow('Grayscale Image', img_gray)  # Display the grayscale image
# cv2.imshow('Blurred Image', blur_img)  # Display the blurred image
# cv2.waitKey(0)  # Wait for a key press to close the window
# cv2.destroyAllWindows()  # Close all OpenCV windows

#### 3. Convert to canny image
img = cv2.imread('resources/lena.png')  # Replace 'lena.png' with your image file path
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)  # Apply Gaussian blur
canny_img = cv2.Canny(img_gray, 100, 200)  # Apply Canny edge detection 


cv2.imshow('Original Image', img)  # Display the original image
cv2.imshow('Grayscale Image', img_gray)  # Display the grayscale image      
cv2.imshow('Blurred Image', img_blur)  # Display the blurred image
cv2.imshow('Canny Image', canny_img)  # Display the Canny edge detection image
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close all OpenCV windows