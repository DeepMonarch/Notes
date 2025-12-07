import cv2
# reading image
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 1\\sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")
    
    # displaying image
    cv2.imshow('Loaded Image', image) # display the image in a window
    cv2.waitKey(0) # 0 means wait indefinitely until a key is pressed
    cv2.destroyAllWindows() # close all OpenCV windows
    
    # saving image
    cv2.imwrite('saved_image.jpg', image)
    