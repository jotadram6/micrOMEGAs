#!usr/bin/env python
#from pylab import *
import commands

def OMEGA(La3,MT0,MTc): #Relic density calculus
    '''Relic density calculus using micromegas'''
    inputfile=open('data1.par','w')
    inputfile.write('MT0    ')
    inputfile.write('%E' %(MT0))
    inputfile.write('\n')
    inputfile.write('MH    ')
    inputfile.write('125')
    inputfile.write('\n')
    inputfile.write('MTc    ')
    inputfile.write('%E' %(MTc))
    inputfile.write('\n')
    inputfile.write('La3    ')
    inputfile.write('%E' %(La3))
    inputfile.write('\n')
    inputfile.close()
#calculo de la densidad de reliquia
    a=commands.getoutput('./main data1.par | grep Omega | awk -F"=" \'{print $3}\'')
    if len(a)==8:
        omega=float(a)
    else:
        omega=-1.0
    #print omega
    return omega
