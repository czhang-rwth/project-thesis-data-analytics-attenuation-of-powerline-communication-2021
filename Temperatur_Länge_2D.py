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

################################################### 30m - 15m ##########################################################################
file30m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Temperatur\\'
file15m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m\\Temperatur\\'

kalibrieren15m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m\\Kalibrierung\\Kalibrierung_richtig.csv'
kalibrieren15m = pd.read_csv(kalibrieren15m_path)
realkalibirieren15m = kalibrieren15m.drop(range(23))
realkalibirieren15m = realkalibirieren15m['---Measurement settings---'].str.split(';', expand=True)
realkalibirieren15m.index = Series(range(201))

kalibrieren30m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Kalibrierung\\New measurement_2021-12-01T16_38_46.xlsx'
kalibrieren30m = pd.read_excel(kalibrieren30m_path)
realkalibirieren30m = kalibrieren30m.drop(range(29))
realkalibirieren30m.index = Series(range(201))

font_title = {'family': 'Arial',
'weight': 'normal',
'size': 16,
}

font1 = {'family': 'Arial',
'weight': 'normal',
'size': 12,
}   

plt.style.use('seaborn')
plt.figure(figsize=(10,6))
plt.title('Dämpfung(30m) - Dämpfung(15m)')
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')

temperature = []
for temp30_file in os.listdir(file30m):
    temp30 = list(temp30_file)
    temp30.remove('.')
    temp30.remove('x')
    temp30.remove('l')
    temp30.remove('s')
    temp30.remove('x')
    temp30[-2] = '.'
    temp30 = float(''.join(temp30))
    for temp15_file in os.listdir(file15m):
        temp15 = list(temp15_file)
        temp15.remove('.')
        temp15.remove('c')
        temp15.remove('s')
        temp15.remove('v')
        temp15[-2] = '.'
        temp15 = float(''.join(temp15))
        if temp15 == temp30:
            print(temp30)
            temperature.append(temp15)
            temp15_file = file15m + temp15_file
            csvfile15 = pd.read_csv(temp15_file)
            if csvfile15.columns == ['---Measurement settings---']:
                realcsvfile15 = csvfile15.drop(range(23))
                realcsvfile15 = realcsvfile15['---Measurement settings---'].str.split(';', expand=True)
                realcsvfile15.index = Series(range(201))
                freq15 = realcsvfile15[0].astype('float') * (10** -6)
                dampf15 = -realcsvfile15[4].astype('float') + realkalibirieren15m[4].astype('float')
            else:
                realcsvfile15 = pd.read_csv(temp15_file, sep=';') 
                freq15 = realcsvfile15['Frequency (Hz)'].astype('float')* (10** -6)
                dampf15 = -realcsvfile15['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren15m[4].astype('float')
            
            temp30_file = file30m + temp30_file
            csvfile30 = pd.read_excel(temp30_file)
            realcsvfile30 = csvfile30.drop(range(29))   
            realcsvfile30.index = Series(range(201))
            freq30 = realcsvfile30['---Measurement settings---'].astype('float') * (10** -6)
            dampf30 = -realcsvfile30['Unnamed: 4'].astype('float') + realkalibirieren30m['Unnamed: 4'].astype('float')

            dampf_achse = dampf30 - dampf15
            plt.plot(freq15, dampf_achse, lw = 0.2)


plt.title('Dämpfung(30m) - Dämpfung(15m)')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m-15m 2D.png', dpi = 1500)
################################################### 30m - 15m ##########################################################################





################################################### 30m - 10m ##########################################################################
file30m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Temperatur\\'
file10m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\10m\\Temperatur\\'

kalibrieren10m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\10m\Kalibrierung\\New measurement_2021-12-02T14_15_10.csv'
kalibrieren10m = pd.read_csv(kalibrieren10m_path)
realkalibirieren10m = kalibrieren10m.drop(range(23))
realkalibirieren10m = realkalibirieren10m['---Measurement settings---'].str.split(';', expand=True)
realkalibirieren10m.index = Series(range(201))

kalibrieren30m_path = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m\\Kalibrierung\\New measurement_2021-12-01T16_38_46.xlsx'
kalibrieren30m = pd.read_excel(kalibrieren30m_path)
realkalibirieren30m = kalibrieren30m.drop(range(29))
realkalibirieren30m.index = Series(range(201))

font_title = {'family': 'Arial',
'weight': 'normal',
'size': 16,
}

font1 = {'family': 'Arial',
'weight': 'normal',
'size': 12,
}   

plt.style.use('seaborn')
plt.figure(figsize=(10,6))
plt.title('Dämpfung(30m) - Dämpfung(10m)')
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')


temperature = []
for temp30_file in os.listdir(file30m):
    temp30 = list(temp30_file)
    temp30.remove('.')
    temp30.remove('x')
    temp30.remove('l')
    temp30.remove('s')
    temp30.remove('x')
    temp30[-2] = '.'
    temp30 = float(''.join(temp30))
    for temp10_file in os.listdir(file10m):
        temp10 = list(temp10_file)
        temp10.remove('.')
        temp10.remove('c')
        temp10.remove('s')
        temp10.remove('v')
        temp10[-2] = '.'
        temp10 = float(''.join(temp10))
        if temp10 == temp30:
            print(temp30)
            temperature.append(temp10)
            temp10_file = file10m + temp10_file
            csvfile10 = pd.read_csv(temp10_file)
            if csvfile10.columns == ['---Measurement settings---']:
                realcsvfile10 = csvfile10.drop(range(23))
                realcsvfile10 = realcsvfile10['---Measurement settings---'].str.split(';', expand=True)
                realcsvfile10.index = Series(range(201))
                freq10 = realcsvfile10[0].astype('float') * (10** -6)
                dampf10 = -realcsvfile10[4].astype('float') + realkalibirieren10m[4].astype('float')
            else:
                realcsvfile10 = pd.read_csv(temp10_file, sep=';') 
                freq10 = realcsvfile10['Frequency (Hz)'].astype('float')* (10** -6)
                dampf10 = -realcsvfile10['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren10m[4].astype('float')
            
            temp30_file = file30m + temp30_file
            csvfile30 = pd.read_excel(temp30_file)
            realcsvfile30 = csvfile30.drop(range(29))   
            realcsvfile30.index = Series(range(201))
            freq30 = realcsvfile30['---Measurement settings---'].astype('float') * (10** -6)
            dampf30 = -realcsvfile30['Unnamed: 4'].astype('float') + realkalibirieren30m['Unnamed: 4'].astype('float')

            dampf_achse = dampf30 - dampf10
            plt.plot(freq10, dampf_achse, lw=0.2)

plt.title('Dämpfung(30m) - Dämpfung(10m)')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\30m-10m 2D.png', dpi = 1500)
################################################### 30m - 10m ##########################################################################





################################################### 15m - 10m ##########################################################################
file15m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m\\Temperatur\\'
file10m = 'E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\10m\\Temperatur\\'

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

font_title = {'family': 'Arial',
'weight': 'normal',
'size': 16,
}

font1 = {'family': 'Arial',
'weight': 'normal',
'size': 12,
}   

plt.style.use('seaborn')
plt.figure(figsize=(10,6))
plt.title('Dämpfung(15m) - Dämpfung(10m)')
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')


temperature = []
for temp15_file in os.listdir(file15m):
    temp15 = list(temp15_file)
    temp15.remove('.')
    temp15.remove('c')
    temp15.remove('s')
    temp15.remove('v')
    temp15[-2] = '.'
    temp15 = float(''.join(temp15))
    for temp10_file in os.listdir(file10m):
        temp10 = list(temp10_file)
        temp10.remove('.')
        temp10.remove('c')
        temp10.remove('s')
        temp10.remove('v')
        temp10[-2] = '.'
        temp10 = float(''.join(temp10))
        if temp10 == temp15:
            print(temp10)
            temperature.append(temp10)
            temp10_file = file10m + temp10_file
            csvfile10 = pd.read_csv(temp10_file)
            if csvfile10.columns == ['---Measurement settings---']:
                realcsvfile10 = csvfile10.drop(range(23))
                realcsvfile10 = realcsvfile10['---Measurement settings---'].str.split(';', expand=True)
                realcsvfile10.index = Series(range(201))
                freq10 = realcsvfile10[0].astype('float') * (10** -6)
                dampf10 = -realcsvfile10[4].astype('float') + realkalibirieren10m[4].astype('float')
            else:
                realcsvfile10 = pd.read_csv(temp10_file, sep=';') 
                freq10 = realcsvfile10['Frequency (Hz)'].astype('float')* (10** -6)
                dampf10 = -realcsvfile10['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren10m[4].astype('float')
            
            temp15_file = file15m + temp15_file
            csvfile15 = pd.read_csv(temp15_file)
            if csvfile15.columns == ['---Measurement settings---']:
                realcsvfile15 = csvfile15.drop(range(23))
                realcsvfile15 = realcsvfile15['---Measurement settings---'].str.split(';', expand=True)
                realcsvfile15.index = Series(range(201))
                freq15 = realcsvfile15[0].astype('float') * (10** -6)
                dampf15 = -realcsvfile15[4].astype('float') + realkalibirieren15m[4].astype('float')
            else:
                realcsvfile15 = pd.read_csv(temp15_file, sep=';') 
                freq15 = realcsvfile15['Frequency (Hz)'].astype('float')* (10** -6)
                dampf15 = -realcsvfile15['Trace 1: Gain: Magnitude (dB)'].astype('float') + realkalibirieren15m[4].astype('float')

            dampf_achse = dampf15 - dampf10
            plt.plot(freq10, dampf_achse, lw = 0.2)

plt.title('Dämpfung(15m) - Dämpfung(10m)')
plt.savefig('E:\\Projektarbeit\\Data\\Kabelmessung_20211201\\15m-10m 2D.png', dpi = 1500)
################################################### 15m - 10m ##########################################################################