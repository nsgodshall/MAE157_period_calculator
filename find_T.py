import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

fname = input("Enter the directory of the file with the data: ")
data = np.genfromtxt(fname, delimiter=",")

time = data[:,0][:500]
sensor = data[:,1][:500]

for i in range(len(sensor)):
    if(sensor[i] == 0):
        sensor[i] = 1
    else:
        sensor[i] = 0

peaks, _ = find_peaks(sensor, height = 0.250)

periods = time[peaks][::2]
count = 0
tot = 0
for p in range(len(periods)):
    if(p%2 == 1):
        tot += periods[p] - periods[p-1]
        count += 1
print("{:.4f} seconds".format((tot/count)))