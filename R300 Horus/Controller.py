#Feed forward controller that adjusts throttle depending on time elapsed
#library importations
import time 
import numpy as np

class Controller():
    def __init__(self):
        pass
        
    def Throttle(t, v, referenceVelocity, integralError, derivativeError):
        error = referenceVelocity - v
        proportionalGain = 2
        integralGain = 2
        derivativeGain = 2
        proportionalThrottle = proportionalGain*error
        integralThrottle = integralGain*integralError
        derivativeThrottle = derivativeGain*derivativeError
        throttle = proportionalThrottle + integralThrottle + derivativeThrottle
        if throttle < 0:
            throttle = 0
        elif throttle > 1:
            throttle = 1
        
        return throttle 
    
    