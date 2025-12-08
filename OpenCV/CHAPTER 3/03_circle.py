import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 3\\sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Drawing a circle - cv2.circle(image, center, radius, color, thickness)
    circle_image = image.copy()
    cv2.circle(circle_image, (400, 400), 200, (0, 0, 255), -1)  # Red circle with thickness -1 (filled), -1 means filled circle and other positive values mean thickness

    cv2.imshow('Circle Image', circle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save circle image
    cv2.imwrite('circle_image.jpg', circle_image)