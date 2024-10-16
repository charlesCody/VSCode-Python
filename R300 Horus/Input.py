#library importations
import time 
import numpy as np

class Input():
    def __init__(self):
        pass
    
    def initialValues(self):
        v = 250.8
        t = 1
        tMax = 1200
        dt = 0.01
        xArray = np.array([])
        tArray = np.array([])
        vArray = np.array([])
        aArray = np.array([])
        throttleArray = np.array([])
        referenceArray = np.array([])

        mass = 285000
        thrust1 = 386950
        thrust2 = 386950
        x = 0
        throttleInitial = 1
        
        dragCoefficient = 0.023
        crossSectionalArea = 38
        yFeet = 36000
        y = (yFeet * 12) / (2.54*100)

        return t, tMax, dt, x, y, tArray, xArray, vArray, aArray, throttleArray, referenceArray, mass, thrust1, thrust2, dragCoefficient, crossSectionalArea, v, throttleInitial, 
   
    def referenceVelocity(t):
        if t <= 300:
            referenceVelocity = 206
        elif t > 300 and t <= 650:
            referenceVelocity = 129
        else:
            referenceVelocity = 262
        return referenceVelocity