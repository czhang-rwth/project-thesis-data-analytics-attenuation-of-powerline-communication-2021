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



font_title = {'family': 'Arial',
'weight': 'normal',
'size': 16,
}

font1 = {'family': 'Arial',
'weight': 'normal',
'size': 12,
}   



########################## 10m ###########################################################
kalibrieren10m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\10m\Kalibrierung\\New measurement_2021-12-02T14_15_10.csv'
kalibrieren10m = pd.read_csv(kalibrieren10m_path)
realkalibirieren10m = kalibrieren10m.drop(range(23))
realkalibirieren10m = realkalibirieren10m['---Measurement settings---'].str.split(';', expand=True)
realkalibirieren10m.index = Series(range(201))

plt.figure(figsize=(10,6))
plt.title('Diagramm der Dämpfungen in Abhängigkeit von Frequenzen, 10m')
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')

temp_color = []
for i in range(len(temperature10m)):
    if temperature10m[i] < 30:
        temp_color.append('blue')
    if temperature10m[i] < 40 and temperature10m[i] >= 30:
        temp_color.append('violet')
    if temperature10m[i] < 50 and temperature10m[i] >= 40:
        temp_color.append('gold')
    if temperature10m[i] < 60 and temperature10m[i] >= 50:
        temp_color.append('red')
    if temperature10m[i] >= 60:
        temp_color.append('maroon')

temp_index = 0
for tempstring in os.listdir(file10m):
    tempstring = file10m + tempstring
    print(tempstring)
    csvfile = pd.read_csv(tempstring)

    if csvfile.columns == ['---Measurement settings---']:
        realcsvfile = csvfile.drop(range(23))
        realcsvfile = realcsvfile['---Measurement settings---'].str.split(';', expand=True)
        realcsvfile.index = Series(range(201))
        x = realcsvfile[0].astype('float') * (10** -6)
        y = -realcsvfile[4].astype('float') + realkalibirieren10m[4].astype('float')
    else:
        realcsvfile = pd.read_csv(tempstring, sep=';')
        x = realcsvfile['Frequency (Hz)'].astype('float')* (10** -6)
        y = -realcsvfile['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren10m[4].astype('float')

    plt.plot(x, y, color = temp_color[temp_index], linewidth = 0.075)
    temp_index += 1

custom_lines = [Line2D([0], [0], color='blue', lw=2),
                Line2D([0], [0], color='violet', lw=2),
                Line2D([0], [0], color='gold', lw=2),
                Line2D([0], [0], color='red', lw=2),
                Line2D([0], [0], color='maroon', lw=2)]
plt.legend(custom_lines, ['T < 30 °C', '30 °C <= T < 40 °C', '40 °C <= T < 50 °C', '50 °C <= T < 60 °C', 'T >= 60 °C'], prop = font1, loc = 'upper right')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\temperaturabhängige Dämpfung 10m 2D.png', dpi = 2000)
########################## 10m ###########################################################





########################## 15m ###########################################################
kalibrieren15m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m\\Kalibrierung\\Kalibrierung_richtig.csv'
kalibrieren15m = pd.read_csv(kalibrieren15m_path)
realkalibirieren15m = kalibrieren15m.drop(range(23))
realkalibirieren15m = realkalibirieren15m['---Measurement settings---'].str.split(';', expand=True)
realkalibirieren15m.index = Series(range(201))

plt.figure(figsize=(10,6))
plt.title('Diagramm der Dämpfungen in Abhängigkeit von Frequenzen, 15m')
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')

temp_color = []
for i in range(len(temperature15m)):
    if temperature15m[i] < 30:
        temp_color.append('blue')
    if temperature15m[i] < 40 and temperature15m[i] >= 30:
        temp_color.append('violet')
    if temperature15m[i] < 50 and temperature15m[i] >= 40:
        temp_color.append('gold')
    if temperature15m[i] < 60 and temperature15m[i] >= 50:
        temp_color.append('red')
    if temperature15m[i] >= 60:
        temp_color.append('maroon')

temp_index = 0
for tempstring in os.listdir(file15m):
    tempstring = file15m + tempstring
    print(tempstring)
    csvfile = pd.read_csv(tempstring)

    if csvfile.columns == ['---Measurement settings---']:
        realcsvfile = csvfile.drop(range(23))
        realcsvfile = realcsvfile['---Measurement settings---'].str.split(';', expand=True)
        realcsvfile.index = Series(range(201))
        x = realcsvfile[0].astype('float') * (10** -6)
        y = -realcsvfile[4].astype('float') + realkalibirieren15m[4].astype('float')
    else:
        realcsvfile = pd.read_csv(tempstring, sep=';')
        x = realcsvfile['Frequency (Hz)'].astype('float')* (10** -6)
        y = -realcsvfile['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren15m[4].astype('float')

    plt.plot(x, y, color = temp_color[temp_index], linewidth = 0.075)
    temp_index += 1

custom_lines = [Line2D([0], [0], color='blue', lw=2),
                Line2D([0], [0], color='violet', lw=2),
                Line2D([0], [0], color='gold', lw=2),
                Line2D([0], [0], color='red', lw=2),
                Line2D([0], [0], color='maroon', lw=2)]
plt.legend(custom_lines, ['T < 30 °C', '30 °C <= T < 40 °C', '40 °C <= T < 50 °C', '50 °C <= T < 60 °C', 'T >= 60 °C'], prop = font1, loc = 'upper right')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\temperaturabhängige Dämpfung 15m 2D.png', dpi = 2000)
########################## 15m ###########################################################





############################################################ 30m ################################################################
kalibrieren30m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Kalibrierung\\New measurement_2021-12-01T16_38_46.xlsx'
kalibrieren30m = pd.read_excel(kalibrieren30m_path)
realkalibirieren30m = kalibrieren30m.drop(range(29))
realkalibirieren30m.index = Series(range(201))

print(kalibrieren30m)
print(realkalibirieren30m)
print(realkalibirieren30m.columns)

plt.figure(figsize=(10,6))
plt.title('Diagramm der Dämpfungen in Abhängigkeit von Frequenzen, 30m')
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')

temp_color = []
for i in range(len(temperature30m)):
    if temperature30m[i] < 30:
        temp_color.append('blue')
    if temperature30m[i] < 40 and temperature30m[i] >= 30:
        temp_color.append('violet')
    if temperature30m[i] < 50 and temperature30m[i] >= 40:
        temp_color.append('gold')
    if temperature30m[i] < 60 and temperature30m[i] >= 50:
        temp_color.append('red')
    if temperature30m[i] >= 60:
        temp_color.append('maroon')


temp_index = 0
for tempstring in os.listdir(file30m):
    tempstring = file30m + tempstring
    print(tempstring)
    csvfile = pd.read_excel(tempstring)
    realcsvfile = csvfile.drop(range(29))   
    realcsvfile.index = Series(range(201))

    x = realcsvfile['---Measurement settings---'].astype('float') * (10** -6)
    y = -realcsvfile['Unnamed: 4'].astype('float') + realkalibirieren30m['Unnamed: 4'].astype('float')

    plt.plot(x, y, color = temp_color[temp_index], linewidth = 0.075)
    temp_index += 1

custom_lines = [Line2D([0], [0], color='blue', lw=2),
                Line2D([0], [0], color='violet', lw=2),
                Line2D([0], [0], color='gold', lw=2),
                Line2D([0], [0], color='red', lw=2),
                Line2D([0], [0], color='maroon', lw=2)]
plt.legend(custom_lines, ['T < 30 °C', '30 °C <= T < 40 °C', '40 °C <= T < 50 °C', '50 °C <= T < 60 °C', 'T >= 60 °C'], prop = font1, loc = 'upper right')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\temperaturabhängige Dämpfung 30m 2D.png', dpi = 2000)
############################################################ 30m ################################################################