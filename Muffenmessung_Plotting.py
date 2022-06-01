import pandas as pd
import matplotlib.pyplot as plt

kalibrierung_file = 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Kalibrierung_ohne_pi_Muffe1_201.csv'
kalibrierung_data = pd.read_csv(kalibrierung_file, sep=';')
print(kalibrierung_data)

muffe1_file = 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Muffe1_Messung1_ohnepirichtig_201points.csv'
muffe1_data = pd.read_csv(muffe1_file, sep=';')
print(muffe1_data)

muffe2_file = 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Muffe1_50ohm_ohnepirichtig_201points.csv'
muffe2_data = pd.read_csv(muffe2_file, sep=';')
print(muffe2_data)

def singleplotting(data, set_color, file):
    font_title = {'family': 'Arial',
    'weight': 'normal',
    'size': 16,
    }

    font1 = {'family': 'Arial',
    'weight': 'normal',
    'size': 12,
    }

    x = data['Frequency (Hz)'] * (10 ** -6)
    y = -data['Trace 1: Gain: Magnitude (dB)'] + kalibrierung_data['Trace 1: Gain: Magnitude (dB)']

    plt.title('Diagramm der Dämpfungen in Frequenzen', font_title)
    plt.xlabel('Frequenz [MHz]', font1)
    plt.ylabel('Dämpfung [dB]', font1)
    plt.xticks(fontsize = 12, fontfamily = 'Arial')
    plt.yticks(fontsize = 12, fontfamily = 'Arial')
    plt.plot(x,y, color = set_color)
    plt.savefig(file, dpi=1000)
    plt.show()

def multipleplotting():
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

    plt.figure(figsize=(10,6))
    plt.style.use('seaborn')
    plt.title('Diagramm der Dämpfungen in Abhängigkeit von Frequenzen', font_title)
    plt.xlabel('Frequenz [MHz]', font1)
    plt.ylabel('Dämpfung [dB]', font1)
    plt.xticks(fontsize = 12, fontfamily = 'Arial')
    plt.yticks(fontsize = 12, fontfamily = 'Arial')
    plt.plot(x1,y1, color = 'green', label = 'Leerlauf')
    plt.plot(x2,y2, color = 'red', label = '50 Ohm')
    plt.legend(prop = font1, loc = 'lower right')
    plt.savefig('E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Multipleplotting.png', dpi=1000)
    plt.show()

#singleplotting(muffe1_data, 'blue', 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Muffe1_Messung1_ohnepi_201points.png')
#singleplotting(muffe2_data, 'green', 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Muffe1_Messung1_ohnepirichtig_201points.png')
#singleplotting(muffe3_data, 'red', 'E:\Projektarbeit\Data\Muffenmessung_September\Analysierbar\Muffe1_50ohm_ohnepirichtig_201points.png')

multipleplotting()