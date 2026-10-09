import cv2
import time
import math
import numpy as np
import pyautogui
from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from HandTrackingModule import handDetector

import mediapipe as mp

#.................................................................................
import os

# Increase volume on macOS
def increase_volume_mac(steps=3):
    for _ in range(steps):
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")

# Decrease volume on macOS
def decrease_volume_mac(steps=3):
    for _ in range(steps):
        os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")


#.................................................................................

# Webcam settings
wCam, hCam = 720, 720
cap = cv2.VideoCapture(0)
pTime = 0

detector = handDetector()

mode = ''
active = 0


pyautogui.FAILSAFE = False

def putText(img, mode, loc=(250, 450), color=(0, 255, 255)):
    cv2.putText(img, str(mode), loc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, color, 3)

while True:
    success, img = cap.read()
    if not success or img is None:
        continue
    img = detector.findHands(img)
    # img = cv2.flip(img,1)
    lmList, bbox = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        fingers = detector.fingersUp()
        
        if (fingers == [0,0,0,0,0]) & (active == 0):
            mode = 'N'
        elif (fingers == [1, 1, 1, 1, 1]) & (active == 0):
            mode = 'Cursor'
            active = 1
        elif (fingers == [0, 1, 0, 0, 0] or fingers == [0, 1, 1, 0, 0]) & (active == 0):
            mode = 'Scroll'
            active = 1 
        elif ( fingers == [1, 1, 0, 0, 0] ) &  (active == 0):
            mode = 'Zoom'
            active = 1         
        elif (fingers == [1, 1, 0, 0, 1] ) &  (active == 0):
            mode = 'Volume'
            active = 1   

    if mode == 'Cursor':
        p = pyautogui.position()
        print(p)
        putText(img, mode)  
        cv2.rectangle(img, (5, 5), (1274, 715), (255, 255, 255), 3)
        if fingers[1:] == [0, 0, 0, 0]:
            active = 0
            mode = 'N'
        else:
            if len(lmList) != 0:
                x1, y1 = lmList[8][1], lmList[8][2]
                w, h = pyautogui.size()
                X = int(np.interp(x1, [110, 620], [w - 1,0]))
                Y = int(np.interp(y1, [20, 350], [0, h - 1]))
                cv2.circle(img, (lmList[8][1], lmList[8][2]), 7, (255, 255, 255), cv2.FILLED)
                cv2.circle(img, (lmList[4][1], lmList[4][2]), 10, (0, 255, 0), cv2.FILLED)
                cv2.circle(img, (lmList[12][1], lmList[12][2]), 10, (255, 255, 255), cv2.FILLED)
                pyautogui.moveTo(X, Y)
                
                if fingers == [0,1,1,1,1]:
                    cv2.circle(img, (lmList[4][1], lmList[4][2]), 10, (0, 0, 255), cv2.FILLED)
                    pyautogui.click()
                elif fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                    cv2.circle(img, (lmList[12][1], lmList[12][2]), 10, (0, 0, 255), cv2.FILLED)
                    pyautogui.rightClick()
            
    elif mode == 'Scroll':
        putText(img, mode)
            
        if len(lmList) != 0:
            if fingers == [0, 1, 0, 0, 0]:
                putText(img, 'U', loc=(200, 455), color=(0, 255, 0))
                pyautogui.scroll(3)
            elif fingers == [0, 1, 1, 0, 0]:
                putText(img, 'D', loc=(200, 455), color=(0, 0, 255))
                pyautogui.scroll(-3)
            elif fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'

    elif mode == 'Zoom':
        putText(img, mode)

        length, img, _ = detector.findDistance(4, 8, img)    
        
        if len(lmList) != 0:
            if fingers == [1,1,0,0,0]:
                if length > 250:  
                    pyautogui.hotkey('command', '+')   
                    putText(img, 'in', loc=(200, 455), color=(0, 255, 0)) 
                    print("Zooming In")
                elif length < 250:  
                    putText(img, 'out', loc=(200, 455), color=(0, 255, 0))
                    pyautogui.hotkey('command', '-')    
                    print("Zooming out")
            elif fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'

    elif mode == 'Volume':
        putText(img,mode)
        
        length, img, _ = detector.findDistance(4, 8, img)
        if len(lmList) != 0:
            if fingers == [1,1,0,0,1]:
                if length > 200:  
                    putText(img, 'up', loc=(200, 455), color=(0, 255, 0))
                    increase_volume_mac(1)    
                    print("volume incresing")
                elif length < 200: 
                    putText(img, 'down', loc=(200, 455), color=(0, 255, 0)) 
                    decrease_volume_mac(1)   
                    print("volume decreasing")
            elif fingers == [0, 0, 0, 0, 0]:
                active = 0
                mode = 'N'

#............................................

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (480, 50), cv2.FONT_ITALIC, 1, (255, 0, 0), 2)
    cv2.imshow('Hand LiveFeed', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
