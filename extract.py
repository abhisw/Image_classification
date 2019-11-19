import pickle

import cv2
#import cv



for name in ['datasample1','input_video_sample1','input_video_sample2','input_video_sample3','videosample5']:

	for lab in ['Motorcycle','Autorickshaw','Rickshaw']:
#for name in ['nov9201Motorcycle5-2','dec21h1330']:
		cap = cv2.VideoCapture('/media/john/games/mltproject/video/'+ name + '.mov')
		#cap = cv2.VideoCapture('D:\\mltproject\\video\\nov92015-2.dav')
		pkl = pickle.load(open(name +'.pkl','rb'))

		print cap.isOpened()

		for i in range(len(pkl)):
			if pkl[i]['label'] == lab:
				for j in range(len(pkl[i]['boxes'])):
					tmp = pkl[i]['boxes'][j]
					if tmp.lost != 1 and tmp.occluded != 1:
						cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,tmp.frame)
						ret, frame = cap.read()
						print ret,j
						try:
							cv2.imwrite('/media/john/games/mltproject/' +lab + '/'+ name + '_' + str(i)+'_'+str(j) + '.jpg',frame[tmp.ytl:tmp.ybr,tmp.xtl:tmp.xbr])
		  				except:
							print 'pass'
							pass
		cap.release()