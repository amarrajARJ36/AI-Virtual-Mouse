import cv2


#Image blurring using GaussianBlur method
# image = cv2.imread('/Users/amarraj/Desktop/Srishti/dog.jpeg')
# blurred_image = cv2.GaussianBlur(image,(99,99),0)
# blurred_image2 = cv2.GaussianBlur(image,(23,23),0) #kernal size should be odd 
# cv2.imshow("orginal image",image)
# cv2.imshow("image",blurred_image)
# cv2.imshow("image2",blurred_image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows


# Edge Detection using Canny method
# image = cv2.imread("/Users/amarraj/Desktop/Srishti/dog.jpeg")
# grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred_image = cv2.GaussianBlur(grayscale,(3,3),1)
# edges = cv2.Canny(blurred_image,100,190)
# cv2.imshow('image', edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Edge detection on camera
# cap = cv2.VideoCapture(0)
# while True:
#     ret ,frame = cap.read()
#     grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(grayscale,(45,45),1)
#     edges = cv2.Canny(blurred,80,100)
#     cv2.imshow('frame',edges)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindow()


import mediapipe as mp


# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Capture video from webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

   
    cv2.imshow('Hand Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
