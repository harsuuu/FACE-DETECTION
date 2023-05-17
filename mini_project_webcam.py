import cv2

face_data=cv2.CascadeClassifier("C:\\Users\\harsh\\Desktop\\PYTHON\\Face detection\\haarcascade_frontalface_default.xml")

webcam=cv2.VideoCapture(0)

while True:
    successful_frame_read,frame=webcam.read()

    grayscaled_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coordinates=face_data.detectMultiScale(grayscaled_frame)

    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)

    cv2.imshow("Face detection",frame)

    cv2.waitKey(1)

    print("code completed")
