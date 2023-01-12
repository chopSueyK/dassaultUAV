import cv2
import numpy 
import torch
import re


model = torch.hub.load("ultralytics/yolov5", 'yolov5s')

#cv2.startWindowThread()
video = cv2.VideoCapture(0)
i = 0
while True:
    check, frame = video.read()
    #frame = cv2.resize(frame, (640, 640))
    result = model(frame, size = 640)
    cv2.imshow('output', frame)
    x =result.tolist()[0]
    s = ""
    for pred in x.pred:
        if pred.shape[0]:
            for c in pred[:, -1].unique():
                        n = (pred[:, -1] == c).sum()  # detections per class
                        s += f"{n} {x.names[int(c)]}{'s' * (n > 1)}, "  # add to string
    if re.search("person", s):
        print(result)
        print(True)
    else:
        print(False)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    