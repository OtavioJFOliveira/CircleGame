import cv2
from cvzone.HandTrackingModule import HandDetector
from random import randint

cap = cv2.VideoCapture(0)
w, h = 1280, 720
cap.set(3, w)
cap.set(4, h)

circleColor = 255,0,0
circleX, circleY, circleRad = 200, 200, 100

handDetector = HandDetector(detectionCon=0.8)

while True:
    status, img = cap.read()
    img = cv2.flip(img, 1)
    img = handDetector.findHands(img)
    list, _ = handDetector.findPosition(img)

    if list:
        fingerPoint = list[8]

        if (circleX - circleRad ) < fingerPoint[0] < (circleX + circleRad) and (circleY - circleRad) < fingerPoint[1]< (circleY + circleRad):
            circleColor = 0, 0, 255
            circleX = randint(circleRad, w-circleX)
            circleY = randint(circleRad, h-circleY)

        else:
            circleColor = 255, 0, 0

    cv2.circle(img, (circleX,circleY), circleRad, circleColor, cv2.FILLED)
    cv2.imshow("Image", img)
    circleY = circleY+1
    cv2.waitKey(1)

