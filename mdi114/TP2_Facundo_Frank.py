#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:58:54 2019

@author: frank
"""

import numpy.random as npr
import numpy as np
import matplotlib as plt

#EXO4 Simulation de loi a denxite par la methode de rejet

#EXO4.1 Loi beta
#loi beta de 1 realisation
def loibeta():
    Uk=npr.random()
    Yk=npr.random()
    k=0
    while ( (6*Yk*(1-Yk)) <= (1.5*Uk)):
        Uk=npr.random()
        Yk=npr.random()
        k=k+1
    return Yk
#print('Loi beta(1 realisation,a=2, b=2): X = {0}\n'.format(loibeta()))

def Nloibeta(N):
    vecteur =[]
    for k in range(N):
        vecteur.append(loibeta())
    return vecteur
print('Loi de Rayleigh(N=3 realisations): X = {0}\n'.format(Nloibeta(3)))



#EXO4.2 Loi gamma
def loiexponentielle(lambda1):
    U = npr.random()
    return -(1/lambda1)*np.log(1-U)
#loi gamma de 1 realisation
def loigamma():
    Uk=npr.random()
    Yk=loiexponentielle(2./3)
    k=0
    f_Yk = (2/np.sqrt(np.pi))*np.sqrt(Yk)*np.exp(-Yk)
    teta = (np.power(3,3./2))/(np.sqrt(2*np.pi*np.e))
    g_Yk = (Yk >= 0 and Yk <= 1)
    while ( f_Yk <= (teta*Uk*g_Yk)):
        Uk=npr.random()
        Yk=npr.random()
        k=k+1
    return Yk
#print('Loi gamma(1 realisation,a=2, b=2): X = {0}\n'.format(loigamma()))

def Nloigamma(N):
    vecteur =[]
    for k in range(N):
        vecteur.append(loigamma())
    return vecteur
print('Loi gamma(N=5 realisations): X = {0}\n'.format(Nloibeta(5)))
    

#EXO5 Histogrammes

import scipy
from pylab import*
import pylab as pylab
lamb=1./3
tableau=-1/lamb*log(1-random(10000))
m1=plt.hist(tableau,bins=linspace(0,6/lamb,61),normed=True)
x=linspace(0,6./lamb,61)
y=lamb*exp(-lamb*x)
plot(x,y,color='red')























