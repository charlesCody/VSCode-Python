#Import Declarations
import numpy as np
import matplotlib.pyplot as plt 
from numpy import random

#Part A
#Variable Constants and Initial Conditions
x = 0
l = 10**(-4)
N = 1000
sigma = 0.3 
mu = 0
xi = 0
yGuess = 1
yGaussian = 0 
i = 0

#Axis Arrays for Plotting
xArray = np.array([])
tArray = np.array([])

#Gaussian Definition
def Gaussian(x, mu, sigma):
    yGaussian = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/(sigma))**2)
    return yGaussian    

#I used a while loop because number of iterations to produce N points is not fixed
while i < N:
    xi = random.rand()
    xi *= 20
    xi -= 10
    yGuess = random.rand()
    yGaussian = Gaussian(xi, mu, sigma)
    
    if yGuess <= yGaussian:
        xArray = np.append(xArray, x)
        tArray = np.append(tArray, i)
        x = x -l*x*x*x + xi
        i += 1
    
    #Skip Loop Otherwise
    else:
       pass
   

plt.plot(tArray, xArray)
plt.xlabel("Time Steps")
plt.ylabel("Position")
plt.show()
    
#Parts B and C
#Variable Constants and Initial Conditions

x = 0
l = 10**(-4)
N = 50000
sigma = 0.3 
mu = 0
xi = 0
yGuess = 1
yGaussian = 0 
i = 0

#Initializing Arrays
xArray = np.array([])
tArray = np.array([])
xxArray = np.array([])
XXArray = np.array([])

#Define Gaussian
def Gaussian(x, mu, sigma):
    yGaussian = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/(sigma))**2)
    return yGaussian    

#I used a while loop because number of iterations to produce N points is not fixed
while i < N:
    xi = random.rand()
    xi *= 20
    xi -= 10
    yGuess = random.rand()
    yGaussian = Gaussian(xi, mu, sigma)
    
    #Condition for if random value is within Gaussian distribution
    if yGuess <= yGaussian:
        xArray = np.append(xArray, x)
        tArray = np.append(tArray, i)
        x = x -l*x*x*x + xi
        xxArray = np.append(xxArray, x*x)
        xx = np.mean(xxArray)
        XXArray = np.append(XXArray, xx)
        
        i += 1
    #Skip iteration otherwise
    else:
       pass
   
#Plotting random walk
plt.plot(tArray, XXArray)
plt.xlabel("Time Step")
plt.ylabel("Mean Position-Squared")
plt.show()

#Proportional Relationship Fails after about 2000 time steps. 
#The system reaches a state of equilibrium at about 10000 time steps. 
    
        
    