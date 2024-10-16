#Import Declarations
import numpy as np
from scipy import integrate
from numpy import random
import timeit

#Part A
#Single Variable Integration
def integrand(x1):
    function = ((x1**2)**(1.5))*np.exp(-np.sqrt(x1**2))
    return function

#Scipy Integral Function
integral = integrate.nquad(integrand, [[-1,1]])
print(integral)

#Two Variable Integration
def integrand(x1, x2):
    function = ((x1**2 + x2**2)**(1.5))*np.exp(-np.sqrt(x1**2 + x2**2))
    return function

#Scipy Integral Function
integral = integrate.nquad(integrand, [[-1,1], [-1,1]])
print(integral)

#Three Variable Integration
def integrand(x1, x2, x3):
    function = ((x1**2 + x2**2 + x3**2)**(1.5))*np.exp(-np.sqrt(x1**2 + x2**2 + x3**2))
    return function

#Scipy Integral Function
integral = integrate.nquad(integrand, [[-1,1], [-1,1], [-1,1]])
print(integral)

#Part B
#Variable Initialization
nSteps = 1000000
integral = 0
#For Loop Condition
for i in range(nSteps):
    #Variable Initialization and Fitting to [-1,1]
    x1 = random.rand()
    x1 *= 2
    x1 -= 1
    x2 = random.rand()
    x2 *= 2
    x2 -= 1
    x3 = random.rand()
    x3 *= 2
    x3 -= 1
    #Integral Function
    integral += ((x1**2 + x2**2 + x3**2)**(1.5))*np.exp(-np.sqrt(x1**2 + x2**2 + x3**2))
    
#Print Output
print(integral)
    
#Part C
#Initial Index
i = 0
#Loop Condition
while i <= 1000000:
    x1 = random.rand()
    p = 1/np.sqrt(2*np.pi)*np.exp(-0.5*((x1)/(1))**2)
   #Check for X1
    if x1<p:
        pass
    else:
        continue
    x2 = random.rand()
    p = 1/np.sqrt(2*np.pi)*np.exp(-0.5*((x1)/(1))**2)
    #Check for X2
    if x1<p:
        pass
    else:
        continue
    x3 = random.rand()
    p = 1/np.sqrt(2*np.pi)*np.exp(-0.5*((x1)/(1))**2)
    
    #Check for X3
    if x1<p:
        pass
    else:
        continue
    
    #Integral Calculation
    integral += ((x1**2 + x2**2 + x3**2)**(1.5))*np.exp(-np.sqrt(x1**2 + x2**2 + x3**2))
    i += 1
    
    print(integral)
    

    