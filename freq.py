#!/usr/bin/env python


import re

output='opt_30.out'

"""
Parameters
"""
scalefreq=1.0
scaleint=1.0
omega=10.0
wavemax=4000


with open(output,'r') as infile:
    frequencies=[]
    for lines in infile:
        if 'Frequencies' in lines:
            preappend=re.findall("\d+.\d+",lines)
            for i in preappend:
                frequencies.append(i)

with open(output,'r') as infile:
    intensities=[]
    for linesi in infile:
        if 'IR Inten' in linesi:
            preappendi=re.findall("\d+.\d+",linesi)
            for j in preappendi:
                intensities.append(j)

frequencies=[float(i) for i in frequencies]
#print frequencies
nvib=len(frequencies)

intensities=[float(i) for i in intensities]
#print intensities
#print len(intensities)

for item in range(nvib):
    print frequencies[item], intensities[item]


exit()
