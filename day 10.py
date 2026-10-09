# import autopy


# autopy.mouse.move(100, 100 )
# autopy.mouse.click()
# autopy.mouse.click(autopy.mouse.Button.RIGHT)

# screenshot = autopy.bitmap.capture_screen()
# Save the screenshot to a file
# screenshot.save('/Users/amarraj/Desktop/Srishti/screenshot.jpeg')




# import pyautogui

# Scroll up by 10 units
# pyautogui.scroll(10)

# Scroll down by 10 units
# pyautogui.scroll(-10)





# import cv2
# import mediapipe as mp
# import pyautogui
# import numpy as np


# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1)
# mp_drawing = mp.solutions.drawing_utils

# # Webcam setup
# cap = cv2.VideoCapture(0)

# # Get screen size
# screen_width, screen_height = pyautogui.size()

# while True:
#     success, img = cap.read()
#     if not success:
#         break

    
#     img = cv2.flip(img, 1)
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = hands.process(img_rgb)


#     frame_height, frame_width, _ = img.shape

#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             # Get the index finger tip position
#             index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

#             # Convert the coordinates
#             finger_x = int(index_finger_tip.x * frame_width)
#             finger_y = int(index_finger_tip.y * frame_height)

#             # Convert to screen coordinates
#             screen_x = np.interp(finger_x, [0, frame_width], [0, screen_width])
#             screen_y = np.interp(finger_y, [0, frame_height], [0, screen_height])

#             # Move the mouse
#             pyautogui.moveTo(screen_x, screen_y)


           
#             mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             x = str(screen_x)
#             y = str(screen_y)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             font_scale = 1
#             color = (100,100,0)
#             thickness = 2
            
#             cv2.putText(img ,x, (800,50),font,font_scale, color, thickness)
#             cv2.putText(img ,y, (990,50),font,font_scale, color, thickness)
#             cv2.putText(img ,'x', (850,80),font,font_scale, color, thickness)
#             cv2.putText(img ,'y', (1040,80),font,font_scale, color, thickness)

#     cv2.imshow('Hand Tracking', img )

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()





# import cv2
# import mediapipe as mp
# import pyautogui
# import numpy as np

# # Initialize MediaPipe Face Mesh
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)
# mp_drawing = mp.solutions.drawing_utils

# # Webcam setup
# cap = cv2.VideoCapture(0)

# # Get screen size
# screen_width, screen_height = pyautogui.size()

# while True:
#     success, img = cap.read()
#     if not success:
#         break

#     img = cv2.flip(img, 1)
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     results = face_mesh.process(img_rgb)

#     frame_height, frame_width, _ = img.shape

#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             # Get the left eye's center landmark (landmark 159 or 145 typically corresponds to the left eye center)
#             left_eye_center = face_landmarks.landmark[159]

#             # Convert the coordinates
#             eye_x = int(left_eye_center.x * frame_width)
#             eye_y = int(left_eye_center.y * frame_height)

#             # Convert to screen coordinates
#             screen_x = np.interp(eye_x, [0, frame_width], [0, screen_width])
#             screen_y = np.interp(eye_y, [0, frame_height], [0, screen_height])

#             # Move the mouse
#             pyautogui.moveTo(screen_x, screen_y)

#             # Draw landmarks and coordinates
#             mp_drawing.draw_landmarks(img, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)

#             x = str(screen_x)
#             y = str(screen_y)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             font_scale = 1
#             color = (100, 100, 0)
#             thickness = 2
            
#             cv2.putText(img, x, (800, 50), font, font_scale, color, thickness)
#             cv2.putText(img, y, (990, 50), font, font_scale, color, thickness)
#             cv2.putText(img, 'x', (850, 80), font, font_scale, color, thickness)
#             cv2.putText(img, 'y', (1040, 80), font, font_scale, color, thickness)

#     cv2.imshow('Face Mesh Tracking', img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

 
import cv2
import mediapipe as mp
import autopy
import numpy as np


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

# Webcam setup
cap = cv2.VideoCapture(0)

# Get screen size
screen_width, screen_height = autopy.screen.size()

while True:
    success, img = cap.read()
    if not success:
        break

    
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)


    frame_height, frame_width, _ = img.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the index finger tip position
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Convert the coordinates
            finger_x = int(index_finger_tip.x * frame_width)
            finger_y = int(index_finger_tip.y * frame_height)

            # Convert to screen coordinates
            screen_x = np.interp(finger_x, [0, frame_width], [0, screen_width])
            screen_y = np.interp(finger_y, [0, frame_height], [0, screen_height])

            # Move the mouse
            autopy.mouse.move(screen_x, screen_y)


           
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x = str(screen_x)
            y = str(screen_y)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (100,100,0)
            thickness = 2
            
            cv2.putText(img ,x, (800,50),font,font_scale, color, thickness)
            cv2.putText(img ,y, (990,50),font,font_scale, color, thickness)
            cv2.putText(img ,'x', (850,80),font,font_scale, color, thickness)
            cv2.putText(img ,'y', (1040,80),font,font_scale, color, thickness)

    cv2.imshow('Hand Tracking', img )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




















#