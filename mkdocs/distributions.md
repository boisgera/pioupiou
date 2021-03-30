Distributions
================================================================================

```python
import pioupiou as pp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

To streamline the visualization of distributions in this document, we introduce 
a helper function `long_form_data`. It instantiates some distributions,
simulates them and returns the results as a [long-form dataframe](https://seaborn.pydata.org/tutorial/data_structure.html) with column names `"Distribution"` and `"Value"`. 
Its arguments are:

  - `distribs`: strings that should eval to random variables,

  - `n`: number of samples used for the simulation (default: `100000`)

```python
def long_form_data(*distribs, n=100000):
    # Modeling and Simulation
    pp.restart()
    Xs = [eval(distrib) for distrib in distribs] # random variables
    omega = pp.Omega(n)
    xs = [X(omega) for X in Xs]
    # Long-form Data Frame
    data = []
    for distrib, x in zip(distribs, xs):
        data.extend([[distrib, np.float64(value)] for value in x])
    return pd.DataFrame(data, columns=["Distribution", "Value"])
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

For example:
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
>>> omega = pp.Omega(10)
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
df = long_form_data(
    "pp.Bernoulli(0.0)", 
    "pp.Bernoulli(0.25)", 
    "pp.Bernoulli(0.5)", 
    "pp.Bernoulli()"
)

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
title = plt.title("Bernoulli Distribution")
plt.savefig("bernoulli.svg")
plt.close()
```

![](images/bernoulli.svg)

Binomial
--------------------------------------------------------------------------------

When $n \in \mathbb{N}$ and $p \in [0,1]$,
the code `B = pp.Binomial(n, p)` instantiates a random variable $B$ with
probability mass function
$$
f(k) 
= 
\left( 
\begin{array}{c} 
n \\\\ k 
\end{array} 
\right) p^k (1-p)^{n-k}
$$
for $k \in \{0,n\}$ and $f(k)=0$ otherwise.
The parameter $p$ has a default value of $0.5$.

```python
df = long_form_data(
    "pp.Binomial(5      )", 
    "pp.Binomial(5, 0.5 )",
    "pp.Binomial(5, 0.25)",
    "pp.Binomial(5, 0.75)", 
)

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
yticks = plt.yticks([0.0, 0.125, 0.25, 0.375, 0.5])
title = plt.title("Binomial Distribution")
plt.savefig("binomial.svg")
plt.close()
```

![](images/binomial.svg)

Poisson
--------------------------------------------------------------------------------

The code `pp.Poisson(lambda_)` creates 
a random variable with probability mass function
$$
f(k) 
= 
\lambda^k \frac{e^{-\lambda}}{k!}, \; k \in \mathbb{N}
$$
and $f(k)=0$ otherwise. The parameter $\lambda$ should be
real and positive.

```python
df = long_form_data(
    "pp.Poisson(1.0)", 
    "pp.Poisson(2.0)",
    "pp.Poisson(4.0)",
    "pp.Binomial(100, 0.04)"
)

ax = sns.histplot(
    data=df,  
    x="Value", 
    hue="Distribution",
    stat="probability", 
    common_norm=False, 
    multiple="dodge", 
    discrete=True, 
    shrink=0.8
)
xlim = plt.xlim(-1.0, 11.0)
title = plt.title("Poisson Distribution")
plt.savefig("poisson.svg")
plt.close()
```

![](images/poisson.svg)

Uniform
--------------------------------------------------------------------------------

When `a < b`, the snippet `U = pp.Uniform(a, b)` creates a random variable $U$ 
with density
$$
f(x) = \frac{1}{b-a} \; \mbox{ if } \; a \leq x \leq b, 
$$
and $f(x)= 0$ otherwise. The default value of `a` is `0.0` and the default value
of `b` is 1.0, thus `U = pp.Uniform()` is equivalent to `U = pp.Uniform(0,1)`.

For example

```python
>>> pp.restart()
>>> U = pp.Uniform()
>>> omega = pp.Omega()
>>> U(omega)
0.6369616873214543
```

is equivalent to

```python
>>> pp.restart()
>>> U = pp.Uniform(0.0, 1.0)
>>> omega = pp.Omega()
>>> U(omega)
0.6369616873214543
```

We are almost sure that values sampled from `U = pp.Uniform(a, b)` are
between `a` and `b`:

```python
>>> pp.restart()
>>> a, b = -3, 7
>>> U = pp.Uniform(a, b)
>>> omega = pp.Omega(1000)
>>> all(a <= U(omega)) and all(U(omega) <= b)
True
```

Let's visualize some examples of the uniform distribution
```python
df = long_form_data(
    "pp.Uniform(-1.5, -1.0)",
    "pp.Uniform( 0.0,  1.0)",
    "pp.Uniform( 2.0,  4.0)"
)

ax = sns.histplot(
    data=df,  
    x="Value", 
    hue="Distribution",
    stat="density", 
    bins = np.arange(-2.0, 4.5, 0.25),
    common_norm=False, 
)
xticks = plt.xticks(np.arange(-2.0, 4.5, 1.0))
title = plt.title("Uniform Distribution")
plt.savefig("uniform.svg")
plt.close()
```

![](images/uniform.svg)

Normal
--------------------------------------------------------------------------------

The snippet `N = pp.Normal(mu, sigma**2)` creates a random variable $N$ with density
$$
f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
$$

The default values of `mu` and `sigma**2` are `0.0` and `1.0`:

```python
>>> pp.restart()
>>> N = pp.Normal()
>>> omega = pp.Omega()
>>> N(omega)
0.3503492272565639
```

```python
>>> pp.restart()
>>> N = pp.Normal(0.0, 1.0)
>>> omega = pp.Omega()
>>> N(omega)
0.3503492272565639
```


The parameters $\mu \in \mathbb{R}$ and $\sigma > 0$ are the mean and standard 
deviation of the random variable:

```python
>>> pp.restart()
>>> N = pp.Normal(1.0, (0.1)**2)
>>> omega = pp.Omega(100000)
>>> n = N(omega)
>>> n # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
array([1.03503492, 0.93865418, 0.82605011, ..., 1.00156987])
>>> np.mean(n)
0.9998490788460421
>>> np.std(n)
0.09990891658278829
```

Let's visualize some normal distributions:

```python
df = long_form_data(
    "pp.Normal( 0.0, 1.0)", 
    "pp.Normal(-2.0, 1.0)", 
    "pp.Normal( 2.0, 2.0)"
)

ax = sns.histplot(
    data=df,  
    x="Value", 
    hue="Distribution",
    stat="density", common_norm=False,
    bins=[-1e9] + list(np.linspace(-5, 5, 10*5+1)) + [1e9],
    element="step"
)
xlim = plt.xlim(-5.0, 5.0)
title = plt.title("Normal Distribution")
plt.savefig("normal.svg")
plt.close()
```

![](images/normal.svg)

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
df = long_form_data(
    "pp.Exponential(0.5)",
    "pp.Exponential(1.0)",
    "pp.Exponential(2.0)"
)

ax = sns.histplot(
    data=df,  
    x="Value", 
    hue="Distribution",
    stat="density", 
    common_norm=False,
    element="step"
)
xlim = plt.xlim(0.0, 5.0)
title = plt.title("Exponential Distribution")
plt.savefig("exponential.svg")
plt.close()
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
df = long_form_data(
    "pp.Cauchy( 0.0, 1.0)", 
    "pp.Cauchy(-2.0, 1.0)", 
    "pp.Cauchy( 2.0, 2.0)"
)

ax = sns.histplot(
    data=df,  
    x="Value", 
    hue="Distribution",
    stat="density", common_norm=False,
    bins=[-1e9] + list(np.linspace(-5, 5, 10*5+1)) + [1e9],
    element="step"
)
xlim = plt.xlim(-5.0, 5.0)
title = plt.title("Cauchy Distribution")
plt.savefig("cauchy.svg")
plt.close()
```

![](images/cauchy.svg)

Student
--------------------------------------------------------------------------------

```python
df = long_form_data(
    "pp.t(0.1)",
    "pp.t(1.0)", 
    "pp.t(10.0)", 
    "pp.Normal(0.0, 1.0)"
)

ax = sns.histplot(
    data=df,  x="Value", hue="Distribution",
    stat="density", common_norm=False, 
    bins=[-1e9] + list(np.linspace(-5, 5, 10*5+1)) + [1e9],
    element="step", fill=False,
)
xlim = plt.xlim(-5.0, 5.0)
title = plt.title("Student t Distribution")
plt.savefig("student-t.svg")
plt.close()
```

![](images/student-t.svg)


Beta
--------------------------------------------------------------------------------

```python
df = long_form_data(
    "pp.Beta(0.5, 0.5)",
    "pp.Beta(5.0, 1.0)",
    "pp.Beta(1.0, 3.0)",
    "pp.Beta(2.0, 2.0)",
    "pp.Beta(2.0, 5.0)"
)

ax = sns.histplot(
    data=df,  
    x="Value", 
    hue="Distribution",
    stat="density", 
    common_norm=False,
    element="step",
    fill=False
)
xlim = plt.xlim(0.0, 1.0)
ylim = plt.ylim(0.0, 4.0)
title = plt.title("Beta Distribution")
plt.savefig("beta.svg")
plt.close()
```

![](images/beta.svg)
