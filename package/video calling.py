import cv2


cap = cv2.VideoCapture(0)

while True:
    # Read a frame
    ret, frame = cap.read()
    if not ret:
        break
    # Display the frame
    cv2.imshow('Your Video',frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()