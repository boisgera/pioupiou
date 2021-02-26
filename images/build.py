#!/usr/bin/env python

import seaborn as sns ; sns.set_theme(style="whitegrid")
import matplotlib.pyplot as plt
import pandas as pd
import pioupiou as pp

import pioupiou as pp
a, b = 0.5, 1.0
X = pp.Uniform(0.0, 1.0)
E = pp.Normal(0.0, 0.1)
Y = a * X + b + E
omega = pp.Omega(500) 
x, y = X(omega), Y(omega)
# import numpy as np
# print(f"mean: {np.mean(y)}, standard deviation: {np.std(y)}")

data = pd.DataFrame({"x":x, "y": y})

g = sns.jointplot(x="x", y="y", data=data,
                  kind="reg", truncate=False,
                  xlim=(0.0, 1.0), ylim=(0.5, 2.0))
#                  ratio = 4/3) #height=7)

plt.savefig("xy.svg")