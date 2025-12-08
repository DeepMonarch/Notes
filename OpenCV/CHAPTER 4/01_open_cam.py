import cv2

cap = cv2.VideoCapture(1) # 0 for default camera, 1 for external camera

while True:
    ret, frame = cap.read() # ret is a boolean indicating if the frame was read correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('Video Feed', frame)

    # Press 'q' to exit the video window
    if cv2.waitKey(1) & 0xFF == ord('q'): # 113 == 113 is ASCII for 'q'
        break

cap.release()
cv2.destroyAllWindows()