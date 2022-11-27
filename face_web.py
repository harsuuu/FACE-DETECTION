import cv2 
from random import randrange

trained_face_data=cv2.CascadeClassifier('C:\\Users\\harsh\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

#img = cv2.imread("C:\\Users\\harsh\\Desktop\\PYTHON\\Face detection\\viru.png")

webcam=cv2.VideoCapture(0)

while True:
    successful_frame_read, frame=webcam.read()

    greyscaled_frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates= trained_face_data.detectMultiScale(greyscaled_frame)

    #print(face_coordinates)
    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(255),randrange(255),randrange(255)),10)

    cv2.imshow('Clever Programmer Face Detector',frame)

    cv2.waitKey(1)

    print("Code completed")

'''face_coordinates= trained_face_data.detectMultiScale(greyscaled_img)

print(face_coordinates)


(x,y,w,h)=face_coordinates[0]
cv2.rectangle(img, (42,36), (42+101, 36+101), (0,0,255), 2)


cv2.imshow("Clever Programmer Face Detector", img)
cv2.waitKey()


print("Code completed")
'''