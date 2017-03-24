from scipy.misc import *
import numpy as np

im=np.load('diff.npy')
imshow(bytescale(im[0,:,:]))
