class ProgramExecution:
    #library importations
    import time 
    import numpy as np
    import matplotlib.pyplot as plt

    #Class Importations
    from ModelFunctions import ModelFunctions
    from Model import Model
    from Input import Input
    from Visualizer import Visualizer
    from Controller import Controller

    #class creation
    Input1 = Input()

    #initial values
    t, tMax, dt, x, y, tArray, xArray, vArray, aArray, throttleArray, referenceArray, mass, thrust1, thrust2, dragCoefficient, crossSectionalArea, v, throttle = Input1.initialValues() 

    ModelFunctions1 = ModelFunctions(y, dragCoefficient, crossSectionalArea, v, thrust1, thrust2, throttle, mass)
    Model1 = Model()
    Controller1 = Controller()

    #propagate state for 30 seconds
    while t <= tMax:
        t, x, v, xArray, tArray, vArray, aArray, throttleArray, referenceArray = Model.ModelFunction(dragCoefficient, crossSectionalArea, thrust1, thrust2, mass, t, dt, y, v,  xArray, vArray, aArray, tArray, throttleArray, referenceArray)
        #time.sleep(0.0005)
    
    Visualizer1 = Visualizer()   
    Visualizer1.VisualizerPlot(xArray, tArray, vArray, aArray, throttleArray, referenceArray)
