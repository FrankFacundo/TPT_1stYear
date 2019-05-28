# -*- coding: utf-8 -*-

"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy.random as npr
from pylab import*
from random import*
from math import*
import numpy as np


"**************************TP1************************"

"PREMIERE PARTIE DU TP1"
#Application1

a=4
b=2
print(a+b)
print(a-b)
print (a/b)
print(a//b)
print(a%b)
print(np.pi)
print(a<b)
print (a>b)
print(a==b)
print(a!=b)
print(type(a))
print(random())
print(arange(3))
print(linspace(1,15,15))

c=True
d=False

print(c and d)
print(c or d)

#Application2

def firstfunction(x): #Fonction qui envoie 0 lorsque x<1 ou x>3, envoie 2 lorsque x=2 et dans les autres cas elle envoie 1
    if x<1 or x>3:
        return 0
    elif x==2:
        return 2
    else:
        return 1
        
def secondfunction(n): #Fonction qui calcule la somme de 'n' premiers nombres somme=0+1+2+3+....+n
    somme=0
    for k in range(n+1):
            somme+=k
    return somme

def thirdfunction(n): #Fonction qui calcule la somme de 'n' premiers nombres somme=0+1+2+3+....+n
    somme=0
    k=1
    while(k<n+1):
        somme+=k
        k+=1
    return somme

#Tests
print(firstfunction(1.5))
print(secondfunction(8))
print(thirdfunction(9))
    
"DEUXIEME PARTIE DU TP1"

#SIMULATION DE LOIS DISCRETES

#Application1
def Bernoullifunction(N,p):
    x=np.zeros(N)
    k=0
    while(k<N):
        if random()<=p:
            x[k]=1
            k+=1
        else:
            x[k]=0
            k+=1
    return x

print(Bernoullifunction(10,0.2))

#Application2

def Binomiale(n,p):
    X=0
    for i in range(n):
        if (random()<=p):
            X+=1
    return X

def NBinomialeloi(N,n,p):
  
    x=np.zeros(N)
    for k in range(N):
      x[k]=Binomiale(n,p)
    return x

print(NBinomialeloi(5,10,0.8))


#Application3

#Premiere maniere


def Geometrique(p):
    t=1
    while(random()>p):
            t+=1
    return t

def Geometriqueloi1(N,p):
    x=np.zeros(N)  
    for k in range(N):
        x[k]=Geometrique(p)
    return x

print(Geometriqueloi1(6,0.8))

#Deuxieme maniere
def Geometriqueloi2(N,p):
    x=np.zeros(N)
    lambd=-log(1-p)
    for k in range(N):
        x[k]=1+int((-1/lambd)*log(random()))
    return x
print(Geometriqueloi2(6,0.8))

#SIMULATION DE LOIS DE DENSITE PAR LA METHODE D'INVERSION

#Application4

def Exponentielleloi(N,l):
    x=np.zeros(N)
    
    for k in range(N):
        x[k]=(-1/l)*log(1-random())
    return x

print(Exponentielleloi(6,0.6))

#Application5


def Cauchyloi(N,m,a):
    x=np.zeros(N)
    
    for k in range(N):
        x[k]=a*tan(pi*(random()-0.5))+m
    return x

print(Cauchyloi(6,4,0.5))


#Application6

def Rayleightloi(N):
    x=np.zeros(N)
    for i in range(N):
        x[i]=sqrt(-2*log(1-random()))
    return x

print(Rayleightloi(6))

"**********************TP2**********************************"

#SIMULATION DE LOIS A DENSITE PAR LA METHODE DE REJET

#Application1:LOI BETA

def densitef(x):
    return 6*x*(1-x)*g(x)

def g(x):
    if (x>=0 and x<=1): 
        return 1
    else:
        return 0
    
    
def Beta22():
    teta=1.5
    y=random()
    while densitef(y)<=teta*random()*g(y):
            y=random()
    return y
        
    
def Beta22N(N):
   x=np.zeros(N)
   
   for k in range(N):
       x[k]= Beta22()
   return x
print(Beta22N(10))

#Application2:LOI GAMMA

def densitegamma(x):
    return 2*sqrt(x/pi)*exp(-x)*Igama(x)


def densiteg(x):
    return (2./3)*exp((-2./3)*x)*Igamma(x)


def Igamma(x):
    if x<0:
        return 0
    else:
        return 1
    
def Gamma():
    teta=(3**1.5)/(sqrt(2*pi*e))
    y=random()
    while densitef(y)<=teta*random()*g(y):
            y=random()
    return y
        
    
def GammaN(N):
   x=np.zeros(N)
   
   for k in range(N):
       x[k]= Gamma()
   return x
print(GammaN(10))    
    
    
#Application3: HISTOGRAMMES

import scipy
from pylab import*
import pylab as pylab

#Exemple
#lamb=1./3
#tableau=-1./lamb*log(1-random(10000));
#m1=pylab.hist(tableau,bins=linspace(0,6/lamb,61),normed=True)
#x=linspace(0,6./lamb,61)
#y=lamb*exp(-lamb*x)
#plot(x,y,color='red')

#Histogramme pour une loi binomiale

n=12
p=0.4
tableau=NBinomialeloi(10000,n,p)
m1=pylab.hist(tableau,bins=linspace(0,n,n+1),normed=True)
x=linspace(0,n,n+1)
y=linspace(0,n,n+1)
for i in range(n+1):
    y[i]=factorial(n)/(factorial(x[i])*factorial(n-x[i]))*pow(p,x[i])*pow(1-p,n-x[i])
plot(x,y,color='red')

#Histogramme pour une loi geométrique 

from pylab import*

p=0.6
tableau=Geometriqueloi1(10000,p)
m1=pylab.hist(tableau,bins=linspace(0,int(5/p),n+1),normed=True)
x=linspace(0,int(5/p),int(5/p)+1)
y=linspace(0,int(5/p),int(5/p)+1)
for i in range (int(5/p)+1):
         y[i]=p*pow((1-p),x[i]-1)
plot(x,y,color='red')        
         
  
#Histogramme pour une loi exponentielle

from pylab import*
n=10
l= 2./3
tableau=Exponentielleloi(10000,l)
m1=pylab.hist(tableau,bins=linspace(0,n,n+1),normed=True)
x=linspace(0,n,n+1)
y=linspace(0,n,n+1)
for i in range (n+1):
         y[i]=l*exp(-x[i]*l)*Igamma(x[i])
plot(x,y,color='red') 


#Histogramme pour une loi Gamma

l=3./2
a=1
n=10
tableau=GammaN(10000)
m1=pylab.hist(tableau,bins=linspace(0,n,n+1),normed=True)
x=linspace(0,n,n+1)
y=linspace(0,n,n+1)
for i in range (n+1):
         y[i]=(pow(x[i],a-1)*pow(l,a)*exp(-l*x[i])*Igamma(x[i]))
plot(x,y,color='red')        
         

#Histogramme pour une loi 



    
