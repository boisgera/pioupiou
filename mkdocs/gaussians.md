Gaussians
================================================================================

![Multivariate gaussians](images/gaussians.svg)

Imports:

```python
    >>> import numpy as np
    >>> import pioupiou as pp; pp.restart()

```

Bivariate Gaussian
--------------------------------------------------------------------------------

```python
    >>> def Normal2(mu1, mu2, Sigma11, Sigma12, Sigma22):
    ...     Sigma21 = Sigma12
    ...     N1 = pp.Normal(mu=mu1, sigma=pp.sqrt(Sigma11))
    ...     mu = mu2 + Sigma21 / Sigma11 * (N1 - mu1)
    ...     sigma = pp.sqrt(Sigma22 - Sigma21 / Sigma22 * Sigma12)
    ...     N2 = pp.Normal(mu, sigma)
    ...     return N1, N2

```

Model
--------------------------------------------------------------------------------

```python
    >>> mu, Sigma = [0.0, 0.0], [[1.0, 0.75], [0.75, 1.0]]
    >>> X, Y = Normal2(mu[0], mu[1], Sigma[0][0], Sigma[0][1], Sigma[1][1])

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

<div class="viz">
```python
data = pd.DataFrame({"x":x, "y": y})
p = sns.jointplot(x="x", y="y", data=data,
                  kind="scatter", alpha=1.0,
                  xlim=(-4.0, 4.0), ylim=(-4.0, 4.0))
p.fig.suptitle("Correlated Gaussian Variables")
p.ax_joint.collections[0].set_alpha(0)
p.fig.tight_layout()
p.fig.subplots_adjust(top=0.95)
plt.savefig("gaussians.svg")
```
</div>



References
--------------------------------------------------------------------------------

  - [Gaussians, in Advanced Robotics (Berkeley CS 287) by Pieter Abbeel](https://people.eecs.berkeley.edu/~pabbeel/cs287-fa12/slides/Gaussians.pdf)
