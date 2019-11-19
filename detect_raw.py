# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:00:16 2016

@author: RAM
"""

import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('/media/john/games/mltproject/data/cascade.xml')
#face_cascade = cv2.CascadeClassifier('/media/john/games/mltproject/data_cycle/cycle_haar_cascade_defualt_20_20.xml')

# frame = cv2.imread('a5.jpg')
# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray,20,20)

# for (x,y,w,h) in faces:
#     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,123,66),2)     
    
# cv2.imshow('frame',frame)

# cv2.waitKey(0)
# cv2.destroyAllWindows()







#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (2048,1536),True)
cap = cv2.VideoCapture('/media/john/games/mltproject/video/datasample1.mov')

print cap.isOpened()

i= 0;
j= 0;

while(cap.isOpened()):

    ret, frame = cap.read()
    j = j+1
    if j < 20:
         continue
    if ret==True:
        j = 0
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 7,7)
        for (x,y,w,h) in faces:            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,123,66),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,'two_wheeler',(x+w/2,y+h/2),font,0.5,(0,255,255),2)
#             to_save = frame[y-5:y+h+5,x-5:x+w+5]
#             name = "C:\\Users\\dell\\Documents\\Python_ml\\faces\\"+"face"+str(i)+".png"
#             i = i+1
#             #cv2.imwrite(name,to_save)
            
#         # write the flipped frame
#         #.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
# out.release()
cv2.destroyAllWindows()