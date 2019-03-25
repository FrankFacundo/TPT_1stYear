#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 08:43:15 2019

@author: frank
"""


import numpy as np
import numpy.random as npr
import scipy
import pylab as pylab

from pylab import *
from random import *
from math import *



#1 Méthodes de simulation d'une loi normale


#1.2 Méthode de Box-Muller
def LoiNormal_box_muller():
    U1 = npr.random()
    U2 = npr.random()
    X1 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)
    #X2 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    return X1
#print('Loi normal central reduite avec méthode de box-muller (1 realisation,m=0,alpha carré=1): X = {0}\n'.format(LoiNormal_box_muller()))

#Loi normal méthode de Box-Muller de N realisations
def N_LoiNormal_box_muller(N):
    vecteur = []
    for k in range(N):
        vecteur.append(LoiNormal_box_muller())
    return vecteur
#print('Loi normal central reduite(N=3 realisations,m=0,alpha carre=1): X = {0}\n'.format(N_LoiNormal_box_muller(5)))

#Histogramme loi normale
def histogramme_loi_normale():
    h1=pylab.hist(N_box_muller(10000),bins=linspace(-5,5,500),normed=True)
    x=linspace(-5,5,500)
    y=(1/np.sqrt(2*np.pi))*np.exp(-np.power(x,2)/2)
    plot(x,y,color='black')
#histogramme_loi_normale()

#1.3 Méthode de rejet via la loi de laplace (loi normale)

#1.3.1 
#loi de Laplace
def loiLaplace():
    U = npr.random()
    X = -np.sign(U-0.5)*np.log(1-2*np.abs(U-0.5))
    return X

#print('Loi de Laplace: X = {0}\n'.format(loiLaplace()))

#Loi normale avec loi de Laplace
    
def loiNormale_Laplace():
    Uk=npr.random()
    Yk=loiLaplace()
    k=0
    f_Yk = (1/np.sqrt(2*np.pi))*np.exp(-np.power(Yk,2)/2)
    teta = np.sqrt((2*np.e)/np.pi)
    g_Yk = 0.5*np.exp(-np.abs(Yk))
    while ( f_Yk <= (teta*Uk*g_Yk)):
        Uk=npr.random()
        Yk=loiLaplace()
        k=k+1
    return Yk
#print('Loi normal central reduite(N=3 realisations,m=0,alpha carre=1): X = {0}\n'.format(loiNormale_Laplace())) 

#Loi normal avec Laplace de N realisations
def N_loiNormale_Laplace(N):
    vecteur = []
    for k in range(N):
        vecteur.append(loiNormale_Laplace())
    return vecteur
#print('Loi normal central reduite(N=3 realisations,m=0,alpha carre=1): X = {0}\n'.format(N_loiNormale_Laplace(3)))

#Histogramme loi normale avec Laplace
def histogramme_loi_normale_laplace():
    h1=pylab.hist(N_loiNormale_Laplace(1000),bins=linspace(-5,5,500),normed=True)
    x=linspace(-5,5,500)
    y=(1/np.sqrt(2*np.pi))*np.exp(-np.power(x,2)/2)
    plot(x,y,color='black')
#histogramme_loi_normale_laplace()


#2 Lois dérivées de la loi normale


#2.1 Loi du Khi-deux
def KhiDeux(n):
    Xn = 0
    for i in range (n):
        Xn = Xn + np.power(LoiNormal_box_muller(),2)
    return Xn 

def N_KhiDeux(N,n):
    vecteur = []
    for k in range(N):
        vecteur.append(KhiDeux(n))
    return vecteur

def histogramme_KhiDeux(N,n):
    h1=pylab.hist(N_KhiDeux(N,n),bins=linspace(0,30,1000),normed=True)
    x=linspace(0,30,500)
    y=((np.power(x, (n/2.)-1 ) ) / (math.gamma(n/2.) * np.power(2,n/2.)) * np.exp(-x/2.))
    plot(x,y,color='black')
    
#histogramme_KhiDeux(10000,5)


#2.2 Loi Student
def loiStudent(n):
    Xn = LoiNormal_box_muller()/(sqrt(KhiDeux(n)/n))
    return Xn 

def N_loiStudent(N,n):
    vecteur = []
    for k in range(N):
        vecteur.append(loiStudent(n))
    return vecteur

def histogramme_loiStudent(N,n):
    h1=pylab.hist(N_loiStudent(N,n),bins=linspace(-10,10,1000),normed=True)
    x=linspace(-10,10,1000)
    a = (math.gamma((n+1)/2.)/(math.gamma(n/2.)*np.sqrt(pi*n))) 
    m = 1+(np.power(x,2)/n)
    b = (1/(np.power(m,(n+1)/2)))
    y = ( a * b )
    plot(x,y,color='black')
    
#histogramme_loiStudent(10000,5)

#2.3 Resultat remarquable

def loiNormale(m,sigma2):
    X = (np.sqrt(sigma2) * LoiNormal_box_muller() ) + m
    return X
def N_loiNormale(N,m,sigma2):
    vecteur = []
    for k in range(N):
        vecteur.append(loiNormale(m,sigma2))
    return vecteur
def histogramme_loiNormale(N,m,sigma2):
    h1=pylab.hist(N_loiNormale(N,m,sigma2),bins=linspace(-10,10,1000),normed=True)
    x=linspace(-10,10,1000)
    y =(1/(np.sqrt(2*np.pi)*np.sqrt(sigma2)))*np.exp(-np.power(x-m,2)/(2*sigma2))
    plot(x,y,color='black')
    
#histogramme_loiNormale(10000,3,2)


#3 Approximation d'une loi normale
#3.2 Lien de la loi normale avec la loi binomiale
    
def loibinomiale(n,p):
    U = rand(1, n)
    Y = (U < p)
    X = sum(Y)
    return X

#print loibinomiale(20,0.5)
def suiteBinomiale(n,p):
    X = (loibinomiale(n,p)-(n*p)) / (np.sqrt(n*p*(1.-p)))
    return X
#print suiteBinomiale(20,0.5)
def N_suiteBinomiale(N,n,p):
    vecteur = []
    for k in range(N):
        vecteur.append(suiteBinomiale(n,p))
    return vecteur
#print N_suiteBinomiale(100,20,0.5)
def histogramme_suiteBinomiale(N,n,p):
    
    h1=pylab.hist(N_suiteBinomiale(N,n,p),bins=linspace(-5,5,1000),normed=True)
    x=linspace(-5,5,1000)
    y = (1/np.sqrt(2*np.pi))*np.exp(-np.power(x,2)/2)
    plot(x,y,color='black')
    
#histogramme_suiteBinomiale(100000,100000,0.5) 


#3.3 Lien de la loi de Poisson
def loiexponentielle(lambda1):
    U = npr.random()
    return -(1./lambda1)*np.log(1-U)

def Nloiexponentielle(lambda1,N):
    vecteur = []
    for k in range(N):
        vecteur.append(loiexponentielle(lambda1))
    return vecteur

def Poisson_geom(lambda_):
    X = 0
    vecteur = Nloiexponentielle(lambda_,1000)
    Sk = 0
    for k in range(1000):
        for i in range (k):
            Sk = Sk + vecteur[i]
        if( Sk <= 1.) :
            X+=1
    return X

def N_Poisson_geom(N,lambda_):
    vecteur = []
    for k in range(N):
        vecteur.append(Poisson_geom(lambda_))
    return vecteur
    
#print(N_Poisson_geom(20,5)

def histogramme_Poisson_geom(N,lambda_):
    
    h1=pylab.hist(N_Poisson_geom(N,lambda_),bins=linspace(0,20,1000),normed=True)
    x=linspace(0,20,1000)
    y = (np.power(lambda_,x) * np.exp(-lambda_)) / (math.factorial(x))
    plot(x,y,color='black')

#istogramme_Poisson_geom(1000, 200)


#3.4 Lien de la loi de Student

#3.5 Théorème Central-Limite

def Yn(n,lambda_):
    Sn = (1./n)*sum(Nloiexponentielle(lambda_,n))
    esperance = 1/lambda_
    variance = (1/math.pow(lambda_,2))
    return (math.sqrt(n)/math.sqrt(variance))*(Sn-esperance)
#test = Yn(1000,1)
#print(test)

def N_Yn(N,n,lambda_):
    vecteur = []
    for k in range (N):
        vecteur.append(Yn(n,lambda_))
    return vecteur

def histogramme_Yn(N,n,lambda_):
    
    h1=pylab.hist(N_Yn(N,n,lambda_),bins=linspace(-5,5,1000),normed=True)
    x=linspace(-5,5,1000)
    y = lambda_ * np.exp(-lambda_*x)
    #plot(x,y,color='black')

histogramme_Yn(10000,1000, 1)