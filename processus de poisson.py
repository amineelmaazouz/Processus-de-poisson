# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:43:01 2023

@author: amine el maazouz
"""

from random import *
from math import log
from matplotlib.pyplot import *
def poisson (lam) :
    X_T=[]
    i=0
    while i<N:
        v=uniform(0,1)
        if v!=0:
            X_T.append(((-lam)**(-1))*log(v))
            i+=1
    S =[0]*(N)
    for i in range (N-1) :
        S[i +1]=S[i]+X_T[i+1]
    return S
#tests
N=50
lam=[1 ,2 ,4]
X = np.linspace(0,N,N)
for l in lam:
    S=poisson(l)
    step(S,X,label="Lambda = %d" % l )
legend ( )