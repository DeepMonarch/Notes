import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 2\\sample.jpg')
if image is None:
    print("Error: Could not load image.")
else:
    # Crop image: [y1:y2, x1:x2]
    cropped_image = image[50:250, 100:300] # Cropping a 200x200 region
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save cropped image
    cv2.imwrite('cropped_image.jpg', cropped_image)
    
    # x axis top to bottom Pixels
    # y axis left to right Pixels
    # image[y1:y2, x1:x2] x1,y1 is the starting point and x2,y2 is the ending point