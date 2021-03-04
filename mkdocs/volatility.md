Stochastic Volatility
================================================================================

![Stochastic volatility](images/volatility.svg)

Imports:

    >>> import numpy as np
    >>> import pioupiou as pp; pp.restart()

Model
--------------------------------------------------------------------------------

The evolution of the asset price \(Y_t\) at time \(t\) is given by

\[
    Y_t \sim \mathcal{N}(0, \exp(H_t/2))
\]

where initially

\[
    H_0 \sim \mathcal{N}\left(\mu, \frac{\sigma}{\sqrt{1 - \phi^2}}\right)
\]

and then

\[
    H_t = \mu  + \phi(H_{t-1}- \mu) + \Delta_t \; \mbox{ with } \; \Delta_t \sim \mathcal{N}(0,\sigma^2).
\]


    >>> mu, phi, sigma = -1.02, 0.95, 0.25
    >>> n = 100
    >>> ts = np.arange(n)
    >>> H, Y = np.zeros(n, dtype=object), np.zeros(n, dtype=object)
    >>> for t in ts:
    ...     if t == 0:
    ...         H[t] = pp.Normal(mu, sigma / np.sqrt(1 - phi*phi))
    ...     else:
    ...         H[t] = mu + phi * (H[t-1] - mu) + pp.Normal(0, sigma)
    ...     Y[t] = pp.Normal(0, pp.exp(0.5 * H[t]))

Simulation
--------------------------------------------------------------------------------

Given that our model is deeply nested, we need to increase the recursion limit:

    >>> import sys; sys.setrecursionlimit(10000)

Then, as usual:

    >>> omega = pp.Omega(100)
    >>> y = np.array([Yt(omega) for Yt in Y])
    >>> y
    array([[-0.03467247, -0.34340423,  0.25390125, ...,  0.96859772,
             1.98091379,  0.19754246],
           [ 0.81756718,  0.08954963, -0.57286052, ..., -2.04860967,
            -0.18998793, -0.25094848],
           [-0.81096151,  0.60424628,  0.44987883, ..., -0.8988355 ,
             1.18628077, -0.664733  ],
           ...,
           [-0.01718594, -0.5785354 , -0.39955856, ..., -1.4898044 ,
            -0.59212422,  0.22604821],
           [ 0.08299539,  0.98580976, -1.09395039, ...,  1.61315771,
             1.12770729, -0.44484522],
           [ 0.40431131, -0.68520976,  0.4213367 , ...,  0.52895462,
             0.75351984,  0.12524886]])

References
--------------------------------------------------------------------------------

  - [Stochastic Volatility Models in Stan User's Guide](https://mc-stan.org/docs/2_21/stan-users-guide/stochastic-volatility-models.html)
