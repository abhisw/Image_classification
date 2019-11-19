import glob, os
from PIL import Image

for label in ['temp']:#['car','Autorickshaw','person','Motorcycle','Rickshaw','cycle','neg']:
	os.chdir("/Users/abhishekyadav/Desktop/mltproject/"+ label)

	cycle_list = []
	for fil in glob.glob("*.jpg"):
	    cycle_list.append(fil)


	#('/media/john/games/mltproject/'+ label +'.txt', 'w').close()
	#f = open('/media/john/games/mltproject/'+ label +'.txt','w')
		
	open('/Users/abhishekyadav/Desktop/mltproject/neg_'+ label +'.txt', 'w').close()
	f = open('/Users/abhishekyadav/Desktop/mltproject/neg_'+ label +'.txt','w')
	for name in cycle_list:
	    #im = Image.open(name)
	    #width, height = im.size
	    #f.write(label+'/'+ name +' 1 0 0 '+str(width-1)+' '+str(height-1)+'\n')
	    f.write(label+'/'+ name +'\n')
	    
	f.close()
