import cv2 

trained_face_data=cv2.CascadeClassifier('C:\\Users\\harsh\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

img = cv2.imread("C:\\Users\\harsh\\Desktop\\PYTHON\\Face detection\\mia.png")

greyscaled_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates= trained_face_data.detectMultiScale(greyscaled_img)

print(face_coordinates)


(x,y,w,h)=face_coordinates[0]
cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
#cv2.rectangle(img, (42,36) , (42+101 , 36+101) , (0,255,0) , 2)

cv2.imshow("Clever Programmer Face Detector", img)
cv2.waitKey()


print("Code completed")
