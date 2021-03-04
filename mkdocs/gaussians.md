Gaussians
================================================================================

![Multivariate gaussians](images/gaussians.svg)

Imports:

    >>> import numpy as np
    >>> import pioupiou as pp; pp.restart()

Bivariate Gaussian
--------------------------------------------------------------------------------

    >>> def Normal2(mu1, mu2, Sigma11, Sigma12, Sigma22):
    ...     Sigma21 = Sigma12
    ...     N1 = pp.Normal(mu=mu1, sigma=pp.sqrt(Sigma11))
    ...     mu = mu2 + Sigma21 / Sigma11 * (N1 - mu1)
    ...     sigma = pp.sqrt(Sigma22 - Sigma21 / Sigma22 * Sigma12)
    ...     N2 = pp.Normal(mu, sigma)
    ...     return N1, N2

Models
--------------------------------------------------------------------------------

    >>> mu = [0.0, 0.0]
    >>> Sigma = [[1.0, 0.75], [0.75, 1.0]]
    >>> N1, N2 = Normal2(mu[0], mu[1], Sigma[0][0], Sigma[0][1], Sigma[1][1])

Simulation
--------------------------------------------------------------------------------

    >>> omega = pp.Omega(1000)
    >>> x, y = N1(omega), N2(omega)
    >>> x # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE 
    array([ 3.50349227e-01, -6.13458179e-01, -1.73949889e+00, ...])
    >>> y # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE 
    array([-1.20958718e+00,  1.65204470e-01, -1.31085277e+00, ...])


References
--------------------------------------------------------------------------------

  - [CS 287: Gaussians, in Advanced Robotics by Pieter Abbeel](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/Gaussians.pdf)
