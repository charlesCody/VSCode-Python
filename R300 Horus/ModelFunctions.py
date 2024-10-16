#library importations
import time 
import numpy as np

class ModelFunctions():
    def __init__(self, y, dragCoefficient, crossSectionalArea, velocity, thrust1, thrust2, throttle, mass):
        self.y = y
        self.dragCoefficient = dragCoefficient
        self.crossSectionalArea = crossSectionalArea
        self.velocity = velocity
        self.thrust1 = thrust1
        self.thrust2 = thrust2
        self.throttle = throttle
        self.mass = mass
        
       
    
    #Calculate Pressure and Temperature
    def altitudeToTemperaturePressureAndDensity(y):
       if y < 11000:
        T = 15.04 - 0.00649 * y
        P = 101.29 * ((T + 273.1)/(288.08)) ** 5.256
       elif y >= 11000 and y <= 25000:
        T = -56.46
        P = 22.65 * np.exp(1.73 - 0.000157 * y)
       else:
        T = -113.21 + 0.00299 * y
        P = 2.488 * ((T + 273.1)/(216.6)) ** (-11.388)
       rho = P / (.2869 * (T + 273.1))
       return P, T, rho

    #Calculate Drag Force
    def dragForce(dragCoefficient, crossSectionalArea, density, velocity):
        FDrag = -0.5*dragCoefficient*crossSectionalArea*density*velocity*velocity
        return FDrag
    
    #Calculate Acceleration
    def accelerationCalculation(thrust1, thrust2, throttle, mass, FDrag):
        acceleration = (throttle*(thrust1 + thrust2)+ FDrag)/(mass) 
        return acceleration
    
    