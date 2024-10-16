#Import Declarations
import numpy as np
from  numpy import random
import matplotlib.pyplot as plt

#Variable Initialization
p = 0.6
L = 2*p
n = 10000
x = 0

#Part D
variance = 0
averageCubed = 0

for i in range(n):
    X = random.rand()
    if X < p:
        x += X
        variance += X*X
        averageCubed += X*X*X
        
    else:
     pass
averageCubed /= 10000

skew = averageCubed / variance**(1.5)

print("Average: ", x, "Variance ", variance, "Skew ", skew )



#Part E
#Loop Through N
for n in [100,1000,10000]:
    x = 0
    variance = 0
    varianceAverage = 0
    skewAverage = 0
    averageCubed = 0
    #Loop Through Samples
    for i in range(10000):
        for N in range(n):
            x = random.rand()
            if x < p:
                x += 1
            else:
                x -= L
            variance += x*x
            averageCubed += x*x*x
        variance /= N
        skew = averageCubed / (N * variance**1.5)
        varianceAverage += variance
        skewAverage += skew
    #Calculate Variance and Skew
    varianceAverage /= 10000
    skewAverage /= 10000
    
    #Print Average
    print("Average: ", x, "Variance ", variance, "Skew ", skew )





        
        