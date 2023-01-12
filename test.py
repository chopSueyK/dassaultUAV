import cv2
from PIL import Image
import numpy as np


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()
#vid = cv2.VideoCapture(0)

def detect(frame):
    bounding_box_cordinates, weights =  hog.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1
    
    cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
    cv2.imshow('output', frame)
    return frame

def detectByCamera(writer):   
    video = cv2.VideoCapture(0)
    print('Detecting people...')
    while True:
        check, frame = video.read()
        frame = cv2.resize(frame, (640, 480))
        frame = detect(frame)
        if writer is not None:
            writer.write(frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break


detectByCamera(cv2.VideoWriter("./output.avi",cv2.VideoWriter_fourcc(*'MJPG'), 10, (600,600)))

video.release()
cv2.destroyAllWindows()
image = Image.fromarray(frame)
image.save("file.jpg")
print(type(frame))
vid.release()
out.release()
cv2.destroyAllWindows()
cv2.waitKey(1)




"""while(True):
    #Start capturing
    ret, frame = vid.read()
    print("www")
    #Grayscale
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    ret,frame = cv2.threshold(frame,50,255,cv2.THRESH_BINARY)
    
    #Detect
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))
    
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    
    out.write(frame.astype('uint8'))

    cv2.imshow('frame',frame)
    
    #Exit key = q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 """
