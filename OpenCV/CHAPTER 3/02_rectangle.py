import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 3\\sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    # Drawing a rectangle - cv2.rectangle(image, top_left, bottom_right, color, thickness)
    rectangle_image = image.copy()
    cv2.rectangle(rectangle_image, (100, 100), (700, 700), (255, 0, 0), 10)  # Blue rectangle with thickness 10

    cv2.imshow('Rectangle Image', rectangle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save rectangle image
    cv2.imwrite('rectangle_image.jpg', rectangle_image)