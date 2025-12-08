import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 2\\sample.jpg')
if image is None:
    print("Error: Could not load image.")
else:
    # Get image dimensions
    # h,w,c = image.shape # height, width, channels
    # so we only need height and width
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Rotate image by 45 degrees
    # center = w//2, h//2 (x,y)
    M = cv2.getRotationMatrix2D(center, 45, 1.0) # angle=45, scale=1.0 (scale is how much to zoom in/out)
    rotated_image = cv2.warpAffine(image, M, (w, h))

    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save rotated image
    cv2.imwrite('rotated_image.jpg', rotated_image)