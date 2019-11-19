import pickle

import cv2
import cv

cap = cv2.VideoCapture('/media/john/games/mltproject/video/nov92015-1.dav')
pkl = pickle.load(open('nov92015-1.pkl','rb'))

print cap.isOpened()

for i in range(len(pkl)):
	if pkl[i]['label'] == 'Person':
		for j in range(len(pkl[i]['boxes'])):
			tmp = pkl[i]['boxes'][j]
			if tmp.lost != 1 and tmp.occluded != 1:
				cap.set(cv.CV_CAP_PROP_POS_FRAMES,tmp.frame)
				ret, frame = cap.read()
				print ret,j
				try:
					cv2.imwrite('/media/john/games/mltproject/temp2/nov1_per'+ str(i)+'_'+str(j) + '.jpg',frame[tmp.ytl:tmp.ybr,tmp.xtl:tmp.xbr])
				except:
					print 'pass'
					pass
cap.release()