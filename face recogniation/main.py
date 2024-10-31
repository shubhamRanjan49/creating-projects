import cv2
face_cap = cv2.CascadeClassifier("c:/Users/HP/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

video_cap = cv2.VideoCapture(0)
while True:
    ret,video = video_cap.read()
    Col = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        Col,
        scaleFactor=1.1,
        minNeighbors=
        5,
        minSize=(40,40),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video,(x,y) , (x+w,y+h),(0,255,0),2)
        
    if not ret:
        print("error: failed to capture video")
        break

    cv2.imshow('video', video)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break  
video_cap.release() 
cv2.destroyAllWindows()            

