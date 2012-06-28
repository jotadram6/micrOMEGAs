#!/usr/bin/env python
from pylab import *
#import commands
import DM_tasks
import sys

if  __name__=='__main__':
    La3=linspace(-20,20,40)
    Mmin=210
    Mmax=6000
    Mpts=100
    MT0=linspace(Mmin,Mmax,Mpts)
    ForSaving=[]
    kk=0
    for j in xrange(len(La3)):
        for i in xrange(len(MT0)):
            relic=DM_tasks.OMEGA(La3[j],MT0[i],MT0[i]+166)
            if kk%10==0: print relic
            ForSaving.append([MT0[i],MT0[i]+166,La3[j],relic])
            kk=kk+1
            #if kk==10:
            #    sys.exit()

    np.save('itm_%d' %Mmin,np.array(ForSaving))
    #Plotting
    X=np.array(ForSaving)
    Om=0.1109
    DOm=0.0056
    nDOm=3
    XX=X[np.logical_and(X[:,3]>Om-nDOm*DOm,X[:,3]<Om+nDOm*DOm)]
    XLL=X[X[:,3]>Om+nDOm*DOm]
    Xll=X[X[:,3]<Om-nDOm*DOm]
    fig=figure()
    ax1=fig.add_subplot(1,1,1)
    #plotting=['rH','bv','k^','go']
    ax1.plot(XX[:,0],log(abs(XX[:,2])),'g^')
    ax1.plot(XLL[:,0],log(abs(XLL[:,2])),'r^')
    ax1.plot(Xll[:,0],log(abs(Xll[:,2])),'b^')
    #for h in xrange(len(gap)):
        #ax1.plot(XX[XX[:,3]==gap[h],plotting[h]])
    #ax1.hlines(0.2,11,1000)
    #ax1.hlines(0.08,11,1000)
    #ax1.set_xscale('log')
    #ax1.set_yscale('log')
    ax1.set_xlabel(r'$M_{T_{0}}$',size='x-large')
    ax1.set_ylabel(r'$log(|\lambda_{3}|)$',size='x-large')
    fig.savefig('First_Spread')
    #show()
    print 'Finish'
