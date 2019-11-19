
import cv2


cap = cv2.VideoCapture("./video/videosample5.mov")

i = 0
print cap.isOpened()
#input_video_sample1.mov
while(cap.isOpened()):
    ret, frame = cap.read()
    print ret,i
    if ret == True:
        cv2.imwrite('./frame_yadavcar/videosample5_'+ str(i) + '.jpg',frame)
			
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i=i+1
cap.release()
