import cv2
import numpy 
import torch
import re

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=320,
    capture_height=320,
    display_width=640,
    display_height=640,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


model = torch.hub.load("ultralytics/yolov5", 'yolov5s')

#cv2.startWindowThread()
video = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
i = 0
while True:
    check, frame = video.read()
    #frame = cv2.resize(frame, (640, 640))
    result = model(frame, size = 320)
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
    
