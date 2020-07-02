#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:40:48 2019

@author: Heitor
"""


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from astropy import units as u
from specutils import Spectrum1D, SpectralRegion
from specutils.analysis import gaussian_sigma_width, gaussian_fwhm, fwhm, fwzi
import pandas as pd

#----------------------------------------------


def main(starname,vm,teff,logg,feh,wlmin,wlmax):
    
    file = open('./main.dat', 'w')

    file.write(starname +'\n')
    file.write('T 0.02 5.0 1.0 0.12 \n')
    file.write(vm +'\n')
    file.write( teff+' '+logg+' '+feh+' 0.08511 1 \n')
    file.write('F 1.0 \n')
    file.write(feh +'\n')
    file.write('\n')
    file.write('flux_'+str(starname)+'\n')
    file.write(wlmin+' '+wlmax+' 10.0')


    print('main.dat updated')
    
#----------------------------------------------
    
    
def abonds():

    abonds = open('./abonds.dat', 'w')    

    abonds.write('  A  6.50 This is the C13 isotope, please leave \n')
    abonds.write(' L6  1.16\n')
    abonds.write(' L7  1.16\n')
    abonds.write(' HE 10.93\n')
    abonds.write(' LI  1.05\n')
    abonds.write(' BE  '+str(1.38+A_BE)+' \n')
    abonds.write('  B  2.70 \n')
    abonds.write('  C  '+str(8.55+A_C)+' \n')
    abonds.write('  N  '+str(7.97+A_N)+' \n')
    abonds.write('  O  '+str(8.77+A_O)+' \n')
    abonds.write('  F  4.56 \n')
    abonds.write(' NE  7.93 \n')
    abonds.write(' NA  '+str(6.19+A_NA)+' MARCS (G2015)\n')
    abonds.write(' MG  '+str(7.55+A_MG)+' MARCS (G2015)\n')
    abonds.write(' AL  '+str(6.40+A_AL)+' MARCS (G2015)\n')
    abonds.write(' SI  '+str(7.45+A_SI)+' MARCS (G2015)\n')
    abonds.write('  P  '+str(5.38+A_P)+' MARCS (G2015)\n')
    abonds.write('  S  '+str(7.06+A_S)+' MARCS (G2015)\n')
    abonds.write(' CL  '+str(5.50+A_CL)+' \n')
    abonds.write(' AR  6.40 \n')
    abonds.write('  K  '+str(5.02+A_K)+' MARCS (G2015)\n')
    abonds.write(' CA  '+str(6.26+A_CA)+' MARCS (G2015)\n')
    abonds.write(' SC  '+str(3.15+A_SC)+' MARCS (G2015)\n')
    abonds.write(' TI  '+str(4.90+A_TI)+' MARCS (G2015)\n')
    abonds.write('  V  '+str(3.96+A_V)+' MARCS (G2015)\n')
    abonds.write(' CR  '+str(5.57+A_CR)+' MARCS (G2015)\n')
    abonds.write(' MN  '+str(5.37+A_MN)+' MARCS (G2015)\n')
    abonds.write(' FE  7.47 3D (G2015)\n')
    abonds.write(' CO  '+str(4.96+A_CO)+' MARCS (G2015)\n')
    abonds.write(' NI  '+str(6.23+A_NI)+' MARCS (G2015)\n')
    abonds.write(' CU  '+str(4.11+A_CU)+' MARCS (G2015)\n')
    abonds.write(' ZN  '+str(4.46+A_ZN)+' MARCS (G2015)\n')
    abonds.write(' GA  2.96 MARCS (G2015)\n')
    abonds.write(' GE  3.51 MARCS (G2015)\n')
    abonds.write(' AS  2.30 from meteorites\n')
    abonds.write(' SE  3.34 from meteorites\n')
    abonds.write(' BR  2.54 from meteorites\n')
    abonds.write(' KR  3.25 Interp. s-process (AGSS09)\n')
    abonds.write(' RB  2.48 MARCS (G2015)\n')
    abonds.write(' SR  2.73 MARCS (G2015)\n')
    abonds.write('  Y  2.14 MARCS (G2015)\n')
    abonds.write(' ZR  2.53 (Zr II) MARCS (G2015)\n')
    abonds.write(' NB  1.47 MARCS (G2015)\n')
    abonds.write(' MO  1.93 MARCS (G2015)\n')
    abonds.write(' RU  1.80 MARCS (G2015)\n')
    abonds.write(' RH  0.95 MARCS (G2015)\n')
    abonds.write(' PD  1.49 MARCS (G2015)\n')
    abonds.write(' AG  0.92 MARCS (G2015)\n')
    abonds.write(' CD  1.73 MARCS (G2015)\n')
    abonds.write(' IN  0.80 Sunspot (V2008)\n')
    abonds.write(' SN  2.04 MARCS (G2015)\n')
    abonds.write(' SB  1.01 from meteorites\n')
    abonds.write(' TE  2.18 from meteorites\n')
    abonds.write('  I  1.55 from meteorites\n')
    abonds.write(' XE  2.24 Interp. s-process (AGSS09)\n')
    abonds.write(' CS  1.08 from meteorites\n')
    abonds.write(' BA  2.18 HM (2.25 for 3D models, 2.10 for MARCS with non-LTE corr.)\n')
    abonds.write(' LA  1.11 3D (G2015)\n')
    abonds.write(' CE  1.58 3D (G2015)\n')
    abonds.write(' PR  0.72 3D (G2015)\n')
    abonds.write(' ND  1.42 3D (G2015)\n')
    abonds.write(' SM  0.95 3D (G2015)\n')
    abonds.write(' EU  0.52 3D (G2015)\n')
    abonds.write(' GD  1.08 3D (G2015)\n')
    abonds.write(' TB  0.31 3D (G2015)\n')
    abonds.write(' DY  1.10 3D (G2015)\n')
    abonds.write(' HO  0.48 3D (G2015)\n')
    abonds.write(' ER  0.93 3D (G2015)\n')
    abonds.write(' TM  0.11 3D (G2015)\n')
    abonds.write(' YB  0.85 3D (G2015)\n')
    abonds.write(' LU  0.10 3D (G2015)\n')
    abonds.write(' HF  0.85 3D (G2015)\n')
    abonds.write(' TA -0.12 from meteorites\n')
    abonds.write('  W  0.83 3D (G2015)\n')
    abonds.write(' RE  0.26 from meteorites\n')
    abonds.write(' OS  1.40 MARCS (G2015)\n')
    abonds.write(' IR  1.38 MARCS (G2015)\n')
    abonds.write(' PT  1.62 from meteorites\n')
    abonds.write(' AU  0.88 MARCS (G2015)\n')
    abonds.write(' HG  1.17 from meteorites\n')
    abonds.write(' TL  0.90 Sunspot (L1972)\n')
    abonds.write(' PB  1.95 MARCS (G2015)\n')
    abonds.write(' BI  0.65 from meteorites\n')
    abonds.write(' TH  0.02 MARCS (G2015)\n')
    abonds.write('  U -0.54 from meteorites   \n')
    abonds.write('1')   
    abonds.write('1')     
    
    print('abonds.dat updated')
       
   
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
    
#INPUT_file='APOGEE-selectedorbit_0.txt'

INPUT_file='input.txt'
    
STARS = np.genfromtxt(INPUT_file, skip_header=1, unpack=True, dtype=str)

data = pd.DataFrame()
#---
#Parametres
#---

data['name'] = STARS[0]
data['vm']   = STARS[1]
data['Teff'] = STARS[2]
data['logg'] = STARS[3]
data['FeH']  = STARS[4].astype(str)

#data['APOGEE_name'] = APOGEE[0]
#data['APOGEE_ID'] = APOGEE[1]
   
#----------------------------------------------
#---------
# initial abonds ( over solar)
#---------
A_BE=0.0
A_C=0.0
A_N=0.0
A_O=0.0
A_NA=0.0
A_MG=0.0
A_AL=0.0
A_SI=0.0
A_P=0.0
A_S=0.0
A_CL=0.0
A_K=0.0
A_CA=0.0
A_SC=0.0
A_TI=0.0
A_V=0.0
A_CR=0.0
A_MN=0.0
A_CO=0.0
A_NI=0.0
A_CU=0.0
A_ZN=0.0
#---------

wlmin='5000'
wlmax='7000'
    
#A_CU
element='CU'
ABONDSlist=[-0.3,0.0,0.3]

#----------------------------------------------

#starname='ap1'
#vm='2.0'
#teff='4500.0'
#logg='2.0'
#feh='-1.20'

# Go to the terminal: link.py and Y

#lockstep


n=0
for N in data['name']:
    a=0
    for A in ABONDSlist:
    # Add elements to vary in lockstep
        A_CU=A

        if str(A)[0]=='-':
            starname=N+'_'+element+'_m'+str(A)[1]+str(A)[3]
        else:
            starname=N+'_'+element+'_'+str(A)[0]+str(A)[2] 
        vm  =data['vm'][n]
        teff=data['Teff'][n]
        logg=data['logg'][n]
        feh =data['FeH'][n]
        main(starname,vm,teff,logg,feh,wlmin,wlmax)       

        abonds()
    
        if float(teff) > 4999:
            os.system("innewmarcs --allow T")
        else:
            os.system("innewmarcs")
        
        os.system("hydro2")
        os.system("pfant")
        os.system("./nulbad.sh")
        a=a+1
    # mv the whole star( flux, main.dat and abonds) to a directorio with its name 
    n=n+1



# to test the output
#os.system('plot-spectra.py flux_'+starname+'.norm.nulbad.0.100 ')

#----------------------------------------------




























    
    
   