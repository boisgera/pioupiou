Distributions
================================================================================

```python
import pioupiou as pp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

Bernoulli
--------------------------------------------------------------------------------

The snippet `B = pp.Bernoulli(p)` instantiates a random boolean variable $B$ such that

$$
\begin{array}{lcl}
\mathbb{P}(B = \mathrm{true}) &=& p \\
\mathbb{P}(B = \mathrm{false}) &=& 1-p \\
\end{array}
$$


```python
>>> pp.restart()
>>> B = pp.Bernoulli(0.5)
>>> omega = pp.Omega(10)
>>> b = B(omega)
>>> b # doctest: +NORMALIZE_WHITESPACE
array([False,  True,  True,  True, False, False, False, False, False, False])
```

The parameter `p` is optional; its default value is `0.5`. 
Thus `B = Bernoulli()` is equivalent to `B = Bernoulli(0.5)`.

```python
>>> pp.restart()
>>> B = pp.Bernoulli()
>>> omega = pp.Omega(10)
>>> all(b == B(omega))
True
```

With `p=0.0` or `p=1.0` you will get almost surely `False` and `True`
respectively.

```python
>>> B = pp.Bernoulli(0.0)
>>> omega = pp.Omega(100)
>>> all(B(omega) == False)
True
```

```python
>>> B = pp.Bernoulli(1.0)
>>> omega = pp.Omega(10)
>>> all(B(omega) == True)
True
```

With a larger number of independent samples, we can check these probabilities 
in a histogram
```python
pp.restart()
B0, B1 = pp.Bernoulli(0.0), pp.Bernoulli(0.25)
B2, B3 = pp.Bernoulli(0.5), pp.Bernoulli()
omega = pp.Omega(100000)
b0, b1, b2, b3 = B0(omega), B1(omega), B2(omega), B3(omega)
data = [["Bernoulli(0.0)", v] for v in b0] + \
       [["Bernoulli(0.25)", v] for v in b1] + \
       [["Bernoulli(0.5)", v] for v in b2] + \
       [["Bernoulli()", v] for v in b3]
df = pd.DataFrame(data, columns=["Distribution", "Value"])
ax = sns.histplot(
    data=df,  
    x="Value", 
    hue="Distribution",
    stat="probability", 
    common_norm=False, 
    multiple="dodge", 
    discrete=True, 
    shrink=0.5
)
yticks = plt.yticks([0.0, 0.25, 0.5, 0.75, 1.0])
xticks = plt.xticks([0, 1], ["False", "True"])
text = plt.title("Bernoulli Distribution")
plt.savefig("bernoulli.svg")
```

![](images/bernoulli.svg)

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


```python
pp.restart()
E0 = pp.Exponential(0.5)
E1 = pp.Exponential(1.0)
E2 = pp.Exponential(2.0)
omega = pp.Omega(10000)
e0, e1, e2 = E0(omega), E1(omega), E2(omega)

_  = sns.histplot(
        {"Exponential(0.5)": e0, 
         "Exponential(1.0)": e1, 
         "Exponential(2.0)": e2}, 
        stat="density", common_norm=False,
        element="step"
       )
_ = plt.xlim(0.0, 5.0)
_ = plt.title("Exponential Distribution")
plt.gcf().subplots_adjust(top=0.95)
plt.savefig("exponential.svg")
```

![](images/exponential.svg)

Cauchy
--------------------------------------------------------------------------------

`Cauchy(x0=0.0, gamma=1.0)` generates a random variable with density
$$
f(x) = \frac{1}{\pi \gamma} \frac{\gamma^2}{(x-x_0)^2 + \gamma^2}.
$$

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

```python
plt.close(); pp.restart()
C = pp.Cauchy()
omega = pp.Omega(100000)
c = C(omega)
_  = sns.histplot(
        {"Cauchy()": c}, 
        stat="density",
        bins=[-1e9] + list(np.linspace(-5, 5, 10*5+1)) + [1e9],
        element="step"
        )
_ = plt.xlim(-5.0, 5.0)
_ = plt.title("Cauchy Distribution")
plt.gcf().subplots_adjust(top=0.95)
plt.savefig("cauchy-1.svg")
```

![](images/cauchy-1.svg)


```python
plt.close(); pp.restart()
C0, C1, C2 = pp.Cauchy(0.0, 1.0), pp.Cauchy(-2.0, 1.0), pp.Cauchy(2.0, 2.0)
omega = pp.Omega(100000)
c0, c1, c2 = C0(omega), C1(omega), C2(omega)
_  = sns.histplot(
        {"Cauchy( 0.0, 1.0)": c0,
         "Cauchy(-2.0, 1.0)": c1,
         "Cauchy(2.0, 2.0)": c2}, 
        stat="density", common_norm=False,
        bins=[-1e9] + list(np.linspace(-5, 5, 10*5+1)) + [1e9],
        element="step")
_ = plt.xlim(-5.0, 5.0)
_ = plt.title("Cauchy Distribution")
plt.gcf().subplots_adjust(top=0.95)
plt.savefig("cauchy-2.svg")
```


![](images/cauchy-2.svg)