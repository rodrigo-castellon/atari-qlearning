# coding: utf-8
'''
Required dependencies:
NumPy
Matplotlib
IPython Display
'''

# In[1]:

#get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
rc('animation', html='html5')


# In[2]:

fig = plt.figure()
ims = []


for i in range(10):
    ims.append((plt.pcolor(np.random.random([100,100])),))


# In[3]:

im_ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=3000, blit=True)


# In[4]:

im_ani


# In[5]:

HTML(im_ani.to_html5_video())


# In[6]:

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
im_ani.save('im.mp4', writer=writer)


# In[ ]:




