import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

kalibrierung_file = 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Kalibrierung_ohne_pi_Muffe1_201.csv'
kalibrierung_data = pd.read_csv(kalibrierung_file, sep=';')
print(kalibrierung_data)

muffe1_file = 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Muffe1_Messung1_ohnepirichtig_201points.csv'
muffe1_data = pd.read_csv(muffe1_file, sep=';')
print(muffe1_data)

muffe2_file = 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Muffe1_50ohm_ohnepirichtig_201points.csv'
muffe2_data = pd.read_csv(muffe2_file, sep=';')
print(muffe2_data)

def Differenz_Plotting():
    font_title = {'family': 'Arial',
    'weight': 'normal',
    'size': 16,
    }

    font1 = {'family': 'Arial',
    'weight': 'normal',
    'size': 12,
    }   

    x = muffe1_data['Frequency (Hz)'] * (10 ** -6)
    y = -muffe1_data['Trace 1: Gain: Magnitude (dB)'] + muffe2_data['Trace 1: Gain: Magnitude (dB)']

    plt.figure(figsize=(10,6))
    plt.style.use('seaborn')
    plt.title('Dämpfungsdifferenzen der Testfälle Leerlauf und mit 50 Ohm', font_title)
    plt.xlabel('Frequenz [MHz]', font1)
    plt.ylabel('Dämpfung [dB]', font1)
    plt.xticks(fontsize = 12, fontfamily = 'Arial')
    plt.yticks(fontsize = 12, fontfamily = 'Arial')
    plt.plot(x,y, color = 'blue')
    plt.savefig('E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Differenz.png', dpi=1000)
    plt.show()

Differenz_Plotting()

#Korrelation Spearman 
muffe1_daempfung = -muffe1_data['Trace 1: Gain: Magnitude (dB)'] + kalibrierung_data['Trace 1: Gain: Magnitude (dB)']
muffe2_daempfung = -muffe2_data['Trace 1: Gain: Magnitude (dB)'] + kalibrierung_data['Trace 1: Gain: Magnitude (dB)']
korr = stats.spearmanr(muffe1_daempfung, muffe2_daempfung)
print(korr)
print(korr[0])

### Regression 
font_title = {'family': 'Arial',
'weight': 'normal',
'size': 16,
}

font1 = {'family': 'Arial',
'weight': 'normal',
'size': 12,
}   

x = muffe1_data['Frequency (Hz)'] * (10 ** -6)
y = -muffe1_data['Trace 1: Gain: Magnitude (dB)'] + muffe2_data['Trace 1: Gain: Magnitude (dB)']

slope, intercept, r, p, std_err = stats.linregress(x, y)
y_regress = [slope*i + intercept for i in x]
print('slope = ', slope, ' intercept = ', intercept)

plt.figure(figsize=(10,6))
plt.style.use('seaborn')
plt.title('Dämpfungsdifferenzen der Testfälle Leerlauf und mit 50 Ohm und deren Regression', font_title)
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')
plt.scatter(x,y, color = 'deepskyblue', label = 'Differenz von Dämpfungen')
plt.plot(x, y_regress, color = 'blue', label = 'Regression der Differenz')
plt.legend(prop = font1, loc = 'lower right')
plt.savefig('E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Differenz und Regression.png', dpi=1000)
plt.show()