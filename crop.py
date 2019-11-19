import glob, os
from PIL import Image
os.chdir("/Users/abhishekyadav/Desktop/frame_yadavcar/")
cycle_list = []
i=0
        
for fil in glob.glob("*.jpg"):
        cycle_list.append(fil)
    
        img =  Image.open(fil)
        img2 = img.crop((0, 52, 639, 300))
        img2.save('video1'+str(i)+'.jpg')
        #cv2.imwrite('./frame_yadavcar/video1'+ str(i) + '.jpg',img2)
        #('/media/john/games/mltproject/'+ label +'.txt', 'w').close()
        #f = open('/media/john/games/mltproject/'+ label +'.txt','w')
        i=i+1