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

# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import seaborn as sns
import pioupiou as pp; pp.restart()

proportion_female = 0.516
Is_female = pp.Bernoulli(proportion_female)
mu_female = 161.7
sigma_female = (175.0 - 149.0) / (2 * 1.96)
Height_female = pp.Normal(mu_female, sigma_female)
mu_male = 174.4
sigma_male = (189.0 - 162.0) / (2 * 1.96)
Height_male = pp.Normal(mu_male, sigma_male)

Is_male = pp.logical_not(Is_female)
Height = Is_female * Height_female + Is_male * Height_male

omega = pp.Omega(1000)

height = Height(omega) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
df = pd.DataFrame({"Height [cm]": height})
sns.displot(df, x="Height [cm]", stat="density", kde=True, aspect=16/9)
plt.title("Height Distribution in France")
plt.gcf().subplots_adjust(top=0.95)
plt.savefig("height.svg")

# ------------------------------------------------------------------------------

import numpy as np
import pioupiou as pp; pp.restart()


def Normal2(mu1, mu2, Sigma11, Sigma12, Sigma22):
    Sigma21 = Sigma12
    N1 = pp.Normal(mu=mu1, sigma=pp.sqrt(Sigma11))
    mu = mu2 + Sigma21 / Sigma11 * (N1 - mu1)
    sigma = pp.sqrt(Sigma22 - Sigma21 / Sigma22 * Sigma12)
    N2 = pp.Normal(mu, sigma)
    return N1, N2

mu = [0.0, 0.0]
Sigma = [[1.0, 0.75], [0.75, 1.0]]
N1, N2 = Normal2(mu[0], mu[1], Sigma[0][0], Sigma[0][1], Sigma[1][1])
omega = pp.Omega(1000)
x, y = N1(omega), N2(omega)

data = pd.DataFrame({"x":x, "y": y})
g = sns.jointplot(x="x", y="y", data=data,
                  kind="scatter", alpha=1.0,
                  xlim=(-4.0, 4.0), ylim=(-4.0, 4.0))
#g.plot_joint(sns.kdeplot)

plt.savefig("gaussians.svg")



