##
import cv2

cap = cv2.VideoCapture(".mp4")

i = 0
print cap.isOpened()

while(cap.isOpened()):
    ret, frame = cap.read()
    print ret,i % (18*3)
    if ret == True:
        cv2.imwrite('C:\\Users\\dell\\Documents\\Python_ml\\video_data\\negative\\neg10_'+ str(i) + '.jpg',frame)
    else:
		break
			
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()