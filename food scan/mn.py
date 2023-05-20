import cv2
from cvzone.ClassificationModule import Classifier
import d_set

cap = cv2.VideoCapture(0)# to use default web_cam use " 0 "
 # to use external webcam use " 1 "
myClassifier = Classifier('assect\model1.h5','assect\model.txt')
print("load complete")
# fpsReader = cvzone.FPS()

while True:
    _,img =  cap.read()
    prediction, index = myClassifier.getPrediction(img)
    if index == 1 :
        d_set.apple()
    elif index == 2 :
        d_set.orange()
    elif index == 3 :
        d_set.banana()
    elif index == 4 :
        d_set.carrots()
    elif index == 5 :
        d_set.lemon()
    elif index == 6:
        d_set.mango()
    elif index == 8 :
        d_set.chilli()

  #  print(prediction,index)
    # fps, _ = fpsReader.update()

    cv2.imshow("image",img)
    cv2.waitKey(1)
