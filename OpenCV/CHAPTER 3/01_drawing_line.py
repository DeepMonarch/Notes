import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 3\\sample.jpg')
if image is None:
    print("Error: Could not load image.")
else:
    # Drawing a line - cv2.line(image, start_point, end_point, color, thickness)
    line_image = image.copy()
    cv2.line(line_image, (50, 50), (800, 800), (0, 255, 0), 10)  # Green line with thickness 10

    cv2.imshow('Line Image', line_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save line image
    cv2.imwrite('line_image.jpg', line_image)