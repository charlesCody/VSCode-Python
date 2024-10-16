from ModelFunctions import ModelFunctions
from Controller import Controller
from UserInterface import UserInterface
import numpy as np

class Model():
    def __init__(self):
        pass
    
    def ModelFunction(dragCoefficient, crossSectionalArea, thrust1, thrust2, mass, t, dt, y, v,xArray, vArray, aArray, tArray, throttleArray, referenceArray):
        P, T, rho = ModelFunctions.altitudeToTemperaturePressureAndDensity(y) 
        FD = ModelFunctions.dragForce(dragCoefficient, crossSectionalArea, rho, v)
        referenceVelocity = UserInterface.referenceVelocity(t)
        throttle = Controller.Throttle(t, v, referenceVelocity)
        acceleration = dt*ModelFunctions.accelerationCalculation(thrust1, thrust2, throttle, mass, FD)
        v += acceleration
        x = v * t
        xArray = np.append(xArray, x)
        tArray = np.append(tArray, t)
        vArray = np.append(vArray, v)
        aArray = np.append(aArray, acceleration)
        throttleArray = np.append(throttleArray, throttle)
        referenceArray = np.append(referenceArray, referenceVelocity)
        print("Velocity = ", v, " meters per second ", "Distance = ", x, " meters time = ",t, "seconds ", " throttle level = ", throttle) 
        t += 0.01
        return t, x, v, xArray, tArray, vArray, aArray, throttleArray, referenceArray
       