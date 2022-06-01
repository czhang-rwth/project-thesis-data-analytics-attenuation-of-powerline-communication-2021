import os
from numpy import isnan
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame
from pandas.core.series import Series
import math

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





############################################### multi plotting #################################################################

kalibrieren10m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\10m\Kalibrierung\\New measurement_2021-12-02T14_15_10.csv'
kalibrieren10m = pd.read_csv(kalibrieren10m_path)
realkalibirieren10m = kalibrieren10m.drop(range(23))
realkalibirieren10m = realkalibirieren10m['---Measurement settings---'].str.split(';', expand=True)
realkalibirieren10m.index = Series(range(201))

kalibrieren15m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m\\Kalibrierung\\Kalibrierung_richtig.csv'
kalibrieren15m = pd.read_csv(kalibrieren15m_path)
realkalibirieren15m = kalibrieren15m.drop(range(23))
realkalibirieren15m = realkalibirieren15m['---Measurement settings---'].str.split(';', expand=True)
realkalibirieren15m.index = Series(range(201))

kalibrieren30m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Kalibrierung\\New measurement_2021-12-01T16_38_46.xlsx'
kalibrieren30m = pd.read_excel(kalibrieren30m_path)
realkalibirieren30m = kalibrieren30m.drop(range(29))
realkalibirieren30m.index = Series(range(201))

fig = plt.figure()
ax1 = plt.axes(projection = '3d')

temperature_index = 0
for tempstring in os.listdir(file10m):
    tempstring = file10m + tempstring
    print(tempstring)
    csvfile = pd.read_csv(tempstring)

    if csvfile.columns == ['---Measurement settings---']:
        realcsvfile = csvfile.drop(range(23))
        realcsvfile = realcsvfile['---Measurement settings---'].str.split(';', expand=True)
        realcsvfile.index = Series(range(201))
        temp_achse_10m = temperature10m[temperature_index]
        freq_achse_10m = realcsvfile[0].astype('float') * (10** -6)
        dampf_achse_10m = -realcsvfile[4].astype('float') + realkalibirieren10m[4].astype('float')
    else:
        realcsvfile = pd.read_csv(tempstring, sep=';')
        temp_achse_10m = temperature10m[temperature_index] 
        freq_achse_10m = realcsvfile['Frequency (Hz)'].astype('float')* (10** -6)
        dampf_achse_10m = -realcsvfile['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren10m[4].astype('float')
  
    ax1.plot(freq_achse_10m, dampf_achse_10m, temp_achse_10m, color = 'blue', label = '10m')
    temperature_index = temperature_index + 1

temperature_index = 0
for tempstring in os.listdir(file15m):
    tempstring = file15m + tempstring
    print(tempstring)
    csvfile = pd.read_csv(tempstring)

    if csvfile.columns == ['---Measurement settings---']:
        realcsvfile = csvfile.drop(range(23))
        realcsvfile = realcsvfile['---Measurement settings---'].str.split(';', expand=True)
        realcsvfile.index = Series(range(201))
        temp_achse_15m = temperature15m[temperature_index]
        freq_achse_15m = realcsvfile[0].astype('float') * (10** -6)
        dampf_achse_15m = -realcsvfile[4].astype('float') + realkalibirieren15m[4].astype('float')
    else:
        realcsvfile = pd.read_csv(tempstring, sep=';')
        temp_achse_15m = temperature15m[temperature_index] 
        freq_achse_15m = realcsvfile['Frequency (Hz)'].astype('float')* (10** -6)
        dampf_achse_15m = -realcsvfile['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren15m[4].astype('float')
  
    ax1.plot(freq_achse_15m, dampf_achse_15m, temp_achse_15m, color='green', label = '15m')
    temperature_index = temperature_index + 1

temperature_index = 0
for tempstring in os.listdir(file30m):
    tempstring = file30m + tempstring
    print(tempstring)
    csvfile = pd.read_excel(tempstring)
    realcsvfile = csvfile.drop(range(29))   
    realcsvfile.index = Series(range(201))

    temp_achse_30m = temperature30m[temperature_index]
    freq_achse_30m = realcsvfile['---Measurement settings---'].astype('float') * (10** -6)
    dampf_achse_30m = -realcsvfile['Unnamed: 4'].astype('float') + realkalibirieren30m['Unnamed: 4'].astype('float')

    ax1.plot(freq_achse_30m, dampf_achse_30m, temp_achse_30m, color='red', label='30m')
    temperature_index = temperature_index + 1

ax1.set_xlabel('Frequenz [MHz]')
ax1.set_ylabel('Dämpfung [dB]')
ax1.set_zlabel('Temperatur [°C]')

plt.title('Diagramm der Dämpfungen in Abhängigkeit von Frequenzen, 10m, 15m, 30m')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\temperaturabhängige Dämpfung 10+15+30.png', dpi = 1500)