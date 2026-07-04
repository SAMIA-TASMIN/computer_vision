import cv2

##Reading images

# img = cv2.imread('resources/lena.png')  # Replace 'lena.png' with your image file path
# print(img)  # Print the image dimensions to the console
# cv2.imshow('Output', img)  # Display the image in a window
# cv2.waitKey(0)  # Wait for a key press to close the window


## Reading videos

# cap = cv2.VideoCapture("resources/elon.mp4")

# while True:
#     success, frame = cap.read()  # Read a frame from the video
#     cv2.imshow('Output', frame)  # Display the frame in a window

#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for 'q' key to exit
#         break


## Reading from webcam
# cap = cv2.VideoCapture(0)  # 0 is the default camera index

# cap.set(3, 640)  # Set the width of the video frame
# cap.set(4, 480)  # Set the height of the video frame

# while True:
#     success, frame = cap.read()  # Read a frame from the webcam
#     cv2.imshow('Output', frame)  # Display the frame in a window

#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for 'q' key to exit
#         break