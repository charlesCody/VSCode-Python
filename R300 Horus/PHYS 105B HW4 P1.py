#Part A
#Import Declarations
import numpy as np 
from numpy import random
import matplotlib.pyplot as plt 

#Initial Variables
N = 1000
pRight = 0.5

#Variables for first plot
X1 = 0
t1 = 0
xArrayOne = np.array([])
tArrayOne = np.array([])

#first calculation loop
for N in range(1000):
    x = random.rand()
    if x < pRight:
        X1 += 1
    else:
        X1 -= 1
    x = random.rand()
    if x < pRight:
        t1 += 1
    else:
        t1 -= 1
    xArrayOne = np.append(xArrayOne, X1)
    tArrayOne = np.append(tArrayOne, t1)
    


#second initialization  
X2 = 0
t2 = 0
xArrayTwo = np.array([])
tArrayTwo = np.array([])

#Second calculation loop
for N in range(1000):
    x = random.rand()
    if x < pRight:
        X2 += 1
    else:
        X2 -= 1
    x = random.rand()
    if x < pRight:
        t2 += 1
    else:
        t2 -= 1
    xArrayTwo = np.append(xArrayTwo, X2)
    tArrayTwo = np.append(tArrayTwo, t2)

#Third initialization
X = 0
t = 0
xArrayThree = np.array([])
tArrayThree = np.array([])

#Third calculation loop
for N in range(1000):
    x = random.rand()
    if x < pRight:
        X += 1
    else:
        X -= 1
    x = random.rand()
    if x < pRight:
        t += 1
    else:
        t -= 1

    xArrayThree = np.append(xArrayThree, X)
    tArrayThree = np.append(tArrayThree, t)
  
#Plotting Random Walks  
plt.plot(tArrayOne, xArrayOne, color = 'b')
plt.plot(tArrayTwo, xArrayTwo, color = 'g')
plt.plot(tArrayThree, xArrayThree, color = 'r')
plt.title("Third Random Walk")
plt.xlabel("t")
plt.ylabel("X")
plt.show()

#Part B
#Initial Variables
N = 1000
pRight = 0.5
variance = 1
mean = 0
rng = np.random.default_rng()
#Variables for first plot
X1 = 0
t1 = 0
increment = rng.normal()
xArrayOne = np.array([])
tArrayOne = np.array([])

#first calculation loop
for N in range(1000):
    x = random.rand()
    if x < pRight:
        X1 += increment
    else:
        X1 -= increment
    x = random.rand()
    if x < pRight:
        t1 += increment
    else:
        t1 -= increment
    xArrayOne = np.append(xArrayOne, X1)
    tArrayOne = np.append(tArrayOne, t1)
    


#second initialization  
X2 = 0
t2 = 0
increment = rng.normal()
xArrayTwo = np.array([])
tArrayTwo = np.array([])

#Second calculation loop
for N in range(1000):
    x = random.rand()
    if x < pRight:
        X2 += increment
    else:
        X2 -= increment
    x = random.rand()
    if x < pRight:
        t2 += increment
    else:
        t2 -= increment
    xArrayTwo = np.append(xArrayTwo, X2)
    tArrayTwo = np.append(tArrayTwo, t2)

#Third initialization
X = 0
t = 0
increment = rng.normal()
xArrayThree = np.array([])
tArrayThree = np.array([])

#Third calculation loop
for N in range(1000):
    x = random.rand()
    if x < pRight:
        X += increment
    else:
        X -= increment
    x = random.rand()
    if x < pRight:
        t += increment
    else:
        t -= increment
    
    xArrayThree = np.append(xArrayThree, X)
    tArrayThree = np.append(tArrayThree, t)
  
#Plotting Random Walks  
plt.plot(tArrayOne, xArrayOne, color = 'b')
plt.plot(tArrayTwo, xArrayTwo, color = 'g')
plt.plot(tArrayThree, xArrayThree, color = 'r')
plt.title("Random Walk")
plt.xlabel("t")
plt.ylabel("X")
plt.show()
