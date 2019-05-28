    #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:35:27 2019

@author: frank
"""

import numpy.random as npr
from pylab import *
from random import *
from math import *
import numpy as np



#EXO1.1
# =============================================================================
# i = 11 / 5
# print(type(i))
# print random()
# print arange(1,10,2) #(init,fin,pas)
# 
# x = 397.0 and 6
# print x
# =============================================================================


#EXO1.2
# =============================================================================
# def firstfunction(x):
#     if x<1 or x>3 :
#         return 0
#     elif x==2:
#         return 2
#     else:
#         return 1
# 
# def secondfunction(n):  #somme des n premieres nombres 
#     somme = 0
#     for k in range (n+1):
#         somme +=k
#     return somme
# 
# def thirdfunction(n):   #somme des n premieres nombres 
#     somme=0
#     k=1
#     while(k<n+1):
#         somme += k
#         k+=1
#     return somme
# 
# print secondfunction(1.5)
# print secondfunction(4)
# print thirdfunction(4)
# =============================================================================

#EXO2 Simulation des lois discretes
#EXO2.1
#loi bernoulli p simulant N realisations
def loibernoulli(p,N):
    lst = []
    for i in range(1,N):    
        U = random()
        #U = rand(1)
        if(U < p):
            X = 1
        else :
            X = 0
        lst.append(X)
    return lst
print('loibernoulli')
print(loibernoulli(0.5,10))



#EXO2.2
#loi binomiale avec param n et p simulant N realisations
def loibinomiale(n,p,N):
    lst = []
    for i in range(N):    
        U = rand(1, n)
        Y = (U < p)
        X = sum(Y)
        lst.append(X)
    return lst
print('loibinomiale')
print(loibinomiale(20,0.5,5))


#EXO2.3
#loi geometrique avec param p simulant N realisations
def loigeometrique(p,N):
    lst = []
    for i in range(N):    
        
        X = 1
        U = random()
        while (U > p):
           X = X + 1; 
           U = rand(1);
        
        lst.append(X)
    return lst
print('loigeometrique')
print(loigeometrique(0.5,5))


#EXO3 Simulation de loi a denxite par la methode d'inversion

#EXO3.1 Loi exponentielle
#loi exponentielle de 1 realisation
def loiexponentielle(lambda1):
    U = npr.random()
    return -(1./lambda1)*np.log(1-U)
#print('Loi exponentielle(1 realisation,λ=0.5): X = {0}\n'.format(loiexponentielle(0.5)))
#loi exponentielle de N realisations
def Nloiexponentielle(lambda1,N):
    vecteur = []
    for k in range(N):
        vecteur.append(loiexponentielle(lambda1))
    return vecteur
print('Loi exponentielle(N=3 realisations,λ=0.5): X = {0}\n'.format(Nloiexponentielle(0.5,3)))


#EXO3.2 Loi de Cauchy
#loi de Cauchy de 1 realisation
def loiCauchy(m,alpha):
    U = npr.random()
    return alpha*np.tan(np.pi*(U-1/2))+m
#print('Loi de Cauchy(1 realisation,m=2,α=0.5): X = {0}\n'.format(loiCauchy(2,0.5)))

#loi de Cauchy de N realisations
def NloiCauchy(m,alpha,N):
    vecteur = []
    for k in range(N):
        vecteur.append(loiCauchy(m,alpha))
    return vecteur
print('Loi de Cauchy(N=3 realisations,m=2,α=0.5): X = {0}\n'.format(NloiCauchy(2,0.5,3)))

#EXO3.3 Loi de Rayleigh
#loi de Rayleigh de 1 realisation
def loiRayleigh():
    U = npr.random()
    return np.sqrt(-2*np.log(1-U))
#print('Loi de Rayleigh(1 realisation): X = {0}\n'.format(loiRayleigh()))
#loi de Rayleigh de N realisations
def NloiRayleigh(N):
    vecteur =[]
    for k in range(N):
        vecteur.append(loiRayleigh())
    return vecteur
print('Loi de Rayleigh(N=3 realisations): X = {0}\n'.format(NloiRayleigh(3)))


