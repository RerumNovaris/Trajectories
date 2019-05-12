# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 15:19:39 2016

@author: MW
"""

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import time

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
plt.ion()
plt.show()  #plt.show(block=True)

verts = [
    (0, 0), #I'm just assuming two sets of points here. I actually intend to put variables here which I can update in real time.
    (27, 0)
    ]

codes = [Path.MOVETO,
         Path.LINETO]  

path = Path(verts, codes)

#fig = plt.figure()
#ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='white', lw=2)
ax.add_patch(patch)
#ax.set_xlim(-100,100)
#ax.set_ylim(-100,100)
plt.draw()
plt.pause(1)
#time.sleep(1)