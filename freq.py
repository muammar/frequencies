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
# Scaling frequencies
scfreq=[]
for idx,vib in enumerate(frequencies):
    scfreq.append(frequencies[idx]*scalefreq)

#print scfreq

# Different cases for omega values

spectrum=[]
wave=[]

if omega > 0:
    for j in range(wavemax):
        pspectrum=[]
        for i in range(nvib):
            pspectrum.append(scaleint*intensities[i]*omega/(4*(j-frequencies[i])**2+omega**2))
        wave.append(j+1)
        spectrum.append(sum(pspectrum))

else:
    wave[0] = 0.0
    j = 3
    for i in range(nvib):
        wave[j-1]=frequencies[i] - 0.01
        wave[j] = position[i]


"""

C *** Code for Line Spectrum *** (omega .EQ. 0)
      else
        wave(1) = 0.0
        j=3
        do i=1,nvib
            wave(j-1) = position (i) - 0.01
            wave(j)   = position (i)
            spectrum(j)=scaleint*intens(i)
            wave(j+1) = position (i) + 0.01
            j=j+3
        end do
        wave(j-1) = 4000.0
        wavemax = j-1
      end if



C  **** Output directly to file

        open (2,file=jobname(1:nn)//'.prn',
     &    form='FORMATTED',status='unknown')

        do j=1,wavemax
          write(2,'(F8.2,F11.5)')  wave(j),spectrum(j)
        end do

        close(1)
        close(2)


	end

"""
