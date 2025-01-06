import numpy as np


import os

loc = os.path.dirname(os.path.realpath(__file__))

class Filt:
    def __init__(self, name= None, wave= None, throughput= None):
        self.name = name
        self.wave = wave
        self.throughput = throughput

file = 'filters/filters.txt'
file_path=os.path.join(loc,file)

with open(file_path, 'r') as fp:
    lines = fp.readlines()

filters : list[Filt] = []
wave : list[float] = []
through : list[float] = []

for line in lines:
    if 'lambda_c' in line:
        header = ' '.join(line.split()[1:])
        if len(wave) > 0:
            new_filter = Filt(name= header, wave=np.asarray(wave, dtype= float),throughput= np.asarray(through, dtype= float))
            filters.append(new_filter)

        # Clear the lists?
        wave = []
        through = []
    else:
        lspl = np.asarray(line.split(), float)
        wave.append(lspl[1])
        through.append(lspl[2])

new_filter = Filt(name=header,wave=np.asarray(wave, float), throughput=np.asarray(through, float))

filters.append(new_filter)
print(f'Imported filters from {file}')
