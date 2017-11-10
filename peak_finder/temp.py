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

peak_value = 0
for num in amplitude:
    if num > peak_value and num > 0.1:
        peak_value = num
    else:
        peak_value = peak_value


plt.plot(wavelength, amplitude)
