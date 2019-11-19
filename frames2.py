
import cv2


cap = cv2.VideoCapture("./video/input_video_sample1.mov")

i = -1
print cap.isOpened()
#input_video_sample1.mov
while(cap.isOpened()):
    ret, frame = cap.read()
    i=i+1
    if i < 450:
        continue
    print ret,i
    if ret == True:
        cv2.imwrite('./mltproject/neg_car/input_video_sample1_'+ str(i) + '.jpg',frame)
			
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #i=i+1
cap.release()
