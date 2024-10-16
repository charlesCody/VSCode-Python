#Import Declarations
from scipy.integrate import *
import matplotlib.pyplot as plt
import numpy as np

#Part A
gamma = 2
w0 = 3

#Differential Equation
def equation(x, gamma, w0):
    f = x[2] + gamma*x[1] + w0*w0*x[0]
    return f

#Arguments for Odeint and Odeint Calculation
time = np.arange(0,1000,0.01)
position = odeint(equation, [0,0,0], time).T

#Plotting Solution
plt.plot(time, position, 'red', linewidth = 2)
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()

#Part B
h = 0.01

#Differential Equation
def f(xPrime, x):
    f = gamma*xPrime + w0*w0*x
    return f

#Initial Conditions
xPrimePrime = 0
xPrime = 0
x = 0
t = 0

#Arrays for Plotting
xArray = np.array([])
tArray = np.array([])

#Euler's Method
while t <= 1000:
    xPrimePrime = f(xPrime, x)
    xPrime += xPrimePrime*h
    x = -(xPrimePrime - gamma*xPrime)/w0*w0
    xArray = np.append(xArray, x)
    tArray = np.append(tArray, t)
    t += h

#Plotting Solution
plt.plot(tArray, xArray)
plt.xlabel("Time")    
plt.ylabel("Position")

#Part C
#Equation for Odeint to Solve
def equation(x):
    f = x*x + 7
    return f

#Calculation of Odeint
time = np.arange(0,1000,0.01)
position = odeint(equation, [0], time).T

#Plotting Solution
plt.plot(time, position)
plt.xlabel("Time")
plt.ylabel("Position")
plt.show()



