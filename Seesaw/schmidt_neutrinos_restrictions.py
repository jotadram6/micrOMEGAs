#!usr/bin/env python
from pylab import *
import commands
import schmidt_spread

def Ifn(x):
    '''Loop function'''
    IFN=(x/(1-x))*(1-(x*log(x)/(1-x)))
    return IFN

def Lambda(Mi,Meta):
    '''Lambda definition for each right neutrino'''
    deltaMsol=2.43E-21
    h32=0.3**2
    Lambda3=deltaMsol/(3*h32)
    M3=6000
    vev=246
    lambda5=(Lambda3*M3*(4*pi)**2)/(2.*Ifn((M3/Meta)**2)*vev**2)
    return ((2.*lambda5*vev**2)/(Mi*(4*pi)**2))*Ifn((Mi/Meta)**2)

def h1func(psi,M1,Meta):
    deltaMatm=7.59E-23
    Lambda1=Lambda(M1,Meta)
    #print (deltaMatm**2/(4*Lambda1**2)+4.*psi**2)
    if (deltaMatm**2/(4*Lambda1**2)+4.*psi**2)>=0:
        h1_plus=((deltaMatm/(2.*Lambda1)+sqrt((deltaMatm**2/(4*Lambda1**2)+4.*psi**2))))/2
        h1_minus=((deltaMatm/(2.*Lambda1)-sqrt((deltaMatm**2/(4*Lambda1**2)+4.*psi**2))))/2
        if h1_plus>=0:
            return sqrt(h1_plus)
        else:
            print 'Error 1: Negative solution'
            pass
    else:
        print 'Error 2: Imaginary solution'
        pass

if  __name__=='__main__':
    gap=array([2.0,10.,15.,20.])
    MN1=linspace(5.,6000.,6000)
    relic=array([zeros_like(MN1),zeros_like(MN1),zeros_like(MN1),zeros_like(MN1)])
    psi=1.0
    ForSaving=[]
    #h1=h2=0.1
    #for j in xrange(len(gap)):
    #    for i in xrange(len(MN1)):
    #        relic[j][i]=schmidt.OMEGA(gap[j],MN1[i])
    #        print relic[j][i]
    #        ForSaving.append([MN1[i],0.01,relic[j][i],gap[j]])
    #np.save('schmidt_n_restrictions1',np.array(ForSaving))
    #h1=0.8,h2=0.125
    h1=0; h2=0
    for j in xrange(len(gap)):
        for i in xrange(len(MN1)):
            h1=h1func(psi,MN1[i],gap[j]*MN1[i])
            h2=psi/h1
            print h1,h2, h1*h2
            relic[j][i]=schmidt_spread.OMEGA_minimal_complex(gap[j],MN1[i],h1,h2)
            #print relic[j][i]
            ForSaving.append([MN1[i],psi,relic[j][i],gap[j]])
    np.save('schmidt_n_restrictions_1.0',np.array(ForSaving))
   
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
    fig.savefig('schmidt_n_restrictions_1')
    show()
