import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 2\\sample.jpg')
if image is None:
    print("Error: Could not load image.")
else:
    # Flip image horizontally
    flipped_image = cv2.flip(image, 1) # (flip code) 1 for horizontal, 0 for vertical, -1 for both axes

    cv2.imshow('Flipped Image', flipped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save flipped image
    cv2.imwrite('flipped_image.jpg', flipped_image)