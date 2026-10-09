# import cv2


# cap = cv2.VideoCapture(0)
# center =(700,350)
# radius = 200
# color = (100,0,0)
# thickness = 3

# while True:
#     ret , frame = cap.read()
#     if not ret:
#         break
#     else:
#         cv2.circle(frame, center, radius, color, thickness)
#         cv2.imshow('Video', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows


import cv2

cap = cv2.VideoCapture(0)
topleft = (250,450)
bottamright = (650,70)
color = (0,0,110)
thickness = 3

while True:
    ret , frame = cap.read()
    if not ret:
        break
    else:
        cv2.rectangle(frame, topleft, bottamright, color, thickness)
        cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()