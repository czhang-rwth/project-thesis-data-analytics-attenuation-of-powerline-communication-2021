import os
from numpy import isnan
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import math
from scipy import stats
from matplotlib.lines import Line2D

#################################################Save all the temperatures as list #####################################################

file30m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Temperatur\\'
file15m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m\\Temperatur\\'
file10m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\10m\\Temperatur\\'
temperature30m, temperature15m, temperature10m = [], [], []

for tempstring in os.listdir(file30m):
    templist = list(tempstring)
    templist.remove('.')
    templist.remove('x')
    templist.remove('l')
    templist.remove('s')
    templist.remove('x')
    templist[-2] = '.'
    temperature30m.append(float(''.join(templist)))

for tempstring in os.listdir(file15m):
    templist = list(tempstring)
    templist.remove('.')
    templist.remove('c')
    templist.remove('s')
    templist.remove('v')
    templist[-2] = '.'
    temperature15m.append(float(''.join(templist)))

for tempstring in os.listdir(file10m):
    templist = list(tempstring)
    templist.remove('.')
    templist.remove('c')
    templist.remove('s')
    templist.remove('v')
    templist[-2] = '.'
    temperature10m.append(float(''.join(templist)))

#################################################Save all the temperatures as list #####################################################





############################################## 15m ##################################################################
kalibrieren15m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m\\Kalibrierung\\Kalibrierung_richtig.csv'
kalibrieren15m = pd.read_csv(kalibrieren15m_path)
realkalibirieren15m = kalibrieren15m.drop(range(23))
realkalibirieren15m = realkalibirieren15m['---Measurement settings---'].str.split(';', expand=True)
realkalibirieren15m.index = Series(range(201))

fig = plt.figure()
ax1 = plt.axes(projection = '3d')

temperature_index = 0
for tempstring in os.listdir(file15m):
    tempstring = file15m + tempstring
    print(tempstring)
    csvfile = pd.read_csv(tempstring)

    if csvfile.columns == ['---Measurement settings---']:
        realcsvfile = csvfile.drop(range(23))
        realcsvfile = realcsvfile['---Measurement settings---'].str.split(';', expand=True)
        realcsvfile.index = Series(range(201))
        temp_achse = temperature15m[temperature_index]
        freq_achse = realcsvfile[0].astype('float') * (10** -6)
        dampf_achse = -realcsvfile[4].astype('float') + realkalibirieren15m[4].astype('float')
    else:
        realcsvfile = pd.read_csv(tempstring, sep=';')
        temp_achse = temperature15m[temperature_index] 
        freq_achse = realcsvfile['Frequency (Hz)'].astype('float')* (10** -6)
        dampf_achse = -realcsvfile['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren15m[4].astype('float')
    
    slope15, intercept15, r15, p15, std_err15 = stats.linregress(freq_achse, dampf_achse)
    y_regress = [slope15*a + intercept15 for a in freq_achse]
    ax1.plot(freq_achse, y_regress, temp_achse)
    temperature_index = temperature_index + 1

ax1.set_xlabel('Frequenz [MHz]')
ax1.set_ylabel('Dämpfung [dB]')
ax1.set_zlabel('Temperatur [°C]')

plt.title('Regression von Dämpfungen, 15m')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\regression von dämpfung 15m 3D.png', dpi = 1500)
############################################## 15m ##################################################################





############################################################ 30m ################################################################
kalibrieren30m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Kalibrierung\\New measurement_2021-12-01T16_38_46.xlsx'
kalibrieren30m = pd.read_excel(kalibrieren30m_path)
realkalibirieren30m = kalibrieren30m.drop(range(29))
realkalibirieren30m.index = Series(range(201))

fig = plt.figure()
ax1 = plt.axes(projection = '3d')

temperature_index = 0
for tempstring in os.listdir(file30m):
    tempstring = file30m + tempstring
    print(tempstring)
    csvfile = pd.read_excel(tempstring)
    realcsvfile = csvfile.drop(range(29))   
    realcsvfile.index = Series(range(201))

    temp_achse = temperature30m[temperature_index]
    freq_achse = realcsvfile['---Measurement settings---'].astype('float') * (10** -6)
    dampf_achse = -realcsvfile['Unnamed: 4'].astype('float') + realkalibirieren30m['Unnamed: 4'].astype('float')

    slope30, intercept30, r30, p30, std_err30 = stats.linregress(freq_achse, dampf_achse)
    y_regress = [slope30*a + intercept30 for a in freq_achse]
    ax1.plot(freq_achse, y_regress, temp_achse)
    temperature_index = temperature_index + 1

ax1.set_xlabel('Frequenz [MHz]')
ax1.set_ylabel('Dämpfung [dB]')
ax1.set_zlabel('Temperatur [°C]')

plt.title('Regression von Dämpfungen, 30m')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\regression von dämpfung 30m 3D.png', dpi = 1500)
############################################################ 30m ################################################################