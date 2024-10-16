#library importations
import time 
import numpy as np
import matplotlib.pyplot as plt

class Visualizer():
    def __init__(self):
        pass
    
    def VisualizerPlot(self, xArray, tArray, vArray, aArray, throttleArray, referenceArray):
        #Position Subplot
        plt.subplot(1,4,1)
        plt.plot(tArray, xArray, color = 'k')
        plt.title("X position vs Time")
        plt.xlabel("Time (s)")
        plt.ylabel("X position (m)")
        plt.grid()

        #Velocity Subplot
        plt.subplot(1,4,2)
        plt.plot(tArray, vArray, color = 'k')
        plt.plot(tArray, referenceArray, color = 'r')
        plt.title("Velocity vs Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s)")
        plt.grid()

        #Acceleration Subplot
        plt.subplot(1,4,3)
        plt.plot(tArray, aArray, color = 'k')
        plt.title("Acceleration vs Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Velocity (m/s^2)")
        plt.grid()

        #Acceleration Subplot
        plt.subplot(1,4,4)
        plt.plot(tArray, throttleArray, color = 'k')
        plt.title("Throttle vs Time")
        plt.xlabel("Time (s)")
        plt.ylabel("Throttle Level")
        plt.grid()

        plt.show()
    

