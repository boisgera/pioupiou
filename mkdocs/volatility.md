Stochastic Volatility
================================================================================

![Stochastic volatility](images/volatility.svg)

Imports:

    >>> import numpy as np
    >>> import pioupiou as pp; pp.restart()

Model
--------------------------------------------------------------------------------

    >>> import sys; sys.setrecursionlimit(10000)

    >>> n = 100
    >>> ts = np.arange(n)
    >>> mu, phi, sigma = -1.02, 0.95, 0.25
    >>> H, Y = np.zeros(n, dtype=object), np.zeros(n, dtype=object)
    >>> for t in ts:
    ...     if t == 0:
    ...         H[t] = pp.Normal(0, sigma / np.sqrt(1 - phi*phi))
    ...     else:
    ...         H[t] = mu + phi * (H[t-1] - mu) + pp.Normal(0, sigma)
    ...     Y[t] = pp.Normal(0, pp.exp(0.5 * H[t]))

Simulation
--------------------------------------------------------------------------------

    >>> omega = pp.Omega(100)
    >>> y = np.array([Yt(omega) for Yt in Y])
    >>> y
    array([[-0.05773976, -0.57186803,  0.42281951, ...,  1.61299726,
             3.2987983 ,  0.32896572],
           [ 1.32720842,  0.14537157, -0.92996065, ..., -3.3256374 ,
            -0.30841941, -0.4073805 ],
           [-1.28497634,  0.95743407,  0.71283735, ..., -1.42421353,
             1.87967335, -1.05327587],
           ...,
           [-0.01724657, -0.58057645, -0.40096819, ..., -1.49506038,
            -0.59421322,  0.2268457 ],
           [ 0.08327353,  0.98911348, -1.09761652, ...,  1.61856385,
             1.13148655, -0.44633602],
           [ 0.40559841, -0.68739109,  0.422678  , ...,  0.53063852,
             0.75591863,  0.12564758]])

References
--------------------------------------------------------------------------------

  - [Stochastic Volatility Models in Stan User's Guide](https://mc-stan.org/docs/2_21/stan-users-guide/stochastic-volatility-models.html)
