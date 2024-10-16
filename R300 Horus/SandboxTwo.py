import numpy as np
import matplotlib.pyplot as plt
from numpy import random

xArray = np.array([])
yArray = np.array([])

for i in range(100):
    x = i
    y = random.rand()
    xArray = np.append(xArray, i)
    yArray = np.append(yArray, y)
    
plt.plot(xArray, yArray, color = 'red')
plt.show()
    
    
    


