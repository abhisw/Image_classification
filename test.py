import os, struct
from array import array as pyarray
import numpy as np#import append, array, int8, uint8, zeros

dataset="training"
digits=np.arange(10)
path="."
"""
Loads MNIST files into 3D numpy arrays

Adapted from: http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py
"""

#if dataset == "training":
fname_img = os.path.join(path, 'train-images.idx3-ubyte')
fname_lbl = os.path.join(path, 'train-labels.idx1-ubyte')
#elif dataset == "testing":
fname_img2 = os.path.join(path, 't10k-images.idx3-ubyte')
fname_lbl2 = os.path.join(path, 't10k-labels.idx1-ubyte')
#else:
#   raise ValueError("dataset must be 'testing' or 'training'")

flbl = open(fname_lbl, 'rb')
magic_nr, size = struct.unpack(">II", flbl.read(8))
lbl = pyarray("b", flbl.read())
flbl.close()

fimg = open(fname_img, 'rb')
magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
img = pyarray("B", fimg.read())
fimg.close()

ind = [ k for k in range(size) if lbl[k] in digits ]
N = len(ind)

images = np.zeros((N, rows, cols), dtype=np.uint8)
labels = np.zeros((N, 1), dtype=np.int8)
for i in range(len(ind)):
    images[i] = np.array(img[ ind[i]*rows*cols : (ind[i]+1)*rows*cols ]).reshape((rows, cols))
    labels[i] = lbl[ind[i]]





flbl2 = open(fname_lbl2, 'rb')
magic_nr2, size2 = struct.unpack(">II", flbl2.read(8))
lbl2 = pyarray("b", flbl2.read())
flbl2.close()

fimg2 = open(fname_img2, 'rb')
magic_nr2, size2, rows2, cols2 = struct.unpack(">IIII", fimg2.read(16))
img2 = pyarray("B", fimg2.read())
fimg2.close()

ind2 = [ k for k in range(size2) if lbl2[k] in digits ]
N2 = len(ind2)

images2 = np.zeros((N2, rows2, cols2), dtype=np.uint8)
labels2 = np.zeros((N2, 1), dtype=np.int8)
for i in range(len(ind2)):
    images2[i] = np.array(img2[ ind2[i]*rows2*cols2 : (ind2[i]+1)*rows2*cols2 ]).reshape((rows2, cols2))
    labels2[i] = lbl2[ind2[i]]



new_image=[]
for k in range(len(images)):
	new_image.append(images[k].ravel())


new_image2=[]
for k in range(len(images2)):
	new_image2.append(images2[k].ravel())

#print(new_image[1])
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=1)
neigh.fit(new_image,labels)
print("Done1")
predictions = neigh.predict(new_image2)
print("Done2")
print(predictions[1])