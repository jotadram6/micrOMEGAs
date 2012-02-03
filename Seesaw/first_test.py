#!usr/bin/env python
from pylab import *
import commands

def OMEGA(shift,MN1): #Relic density calculus
    '''Relic density calculus using micromegas'''
    inputfile=open('data1.par','w')
    inputfile.write('MH0    ')
    inputfile.write('%E' %(MN1*shift))
    inputfile.write('\n')
    inputfile.write('MH    ')
    inputfile.write('140')
    inputfile.write('\n')
    inputfile.write('MA0    ')
    inputfile.write('%E' %(MN1*shift))
    inputfile.write('\n')
    inputfile.write('MH1    ')
    inputfile.write('%E' %(MN1*shift))
    inputfile.write('\n')
    inputfile.write('La2    ')
    inputfile.write('0.5')
    inputfile.write('\n')
    #inputfile.write('LaL    ')
    #inputfile.write('\n')
    #inputfile.close()
    inputfile.write('MN1    ')
    inputfile.write('%E' %(MN1))
    inputfile.write('\n')
    inputfile.write('MN2    ')
    inputfile.write('%E' %(MN1))
    inputfile.write('\n')
    inputfile.write('MN3    ')
    inputfile.write('6000')
    inputfile.write('\n')
    inputfile.write('h11    ')
    inputfile.write('0.0')
    inputfile.write('\n')
    inputfile.write('h21    ')
    inputfile.write('0.1*I')
    inputfile.write('\n')
    inputfile.write('h31    ')
    inputfile.write('0.1*I')
    inputfile.write('\n')
    inputfile.write('h12    ')
    inputfile.write('0.0')
    inputfile.write('\n')
    inputfile.write('h22    ')
    inputfile.write('0.1')
    inputfile.write('\n')
    inputfile.write('h32    ')
    inputfile.write('0.1')
    inputfile.write('\n')
    inputfile.write('h13    ')
    inputfile.write('0.285')
    inputfile.write('\n')
    inputfile.write('h23    ')
    inputfile.write('0.3')
    inputfile.write('\n')
    inputfile.write('h33    ')
    inputfile.write('0.3')
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

if __name__=='__main__':
    gap=array([1.05,1.1,1.15,1.2])
    MN1=linspace(10.,1000.,1000)
    relic=array([zeros_like(MN1),zeros_like(MN1),zeros_like(MN1),zeros_like(MN1)])
    for j in xrange(len(gap)):
        for i in xrange(len(MN1)):
            relic[j][i]=OMEGA(gap[j],MN1[i])
            print relic[j][i]
    np.save('shmidt',relic)
    fig=figure()
    ax1=fig.add_subplot(1,1,1)
    for j in xrange(len(gap)):
        ax1.plot(MN1,relic[j])
    ax1.hlines(0.2,11,1000)
    ax1.hlines(0.08,11,1000)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel(r'$M_{1}$',size='x-large')
    ax1.set_ylabel(r'$\Omega h$',size='x-large')
    fig.savefig('schmidt')
    show()
