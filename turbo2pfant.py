#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:29:08 2020

@author: Heitor
"""


import numpy as np 


# 8.889 -3.967 4.786301E-29 0 0 0.1 1 0


INPUT= 'turbospec.20180901.atomsTEST'


AP_ATOMS = np.genfromtxt(INPUT, dtype=str, skip_header=0, unpack=True, delimiter='\n')




Fe_ATOMS=[]
lenn=len(AP_ATOMS[2])

# reading apogee
for line in AP_ATOMS:
    if len(line) > lenn-10:
        Fe_ATOMS.append(line)



lamb=[]
xiex=[]
esp=[]
ion=[]
loggf=[]

n = 0
       
while n < len(Fe_ATOMS):
    
    lamb.append(Fe_ATOMS[n][0:9])
    
    xiex.append(Fe_ATOMS[n][10:17])
    loggf.append(Fe_ATOMS[n][17:24])

    esp.append(Fe_ATOMS[n][69:71])
    ion.append(Fe_ATOMS[n][72:75])   
    
    n=n+1
    
    
#CH='1.071519E-33'
CH='1.0E-30'
#LA1  16037.365
#7.815 -1.177 4.02717E-30 0 0 0.1 1 0


print('Saving... \n')

dat = open(INPUT[:-4]+'_PFANT.dat', 'w')


TO_REMOVE = "H, He, F, Ne, P, Ar, Cl, As, Br, Kr, Xe"


#Ni2, Nb1,2, Tc1, TH1, CL1,2, P1,2,PD2,RU1

#C1 --> espaço C1
#C1, C2, N1, N2, O1, O2, Y1, Y2, S1, S2


m=0
while m < len(esp):
    
    if esp[m].replace(" ", "") != 'RU' and esp[m].replace(" ", "") != 'PD' and esp[m].replace(" ", "") != 'P' and esp[m].replace(" ", "") != 'CL' and esp[m].replace(" ", "") != 'TH' and esp[m].replace(" ", "") != 'TC' and esp[m].replace(" ", "") != 'NB' and esp[m].replace(" ", "") != 'NI' and esp[m].replace(" ", "") != 'H' and esp[m].replace(" ", "") != 'HE' and ion[m] != 'III' and esp[m].replace(" ", "") != 'F' and esp[m].replace(" ", "") != 'NE' and esp[m].replace(" ", "") != 'AR' and esp[m].replace(" ", "") != 'AR' and esp[m].replace(" ", "") != 'KR' and esp[m].replace(" ", "") != 'XE':
        
        if ion[m] == ' I ':
            if len(esp[m].replace(" ", ""))==2:
                dat.write(esp[m].replace(" ", "") +'1'+'  '+lamb[m]+'\n')
            else:
                dat.write(' '+esp[m].replace(" ", "") +'1'+'  '+lamb[m]+'\n')
       
        if ion[m] == ' II':
            if len(esp[m].replace(" ", ""))==2:
                dat.write(esp[m].replace(" ", "") +'2'+'  '+lamb[m]+'\n')
            else:
                dat.write(' '+esp[m].replace(" ", "") +'2'+'  '+lamb[m]+'\n')
    #if ion[m] == 'III':
    #    dat.write(esp[m].replace(" ", "") +'3'+'  '+lamb[m]+'\n')
       
        dat.write(xiex[m].replace(" ", "")+' '+loggf[m]+' '+CH+' 0 0 0.1 1 0'+'\n')

    m=m+1
print('DONE... \n')







































#-------------