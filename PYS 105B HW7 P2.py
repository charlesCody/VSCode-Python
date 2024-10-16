#Import Declarations
import numpy as np
import matplotlib.pyplot as plt

#Arrays for Plotting
xArray = np.array([])
yArray = np.array([])

#Limits of Solution
xMin = 0
xMax = 10
yMin = -10
yMax = 10
h = 1.5

#Initial Values
xi = 0
yi = 1

#Equation to be Solved
def f(x,y):
    f = np.sin(x)
    return f

#RK2 Algorithm
while xi >= xMin and xi <= xMax:
    xArray = np.append(xArray, xi)
    yArray = np.append(yArray, yi)
    k1 = h*f(xi, yi)
    k2 = h*f(xi + k1/2, yi + h/2)
    xi += h
    yi += k2
 
#Plotting Solution   
plt.plot(xArray, yArray)
plt.xlim(xMin, xMax)
plt.ylim(yMin, yMax)
plt.show()
    
 
