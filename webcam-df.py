print("please wait")
import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 640) #lebar
cam.set(4, 480) #tinggi
fd = cv2.CascadeClassifier('algoritma/haarcascade_frontalface_default.xml')
while True:
    retV, frame = cam.read()
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f = fd.detectMultiScale(gr, 1.7, 5) #var, f. skala, minNeighbours
    for (x, y, w, h) in f:
        frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2) #koor,waarna,tebal
    cv2.imshow('webq',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
print("kamera dimatikan (anda menekan tombol 'esc')")
cam.release()
cv2.destroyAllWindows()
    
