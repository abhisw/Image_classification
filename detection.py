# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:00:16 2016

@author: RAM
"""

import numpy as np
import cv2


#cycle_cascade = cv2.CascadeClassifier('record/cas_B/cascade.xml')
#bike_cascade = cv2.CascadeClassifier('record/cas_C/cascade.xml')


cycle_cascade = cv2.CascadeClassifier('/Users/abhishekyadav/Desktop/mltproject/data/cascade.xml')
#bike_cascade = cv2.CascadeClassifier('D:\\mltproject\\record\\cas_C\\cascade.xml')

#cap = cv2.VideoCapture('/media/john/games/mltproject/video/input_video_sample1.mov')
cap = cv2.VideoCapture("/Users/abhishekyadav/Desktop/video/input_video_sample1.mov")
print cap.isOpened()

i= 1;
j= 0;

while(cap.isOpened()):

    ret, frame = cap.read()
    j = j+1
    if j < 20:
         continue
    if ret==True:
        j = 0
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cycles = cycle_cascade.detectMultiScale(gray, 18,18)
    #change it accordingly
        for (x,y,w,h) in cycles:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,123,66),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,'cycle',(x,y),font,0.5,(0,255,255),2)


#bikes = bike_cascade.detectMultiScale(gray, 15,15)
#        for (x,y,w,h) in bikes:
#            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,66),2)
#           font = cv2.FONT_HERSHEY_SIMPLEX
#           cv2.putText(frame,'bike',(x,y),font,0.5,(255,0,255),2)

            
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
# out.release()
cv2.destroyAllWindows()
