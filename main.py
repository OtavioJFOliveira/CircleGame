import cv2
from cvzone.HandTrackingModule import HandDetector
from random import randint

cap = cv2.VideoCapture(0)
w, h = 1280, 720
cap.set(3, w)
cap.set(4, h)

circleColor = 255,0,0
circleX, circleY = 200, 200
circleRad = 50

handDetector = HandDetector(detectionCon=0.8)

class DragCircle():
    def __init__(self, positionCenter, rad=circleRad):
        self.positionCenter = positionCenter
        self.rad = rad

    def update(self, fingerPoint):
        circleX, circleY = self.positionCenter
        circleRad = self.rad
        if (circleX - circleRad) < fingerPoint[0] < (circleX + circleRad) and \
                (circleY - circleRad) < fingerPoint[1] < (circleY + circleRad):
            self.positionCenter = randint(circleRad, w-circleX), 0 - circleRad

circleList = []
for x in range (5):
    circleList.append(DragCircle([randint(circleRad, w-circleX), 0]))

while True:
    status, img = cap.read()
    img = cv2.flip(img, 1)
    img = handDetector.findHands(img)
    list, _ = handDetector.findPosition(img)

    if list:
        fingerPoint = list[8]

        for circle in circleList:
            circle.update(fingerPoint)

    for circle in circleList:
        circleX, circleY = circle.positionCenter
        circleRad = circle.rad
        cv2.circle(img, (circleX,circleY), circleRad, circleColor, cv2.FILLED)
        circle.positionCenter = circleX, circleY + 3
        if circleY > h + circleRad:
            circle.positionCenter = randint(circleRad, w-circleX), 0 - circleRad
    cv2.imshow("Image", img)
    cv2.waitKey(1)

