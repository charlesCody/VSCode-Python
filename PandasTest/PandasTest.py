import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SFOTest.csv')
print(df.to_string())

df.plot(x = "Year", y = "Passenger Numbers")
plt.show()