import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 2\\sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Resize image
    resized_image = cv2.resize(image, (300, 300)) # first *width then *height
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save resized image
    cv2.imwrite('resized_image.jpg', resized_image)