import pickle

import cv2
#import cv



for name in ['datasample1']:
	dic = {}
	cap = cv2.VideoCapture('/media/john/games/mltproject/video/'+ name + '.mov')
	print cap.isOpened()

	for lab in ['Car']:
		pkl = pickle.load(open(name +'.pkl','rb'))
		for i in range(len(pkl)):
			if pkl[i]['label'] == lab:
				#print 'here11111'

				for j in range(len(pkl[i]['boxes'])):
					#print 'here2222'
					tmp = pkl[i]['boxes'][j]
					fr = tmp.frame

					if fr in dic:
						dic[fr].append([tmp.ytl,tmp.ybr,tmp.xtl,tmp.xbr])
					else:
						dic[fr] = []
						dic[fr].append([tmp.ytl,tmp.ybr,tmp.xtl,tmp.xbr])

	print len(dic)

	for f in dic:
		if f < 1226:
			continue
		flag = 1
		lst = dic[f]
		cap.set(cv2.CAP_PROP_POS_FRAMES,f)
		ret, frame = cap.read()
		print ret,f
		for i in lst:
			y1,y2,x1,x2 = i
			for a in range(y1+1,y2-1):
				for b in range(x1+1,x2-1):
					try:
						frame[a,b] = [105,103,102]
					except:
						flag = 0
		try:
			if flag:
				cv2.imwrite('/media/john/games/mltproject/neg_tmp1/'+ name + '_' + str(f)+'.jpg',frame[1:1536,1:1800])
		except:
			print 'pass'
			pass				
		
					# if tmp.lost != 1 and tmp.occluded != 1:
					# 	cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES,tmp.frame)
					# 	ret, frame = cap.read()
					# 	print ret,j
					# 	try:
					# 		cv2.imwrite('/media/john/games/mltproject/' +lab + '/'+ name + '_' + str(i)+'_'+str(j) + '.jpg',frame[tmp.ytl:tmp.ybr,tmp.xtl:tmp.xbr])
		  	# 			except:
					# 		print 'pass'
					# 		pass
	cap.release()