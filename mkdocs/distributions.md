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
# Model and Simulation
pp.restart()
distribs = [
    "pp.Bernoulli(0.0)", 
    "pp.Bernoulli(0.25)", 
    "pp.Bernoulli(0.5)", 
    "pp.Bernoulli()"
]
Xs = [eval(distrib) for distrib in distribs]
omega = pp.Omega(100000)
xs = [X(omega) for X in Xs]

# Data Frame (long-form)
data = []
for distrib, x in zip(distribs, xs):
    data.extend([[distrib, int(value)] for value in x])

df = pd.DataFrame(data, columns=["Distribution", "Value"])

# Visualization
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

Uniform
--------------------------------------------------------------------------------

When `a < b`, the snippet `U = pp.Uniform(a, b)` creates a random variable $U$ 
with density
$$
f(x) = \frac{1}{b-a} \; \mbox{ if } \; a \leq x \leq b, 
$$
and $f(x)= 0$ otherwise. The default value of `a` is `0.0` and the default value
of `b` is 1.0, this `U = pp.Uniform()` is equivalent to `U = pp.Uniform(0,1)`.

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
# Model and Simulation
pp.restart()
distribs = [
    "pp.Uniform(-1.5, -1.0)",
    "pp.Uniform( 0.0,  1.0)",
    "pp.Uniform( 2.0,  4.0)"
]
Xs = [eval(distrib) for distrib in distribs]
omega = pp.Omega(100000)
xs = [X(omega) for X in Xs]

# Data Frame (long-form)
data = []
for distrib, x in zip(distribs, xs):
    data.extend([[distrib, value] for value in x])

df = pd.DataFrame(data, columns=["Distribution", "Value"])

# Visualization
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
# Model and Simulation
pp.restart()
distribs = [
    "pp.Exponential(0.5)",
    "pp.Exponential(1.0)",
    "pp.Exponential(2.0)"
]
Xs = [eval(distrib) for distrib in distribs]
omega = pp.Omega(100000)
xs = [X(omega) for X in Xs]

# Data Frame (long-form)
data = []
for distrib, x in zip(distribs, xs):
    data.extend([[distrib, value] for value in x])

df = pd.DataFrame(data, columns=["Distribution", "Value"])

# Visualization
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
pp.restart()
C = pp.Cauchy()
omega = pp.Omega(100000)
c = C(omega)
ax = sns.histplot(
    {"Cauchy()": c}, 
    stat="density",
    bins=[-1e9] + list(np.linspace(-5, 5, 10*5+1)) + [1e9],
    element="step"
)
xlim = plt.xlim(-5.0, 5.0)
title = plt.title("Cauchy Distribution")
plt.gcf().subplots_adjust(top=0.95)
plt.savefig("cauchy-1.svg")
plt.close()
```

![](images/cauchy-1.svg)


```python
# Model and Simulation
pp.restart()
distribs = [
    "pp.Cauchy( 0.0, 1.0)", 
    "pp.Cauchy(-2.0, 1.0)", 
    "pp.Cauchy( 2.0, 2.0)"
]
Xs = [eval(distrib) for distrib in distribs]
omega = pp.Omega(100000)
xs = [X(omega) for X in Xs]

# Data Frame (long-form)
data = []
for distrib, x in zip(distribs, xs):
    data.extend([[distrib, value] for value in x])

df = pd.DataFrame(data, columns=["Distribution", "Value"])

# Visualization
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
plt.gcf().subplots_adjust(top=0.95)
plt.savefig("cauchy-2.svg")
plt.close()
```

![](images/cauchy-2.svg)

Student
--------------------------------------------------------------------------------

```python
# Model and Simulation
pp.restart()
distribs = [
    "pp.t(0.1)",
    "pp.t(1.0)", 
    "pp.t(10.0)", 
    "pp.Normal(0.0, 1.0)"
]
Xs = [eval(distrib) for distrib in distribs]
omega = pp.Omega(100000)
xs = [X(omega) for X in Xs]

# Data Frame (long-form)
data = []
for distrib, x in zip(distribs, xs):
    data.extend([[distrib, value] for value in x])

df = pd.DataFrame(data, columns=["Distribution", "Value"])

# Visualization
ax = sns.histplot(
    data=df,  x="Value", hue="Distribution", hue_order=distribs,
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
