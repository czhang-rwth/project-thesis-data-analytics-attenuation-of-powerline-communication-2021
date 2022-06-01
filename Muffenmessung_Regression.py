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

font_title = {'family': 'Arial',
'weight': 'normal',
'size': 16,
}

font1 = {'family': 'Arial',
'weight': 'normal',
'size': 12,
}

x1 = muffe1_data['Frequency (Hz)'] * (10 ** -6)
y1 = -muffe1_data['Trace 1: Gain: Magnitude (dB)'] + kalibrierung_data['Trace 1: Gain: Magnitude (dB)']
x2 = muffe2_data['Frequency (Hz)'] * (10 ** -6)
y2 = -muffe2_data['Trace 1: Gain: Magnitude (dB)'] + kalibrierung_data['Trace 1: Gain: Magnitude (dB)']

slope1, intercept1, r1, p1, std_err1 = stats.linregress(x1, y1)
slope2, intercept2, r2, p2, std_err2 = stats.linregress(x2, y2)
print('slope1 = ', slope1, ' intercept1 = ', intercept1)
print('slope2 = ', slope2, ' intercept2 = ', intercept2)

y1_regress = [slope1*x + intercept1 for x in x1]
y2_regress = [slope2*x + intercept2 for x in x2]

plt.figure(figsize=(10,6))
plt.style.use('seaborn')
plt.title('Diagramm der Dämpfungen und deren Regression', font_title)
plt.xlabel('Frequenz [MHz]', font1)
plt.ylabel('Dämpfung [dB]', font1)
plt.xticks(fontsize = 12, fontfamily = 'Arial')
plt.yticks(fontsize = 12, fontfamily = 'Arial')
plt.scatter(x1,y1, color = 'lightgreen', label = 'Leerlauf')
plt.scatter(x2,y2, color = 'lightcoral', label = '50 Ohm')
plt.plot(x1, y1_regress, color = 'green', label = 'Leerlauf Regression')
plt.plot(x2,y2_regress, color = 'red', label = '50 Ohm Regression')
plt.legend(prop = font1, loc = 'lower right')
plt.savefig('E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Regression.png', dpi=1000)
plt.show()