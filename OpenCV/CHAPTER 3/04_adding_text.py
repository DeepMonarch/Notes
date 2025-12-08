import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 3\\sample.jpg')
if image is None:
    print("Error: Could not load image.")
else:
    # adding text - cv2.putText(image, text, position, font, font_scale, color, thickness, lineType)
    text_image = image.copy()
    cv2.putText(text_image, 'OpenCV Text', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 255), 10, cv2.LINE_AA)

    cv2.imshow('Text Image', text_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save text image
    cv2.imwrite('text_image.jpg', text_image)