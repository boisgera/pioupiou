Gaussians
================================================================================

![Multivariate gaussians](images/gaussians.svg)

Imports:

```python
import numpy as np
import pioupiou as pp; pp.restart()
```


Bivariate Gaussian
--------------------------------------------------------------------------------

```python
def Normal2(mu1, mu2, Sigma11, Sigma12, Sigma22):
    Sigma21 = Sigma12
    N1 = pp.Normal(mu1, Sigma11)
    mu = mu2 + Sigma21 / Sigma11 * (N1 - mu1)
    N2 = pp.Normal(mu, Sigma22 - Sigma21 / Sigma22 * Sigma12)
    return N1, N2
```

Model
--------------------------------------------------------------------------------

```python
mu, Sigma = [0.0, 0.0], [[1.0, 0.75], [0.75, 1.0]]
X, Y = Normal2(mu[0], mu[1], Sigma[0][0], Sigma[0][1], Sigma[1][1])
```

Simulation
--------------------------------------------------------------------------------

```python
>>> omega = pp.Omega(1000)
>>> x, y = X(omega), Y(omega)
>>> x # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE 
    array([ 3.50349227e-01, -6.13458179e-01, -1.73949889e+00, ...])
>>> y # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE 
    array([-1.20958718e+00,  1.65204470e-01, -1.31085277e+00, ...])
```

Visualization
--------------------------------------------------------------------------------

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.DataFrame({"x":x, "y": y})
p = sns.jointplot(x="x", y="y", data=data,
                  kind="scatter", alpha=1.0,
                  xlim=(-4.0, 4.0), ylim=(-4.0, 4.0))
_ = p.fig.suptitle("Correlated Gaussian Variables", fontsize="medium")
p.fig.tight_layout()
plt.savefig("gaussians.svg")
```

References
--------------------------------------------------------------------------------

  - [Gaussians, in Advanced Robotics (Berkeley CS 287) by Pieter Abbeel](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/Gaussians.pdf)