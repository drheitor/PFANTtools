#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:41:27 2019

@author: Heitor
"""

import numpy as np 
import pandas as pd
  


def pfantel(lista):
    listanew=[]
    
    for i in lista:
        new=i.replace(' ','')
        new=new.replace('a','A')
        new=new.replace('b','B')
        new=new.replace('c','C')
        new=new.replace('d','D')
        new=new.replace('e','E')
        new=new.replace('f','F')
        new=new.replace('g','G')
        new=new.replace('h','H')
        new=new.replace('i','I')
        new=new.replace('j','J')
        new=new.replace('k','K')
        new=new.replace('l','L')
        new=new.replace('m','M')
        new=new.replace('n','N')
        new=new.replace('o','O')
        new=new.replace('p','P')
        new=new.replace('q','Q')
        new=new.replace('r','R')
        new=new.replace('s','S')
        new=new.replace('t','T')
        new=new.replace('u','U')
        new=new.replace('v','V')
        new=new.replace('w','W')
        new=new.replace('x','X')
        new=new.replace('y','Y')
        new=new.replace('z','Z')
        listanew.append(new)
               
    print('\nDONE!\n')
    
    return(listanew)
        
        
    







INPUT='linesHband.txt'


df = pd.read_csv(INPUT)


df.head()


df['Elm'][1] == "'Ni 2'"



mask1 = df['Elm'] == "'OH 1'"
n=0

el=[]
wl=[]
excit=[]
loggf=[]
rad=[]
stark=[]
waals=[]
factor=[]

for i in df['Elm']:
    
    if i != "'OH 1'" and i !="'CO 1'" and i !="'CN 1'" and i != "'CH 1'" and  i != "'H 1'" and  i != "'Ar 1'" and  i != "'Ne 1'"  and  i != "'H 1'" and i != "'OH 2'" and i !="'CO 2'" and i !="'CN 2'" and i != "'CH 2'" and  i != "'H 2'" and  i != "'Ar 2'" and  i != "'Ne 2'"  and  i != "'H 2'"   and i[4]!='3' and i[3]!='3' and i[4]!='4' and i[3]!='4' and i[4]!='5' and i[3]!='5' and i[4]!='6' and i[3]!='6' and i[4]!='7' and i[3]!='7' and i[4]!='8' and i[3]!='8':
        print(df['Elm'][n])
        el.append(df[df.keys()[0]][n])
        wl.append(df[df.keys()[1]][n])
        excit.append(df[df.keys()[2]][n])
        loggf.append(df[df.keys()[3]][n])
        rad.append(df[df.keys()[4]][n])
        stark.append(df[df.keys()[5]][n])
        waals.append(df[df.keys()[6]][n])
        factor.append(df[df.keys()[7]][n])
        print(str(n))
    
    n=n+1



df1 = pd.DataFrame()
df1['El'] = el   
df1['Wlair'] = wl 
df1['Excit'] = excit   
df1['loggf'] = loggf
df1['rad'] = rad
df1['Stark'] = stark
df1['Waals'] = waals 
df1['Factor'] = factor 

names=pfantel(el)

pfil = open('VALD_H.txt', 'w')
pfil.write('%-8s %5s %8s  %9s   %10s   %10s %10s %10s'%('El', 'Wlair', 'Excit', 'loggf', 'rad', 'Stark','Waals','Factor\n'))
n=0

for i in el:
    ell=names[n]
    wll=wl[n]
    excitl=excit[n]
    loggfl=loggf[n]
    radl=rad[n]
    starkl=stark[n]
    waalsl=waals[n]
    factorl=factor[n]
        
    pfil.write('%6s %7.4f %6.3f %6.3f %6.3f %6.3f %6.3f %6.3f \n'%(ell, wll, excitl, loggfl, radl, starkl, waalsl, factorl))     
    n=n+1
        

np.savetxt(r'./valdH.txt', df1.values, fmt='%s')
df1.to_csv(r'./valdH.csv', sep=',', mode='a')   



pfantfile = open('atoms.dat', 'w')
n=0
for i in names:
    name=i
    if i == "'C21'":
        name="'C2'"

    wlp=wl[n]
    pfantfile.write('%5s %10.3f\n'%(name, wlp))
    excitp=excit[n]
    loggfp=loggf[n]   
    pfantfile.write('%7.3f %6.3f'%(excitp, loggfp))
    pfantfile.write(' 0.3E-30 0.0E+00 0.0E+00 0.5 1.0 0\n')
    
    n=n+1



 
#df.keys()

#df.keys()[1]


    
    
    