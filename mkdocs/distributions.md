Distributions
================================================================================

```python
import numpy as np
import pioupiou as pp
```

Bernoulli
--------------------------------------------------------------------------------

    >>> pp.restart()
    >>> B = pp.Bernoulli()
    >>> omega = pp.Omega(5)
    >>> B(omega)
    array([False,  True,  True,  True, False])

    >>> pp.restart()
    >>> B = pp.Bernoulli(0.5)
    >>> omega = pp.Omega(5)
    >>> B(omega)
    array([False,  True,  True,  True, False])

    >>> B = pp.Bernoulli(0.0)
    >>> omega = pp.Omega(5)
    >>> B(omega)
    array([False, False, False, False, False])

    >>> B = pp.Bernoulli(1.0)
    >>> omega = pp.Omega(5)
    >>> B(omega)
    array([ True,  True,  True,  True,  True])

Uniform
--------------------------------------------------------------------------------

    >>> pp.restart()
    >>> U = pp.Uniform()
    >>> omega = pp.Omega()
    >>> U(omega)
    0.6369616873214543

    >>> pp.restart()
    >>> U = pp.Uniform(0.0, 1.0)
    >>> omega = pp.Omega()
    >>> U(omega)
    0.6369616873214543

    >>> U = pp.Uniform(0.9, 1.1)
    >>> omega = pp.Omega()
    >>> U(omega)
    0.908194704787239

```python
```


Normal
--------------------------------------------------------------------------------

    >>> pp.restart()
    >>> N = pp.Normal()
    >>> omega = pp.Omega()
    >>> N(omega)
    0.3503492272565639

    >>> pp.restart()
    >>> N = pp.Normal(0.0, (1.0)**2)
    >>> omega = pp.Omega()
    >>> N(omega)
    0.3503492272565639

    >>> pp.restart()
    >>> N = pp.Normal(1.0, (0.1)**2)
    >>> omega = pp.Omega(1000)
    >>> n = N(omega)
    >>> n # doctest: +ELLIPSIS
    array([1.03503492, 0.93865418, 0.82605011, ..., 0.969454  ])
    >>> np.mean(n)
    1.004904221840834
    >>> np.std(n)
    0.09904019518744091

Exponential
--------------------------------------------------------------------------------

    >>> pp.restart()
    >>> E = pp.Exponential()
    >>> omega = pp.Omega()
    >>> E(omega)
    1.013246905717726

    >>> pp.restart()
    >>> E = pp.Exponential(1.0)
    >>> omega = pp.Omega()
    >>> E(omega)
    1.013246905717726

    >>> pp.restart()
    >>> E = pp.Exponential(2.0)
    >>> omega = pp.Omega(1000)
    >>> np.mean(E(omega))
    0.5170714017411246

Cauchy
--------------------------------------------------------------------------------

    >>> pp.restart()
    >>> C = pp.Cauchy()
    >>> omega = pp.Omega()
    >>> C(omega)
    0.4589573340936978
    
    >>> pp.restart()
    >>> C = pp.Cauchy(0.0, 1.0)
    >>> omega = pp.Omega()
    >>> C(omega)
    0.4589573340936978

    >>> pp.restart()
    >>> C = pp.Cauchy(3.0, 2.0)
    >>> omega = pp.Omega(1000)
    >>> np.median(C(omega))    
    3.181434516919701
