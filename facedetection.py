import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade/haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade/haarcascade_smile.xml')

cap = cv.VideoCapture(0)
counter = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (216, 191, 216), 1)
        
    
        cv.putText(frame, "Jiya", (x+5, y+20),
                       cv.FONT_HERSHEY_SIMPLEX, fontScale=0.6, color=(216, 191, 216), thickness= 1)
       

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        
        if len(eyes) > 0:
            counter = 0
        else:
            counter += 1

        if counter > 2:
            cv.putText(frame, "Sleeping", (x+60, y+20),
                       cv.FONT_HERSHEY_SIMPLEX, fontScale=0.6, color=(0, 0, 255), thickness= 2)
        else:
            cv.putText(frame, "Eye Detected", (x, y-10),
                       cv.FONT_HERSHEY_SIMPLEX, fontScale=0.6, color=(255, 120, 0), thickness= 2)
        
      
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smile) > 0:
            cv.putText(frame, "Smiling...", (x+60, y+h - 20),
                       cv.FONT_HERSHEY_SIMPLEX, fontScale=0.6, color=(255, 0, 255), thickness= 2)
        
        

    cv.imshow("Face Detection", frame)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv.destroyAllWindows()


