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


#EXO2.1
# =============================================================================
##loi bernoulli p simulant N realisations
# def loibernoulli(p,N):
#     lst = []
#     for i in range(1,N):    
#         U = random()
#         #U = rand(1)
#         if(U < p):
#             X = 1
#         else :
#             X = 0
#         lst.append(X)
#     return lst
# 
# print(loibernoulli(0.5,10))
# 
# =============================================================================


#EXO2.2
# =============================================================================
# #loi binomiale avec param n et p simulant N realisations
# def loibinomiale(n,p,N):
#     lst = []
#     for i in range(N):    
#         U = rand(1, n)
#         Y = (U < p)
#         X = sum(Y)
#         lst.append(X)
#     return lst
# 
# print(loibinomiale(20,0.5,5))
# 
# =============================================================================

#EXO2.3
# =============================================================================
# #loi geometrique avec param p simulant N realisations
# def loigeometrique(p,N):
#     lst = []
#     for i in range(N):    
#         
#         X = 1
#         U = random()
#         while (U > p):
#            X = X + 1; 
#            U = rand(1);
#         
#         lst.append(X)
#     return lst
# 
# print(loigeometrique(0.5,5))
# =============================================================================

