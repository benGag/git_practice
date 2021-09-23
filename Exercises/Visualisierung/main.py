import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("cia_factbook.csv")

print(data)
print("SHAPE: ")
print(data.shape)
print("DTYPES: ")
print(data.dtypes)

print(data.describe())

print(data.head(5))

data.hist(column='population')




plt.show()







