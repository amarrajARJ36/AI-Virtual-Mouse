import cv2
import mediapipe as mp
import time
import math
import numpy as np
import os
import urllib.request

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (0, 17), (17, 18), (18, 19), (19, 20)
]


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = float(detectionCon) if isinstance(detectionCon, (int, float, str)) and str(detectionCon).replace('.','',1).isdigit() else 0.5
        self.trackCon = float(trackCon) if isinstance(trackCon, (int, float, str)) and str(trackCon).replace('.','',1).isdigit() else 0.5

        self.tipIds = [4, 8, 12, 16, 20]
        self.results = None
        self.lmList = []

        if hasattr(mp, 'solutions') and hasattr(mp.solutions, 'hands'):
            self.use_legacy = True
            self.mpHands = mp.solutions.hands
            self.hands = self.mpHands.Hands(
                static_image_mode=self.mode,
                max_num_hands=self.maxHands,
                min_detection_confidence=self.detectionCon,
                min_tracking_confidence=self.trackCon
            )
            self.mpDraw = mp.solutions.drawing_utils
            self.mpDrawStyles = mp.solutions.drawing_styles if hasattr(mp.solutions, 'drawing_styles') else None
        else:
            self.use_legacy = False
            from mediapipe.tasks import python
            from mediapipe.tasks.python import vision

            model_path = os.path.join(os.path.dirname(__file__), 'hand_landmarker.task')
            if not os.path.exists(model_path):
                url = 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task'
                urllib.request.urlretrieve(url, model_path)

            base_options = python.BaseOptions(model_asset_path=model_path)
            options = vision.HandLandmarkerOptions(
                base_options=base_options,
                running_mode=vision.RunningMode.IMAGE,
                num_hands=self.maxHands,
                min_hand_detection_confidence=self.detectionCon,
                min_hand_presence_confidence=self.trackCon
            )
            self.landmarker = vision.HandLandmarker.create_from_options(options)

    def findHands(self, img, draw=True, flipType=True):
        """Finds all hands in a frame and optionally draws landmarks."""
        if flipType:
            img = cv2.flip(img, 1)

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if self.use_legacy:
            self.results = self.hands.process(imgRGB)
            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    if draw:
                        if self.mpDrawStyles:
                            self.mpDraw.draw_landmarks(
                                img,
                                handLms,
                                self.mpHands.HAND_CONNECTIONS,
                                self.mpDrawStyles.get_default_hand_landmarks_style(),
                                self.mpDrawStyles.get_default_hand_connections_style()
                            )
                        else:
                            self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        else:
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
            self.results = self.landmarker.detect(mp_image)
            if self.results and self.results.hand_landmarks:
                h, w, _ = img.shape
                for handLms in self.results.hand_landmarks:
                    if draw:
                        for p1, p2 in HAND_CONNECTIONS:
                            pt1 = (int(handLms[p1].x * w), int(handLms[p1].y * h))
                            pt2 = (int(handLms[p2].x * w), int(handLms[p2].y * h))
                            cv2.line(img, pt1, pt2, (0, 255, 0), 2)
                        for lm in handLms:
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            cv2.circle(img, (cx, cy), 6, (255, 0, 255), cv2.FILLED)

        return img

    def findPosition(self, img, handNo=0, draw=True):
        """Fetches the position list [id, cx, cy] and bounding box of hands."""
        xList = []
        yList = []
        bbox = []
        self.lmList = []

        if self.use_legacy:
            if self.results and self.results.multi_hand_landmarks:
                if handNo < len(self.results.multi_hand_landmarks):
                    myHand = self.results.multi_hand_landmarks[handNo]
                    for id, lm in enumerate(myHand.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        xList.append(cx)
                        yList.append(cy)
                        self.lmList.append([id, cx, cy])
                        if draw:
                            cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        else:
            if self.results and self.results.hand_landmarks:
                if handNo < len(self.results.hand_landmarks):
                    myHand = self.results.hand_landmarks[handNo]
                    for id, lm in enumerate(myHand):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        xList.append(cx)
                        yList.append(cy)
                        self.lmList.append([id, cx, cy])
                        if draw:
                            cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        if xList and yList:
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)

        return self.lmList, bbox

    def fingersUp(self):
        """Checks which fingers are extended (1) or folded (0)."""
        fingers = []
        if len(self.lmList) == 0:
            return fingers

        # Thumb
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def findDistance(self, p1, p2, img, draw=True, r=15, t=3):
        """Finds distance between two landmark points."""
        if len(self.lmList) <= max(p1, p2):
            return 0, img, [0, 0, 0, 0, 0, 0]

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    print("Hand Tracking active! Press 'q' in the camera window to quit.")

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture image from camera.")
            break

        img = detector.findHands(img, draw=True, flipType=True)
        lmList, bbox = detector.findPosition(img, draw=True)

        if len(lmList) != 0:
            fingers = detector.fingersUp()
            length, img, _ = detector.findDistance(4, 8, img)

        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime

        cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


