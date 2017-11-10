# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.lvm')

wavelength = data[:,1]
amplitude = data[:,2]

noise = np.random.rand(300)
amplitude = amplitude+noise/10

peak_value = np.zeros([10])
n = 0
for i in range(len(amplitude)-1):
    if i == 0:
        if amplitude[0]>0 and amplitude[i+1] <amplitude[i] and amplitude[0]>0.15:
            peak_value[n] = amplitude[i]
            n+=1
        else:
            pass
    else:
        if amplitude[i]>amplitude[i-1] and amplitude[i] > amplitude[i+1] and amplitude[i]>0.15:
            peak_value[n] = amplitude[i]
            n+=1
        else:
            pass


#plt.plot(wavelength, amplitude)
#plt.plot(data[:,1],data[:,2])
