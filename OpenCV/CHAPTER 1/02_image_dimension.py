import cv2
image = cv2.imread('C:\\Users\\ALL IS WELL\\OneDrive\\Desktop\\OpenCV\\CHAPTER 1\\sample.jpg')

if image is None:
    print("Error: Could not load image.")
else:
    print(f"Image dimensions: {image.shape}") # prints (height, width, channels)
    h,w,c = image.shape
    print(f"Height: {h}, Width: {w}, Channels: {c}")