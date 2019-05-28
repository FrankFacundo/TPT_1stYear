import numpy.random as npr
from pylab import*
from random import*
from math import*
import numpy as np


#Application1: Methode de Box-Muller

def densitef(x):
    return (1/sqrt(2*pi))*exp(-pow(x,2)/2)


def LoiNormale():
    U1=random()
    U2=random()
    X=sqrt(-2*log(U1))*cos(2*pi*U2)
    return X

def LoiNormaleN(N):
    Y=np.zeros(N)
    for i in range(N):
        Y[i]=LoiNormale()
    return Y

print(LoiNormaleN(10))

#Histogramme
import scipy
from pylab import*
import pylab as pylab
from pylab import*

tableau=LoiNormaleN(10000)
m1=pylab.hist(tableau,bins=linspace(-10,10,21),normed=True)
x=linspace(-10,10,21)
y=linspace(-10,10,21)
for i in range (21):
         y[i]=densitef(x[i])
plot(x,y,color='red') 
    
#Application2: Methode de Rejet via la loi de Laplace

def densiteg(x):
    return (1/2)*exp(-np.abs(x))

def  LoideLaplace():
    U=random()
    X=-sign(U-0.5)*log(1-2*np.abs(U-0.5))
    return X

def LoideLaplaceN(N):
    Y=np.zeros(N)
    for i in range(N):
        Y[i]=LoideLaplace()
    return Y

print(LoideLaplaceN(5))

#Simulation d'une loi normale a l'aide d'une loi de Laplace

def LoiNormalefromLoiLaplace():
    teta=np.sqrt(2*(np.e)/np.pi)
    y= LoideLaplace()
    uk = npr.random()
    while densitef(y)<=uk*teta*densiteg(y):
            y= LoideLaplace()
    return y

def LoiNormalefromLoiLaplaceN(N):
   x=np.zeros(N)
   
   for k in range(N):
       x[k]= LoiNormalefromLoiLaplace()
   return x

print(LoiNormalefromLoiLaplaceN(10))
    
tableau=LoiNormalefromLoiLaplaceN(10000)
m1=pylab.hist(tableau,bins=linspace(-10,10,21),normed=True)
x=linspace(-10,10,21)
y=linspace(-10,10,21)
for i in range (21):
         y[i]=densitef(x[i])
plot(x,y,color='red') 

#Application3: Lois derives de la loi Normale

def I(x):
    if x<0:
        return 0
    else:
        return 1
    
def densitekhi(x,n):
    return pow(x,(n/2)-1)*exp(-x/2)*I(x)/((pow(2,n/2))*math.gamma(n/2))

def S(n):
    somme=0
    for i in range(n):
        somme=somme+ pow(LoiNormale(),2)
    return somme

def LoiKhideux(n,N):
    
    Y=np.zeros(N)
    for i in range(N):
        Y[i]=S(n)
    return Y
#Histogramme de la loi Khideux
n=5
tableau=LoiKhideux(n,10000)
m1=pylab.hist(tableau,bins=linspace(-10,10,21),normed=True)
x=linspace(-10,10,21)
y=linspace(-10,10,21)
for i in range (21):
         y[i]=densitekhi(x[i],n)
plot(x,y,color='red')    

#Application4: Loi de Student

def densiteStudent(x,n):
    return math.gamma((n+1)/2)/(math.gamma(n/2)*sqrt(pi*n)*pow(1+pow(x,2)/n,(n+1)/2))

def X(n):
    Z=LoiNormale()
    Yn=S(n)
    return Z/(sqrt(Yn/n))

def LoideStudent(n,N):
     
    Y=np.zeros(N)
    for i in range(N):
        Y[i]=X(n)
    return Y
#Histogramme de la loi Student
n=5
tableau=LoideStudent(n,10000)
m1=pylab.hist(tableau,bins=linspace(-10,10,21),normed=True)
x=linspace(-10,10,21)
y=linspace(-10,10,21)
for i in range (21):
         y[i]=densiteStudent(x[i],n)
plot(x,y,color='red')   


#RESULTAT REMARQUABLE
def LoiNormale1(m,l2):
    X=LoiNormale()
    return sqrt(l2)*X+m

def Xnmoy(m,n,l2):
    
    somme=0
    for i in range(n):
        somme=somme+LoiNormale1(m,l2)
    return somme/n

def LoiSn2(m,n,l2):
    somme=0
    for i in range(n):
        somme=pow((LoiNormale()-Xnmoy(m,n,l2)),2)
    return somme/(n-1)

def Zn(m,n,l2):
    return ((n-1)*LoiSn2(m,n,l2))/l2

def Tn(m,n,l2):
    return sqrt(n)*(Xnmoy(m,n,l2)-m)/LoiSn2(m,n,l2)

def LoiZn(m,n,l2,N):
    Y=np.zeros(N)
    for i in range(N):
        Y[i]=Zn(m,n,l2)
    return Y
    
def LoiTn(m,n,l2,N):
    T=np.zeros(N)
    for i in range(N):
        T[i]=Tn(m,n,l2)
    return T

#Simulation experimentale----Voir histogrammes

#Pour Zn
m=3
l2=2
n=6
tableau=LoiZn(m,n,l2,10000)
m1=pylab.hist(tableau,bins=linspace(-20,20,41),normed=True)
x=linspace(-20,20,41)
y=linspace(-20,20,41)
for i in range (41):
         y[i]=densitekhi(x[i],n)
plot(x,y,color='red') 

#Pour Tn
m=3
l2=2
n=6
tableau=LoiTn(m,n,l2,10000)
m1=pylab.hist(tableau,bins=linspace(-20,20,41),normed=True)
x=linspace(-20,20,41)
y=linspace(-20,20,41)
for i in range (41):
         y[i]=densiteStudent(x[i],n-1)
plot(x,y,color='red') 

#Lien avec la loi binomiale
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

def Bn(n,p):
    Y=Binomiale(n,p)-n*p
    return Y/(sqrt(n*p*(1-p)))

def LoiBn(n,p,N):
    
    B=np.zeros(N)
    for i in range(N):
        B[i]=Bn(n,p)
        
    return B

#Pour Bn
p=0.5
n=5
tableau=LoiBn(n,p,10000)
m1=pylab.hist(tableau,bins=linspace(-20,20,41),normed=True)
x=linspace(-20,20,41)
y=linspace(-20,20,41)
for i in range (41):
         y[i]=densitef(x[i])
plot(x,y,color='red') 


#Lien avec la loi de Poisson


def LoiExponentielle(a):
    U=random()
    return -(1./a)*(log(1-U))

def LoiExponentielleN(a,n):
    vecteur=np.zeros(n)
    for i in range(n):
        vecteur[i]=LoiExponentielle(a)
    return vecteur
        
    

def Sn1(T,n):
    somme1=0
    for i in range(n):
        somme1=somme1+T[i]
    return somme1
   
def LoidePoisson(a):
    n=100
    vecteur=LoiExponentielleN(a,n)
    somme1=0
    for i in range (n):
        if Sn1(vecteur,i)<=1:
            somme1=somme1+1
    return somme1

def LoidePoissonN(a,N):
   x=np.zeros(N)
   for k in range(N):
       x[k]= LoidePoisson(a)
   return x

def densitef2p(x,m,l2):
    return 1/np.sqrt(2*pi*l2)*exp(-pow(x-m,2)/(2*l2))


#Histogramme pour la loi de poisson   
a=100
N=1000
tableau=LoidePoissonN(a,N)
m1=pylab.hist(tableau,bins=linspace(0,200,201),normed=True)
x=linspace(0,200,201)
y=linspace(0,200,201)
for i in range (201):
         y[i]=densitef2p(x[i],a,a)
plot(x,y,color='red')         
    
    
    
    
    
    
    
    

    
    
    