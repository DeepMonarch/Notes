import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 1\\sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # cv2.COLOR_BGR2GRAY converts BGR to Grayscale
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save grayscale image
    cv2.imwrite('grayscale_image.jpg', gray_image)