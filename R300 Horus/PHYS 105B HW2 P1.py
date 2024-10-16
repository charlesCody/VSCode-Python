#Import Declarations
import numpy as np
import matplotlib.pyplot as plt 
from numpy import random

#Part A
#Constant Initialization
x = 0 
N = 10000
xGuess = 0
yGuess = 0
yGaussian = 0
sigma = 1
mu = 2
i = 0
h = 5

#Array for Histogram
xArray = np.array([])

#Gaussian Definition
def Gaussian(x, mu, sigma):
    yGaussian = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/(sigma))**2)
    return yGaussian        

#While Loop to Accept Random Point
while i < N:
    x = random.rand()
    x *= 20
    x -= 10
    yGuess = random.rand()
    yGaussian = Gaussian(x, mu, sigma)
    
    if yGuess <= yGaussian:
        xArray = np.append(xArray, x)
        i += 1
    
    else:
       pass
    
    
#Part B
plt.hist(xArray, bins = 50)
plt.show()



#Part C
xArray = np.array([])
i = 0

#Bimodal Definition as Sum of Two Gaussians
def Bimodal(x, mu, sigma):
    yBimodal = (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/(sigma))**2) + (1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x - h - mu)/(sigma))**2)
    return yBimodal        

#While Loop for Accepting Points
while i < N:
    x = random.rand()
    x *= 20
    x -= 10
    yGuess = random.rand()
    yBimodal = Bimodal(x, mu, sigma)
    
    if yGuess <= yBimodal:
        xArray = np.append(xArray, x)
        i += 1
    
    else:
       pass
   
#Plotting Histogram 
plt.hist(xArray, bins = 50)
plt.show()

