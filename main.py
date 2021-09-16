import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

circleColor = 255,0,0
circleX, circleY, circleRad = 200, 200, 100

handDetector = HandDetector(detectionCon=8.0)

while True:
    status, img = cap.read()
    img = cv2.flip(img, 1)

    cv2.circle(img, (circleX,circleY), circleRad, circleColor, cv2.FILLED)
    cv2.imshow("Image", img)
    circleY = circleY+2
    cv2.waitKey(1)

