import numpy as np
import matplotlib.pyplot as plt
xArray = np.array([])
yArray = np.array([])

xMin = 0
xMax = 500000 / 257.6
yMin = 0
yMax = 120000
h = 0.1

xi = 0
yi = 120000
fburn = 0
rho = 0.78
v = 257.6
S = 29
K = 0.7 + 0.2*np.tanh(5*(0.8-0.95))
CD = 0.04+0.02*np.tanh(5*(0.8-0.95))

def derivativeFunction(x,yi):    
    f = -0.7*(1/3600)*((0.5*rho*v*v*S*CD + (2*K*yi*yi)/(rho*v*v*S)))
    print(f)
    return f

while xi >= xMin and xi <= xMax:
 xArray = np.append(xArray, xi)
 yArray = np.append(yArray, yi)
 fPrime = derivativeFunction(xi, yi)
 dy = h*fPrime
 xi += h
 yi += dy
 fburn -= dy
 print(fburn)
plt.plot(xArray, yArray)
plt.xlim(xMin, xMax)
plt.ylim(yMin, yMax)
plt.xlabel("Time (s)")
plt.ylabel("Mass (kg)")
plt.title("Mass versus Time")
plt.grid()
plt.show()

 
 