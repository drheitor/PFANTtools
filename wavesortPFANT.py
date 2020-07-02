#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:50:17 2020

@author: Heitor
"""


import numpy as np 




# N1  15017.995
#9.708 -2.988 4.02717E-30 0 0 1.3145 1 0
# N1  15024.243
#7.947 -4.88 2.540973E-31 0 0 0.4433 1 0



INPUT= 'turbospec.20180901.atoms_PFANT.dat'



ATOMS = np.genfromtxt(INPUT, dtype=str, skip_header=0, unpack=True, delimiter='\n')




# for even index 
n=0
line=[]
wave=[]
loggf=[]
while n < len(ATOMS):    
    if (n % 2) == 0:
        wave.append(float(ATOMS[n][3:]))
        line.append(ATOMS[n])
    if (n % 2) != 0:
        loggf.append(ATOMS[n])
    
    n=n+1


# sort wavelength 
sorted_wave = sorted(wave)




print('Saving... \n')

dat = open(INPUT[:-4]+'_sorted.dat', 'w')


for lamb in sorted_wave:
    
    n=wave.index(lamb)
    if len(line[n])==14:
        dat.write(line[n]+'\n')
    else:
        dat.write(' '+line[n]+'\n')
    dat.write(loggf[n]+'\n')


print('DONE... \n')




























#------------