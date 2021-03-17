The Universe
================================================================================

```python
import pioupiou as pp
```

The Big Bang
--------------------------------------------------------------------------------

You may have noticed that every time I define a new model, the first thing I do
is:

```python
pp.restart()
```

While this action is not mandatory, it serves two purposes:

  - It restores the initial state of pioupou 🐣.    
    All the random variables that you have defined so far become invalid, 
    but since you have reduced the size of your model (to nothing !), 
    future sampling will be less computationally expensive.

  - It ensures a deterministic sampling of your random variables.  
    Import pioupiou, create your model and sample it;
    then restart pioupiou and do it again; 
    you will end up with the same values[^3].

[^3]: You may not appreciate this feature but it is terrific when you are 
    testing models since your execution is repeatable.

### Invalid Random Variables

**TODO.** Ensure programatically that invalid random variables throw an
error when sampled. Then doctest the feature here.

### Deterministic Sampling 

Let's see the deterministic sampling in action.
A model is a collection of random variables:
```python
def make_model():
    X = pp.Uniform(0,1)
    Y = pp.Uniform(0,1)
    Z = X + Y
    return X, Y, Z
```

The first run gives us
```python
>>> pp.restart()
>>> X, Y, Z = make_model()
>>> omega = pp.Omega()
>>> X(omega), Y(omega), Z(omega)
(0.6369616873214543, 0.2697867137638703, 0.9067484010853246)
```

Without a restart, new modeling and sampling steps will (probably) give 
different results:
```python
>>> X, Y, Z = make_model()
>>> omega = pp.Omega()
>>> X(omega), Y(omega), Z(omega)
(0.8132702392002724, 0.9127555772777217, 1.726025816477994)
```

But if we restart pioupiou and recreate the model, we have reproduced the 
original results:
```python
>>> pp.restart()
>>> X, Y, Z = make_model()
>>> omega = pp.Omega()
>>> X(omega), Y(omega), Z(omega)
(0.6369616873214543, 0.2697867137638703, 0.9067484010853246)
```

Universe Structure
--------------------------------------------------------------------------------

!!! warning "Internals"
    This section explains the structure of `omega` in `omega = pp.Omega()`. 
    But this is an implementation detail: you can treat `omega` as an opaque
    object and merely use it to sample your random variables.

In pioupou, all randomness is derived from $n$ primitive random 
variables which are independent and uniformly distributed on 
$[0,1]$. Concretely, that means that every random variable in your model depends deterministically on these $n$ primitive random variables[^1]. The number $n$ itself
depends on the complexity of your model:
every time that you invoke `pp.Uniform()` (directly or indirectly), you
instantiate a new primitive random variable.
The call `pp.Omega()` merely samples these $n$ primitive random variables[^2].

[^1]:
    Your universe is $\Omega = [0,1]^n$ and its probability 
    $\mathbb{P}$ is the Lebesgue measure ; for any measurable set $A \subset [0,1]^n$,
    $$
    \mathbb{P}(A) = \int_{[0,1]^n} 1_A(\omega) \, d\omega.
    $$
    Every random variable is a (measurable) function $X :\Omega \to \mathbb{R}$.
    What we call *primitive* random variables in this context are the $n$ random variables
    $U_1, \dots, U_n$ defined by
    $U_i(\omega_1, \dots, \omega_n) = \omega_i$.
    Thus, for any random variable $X$, we have
    $$
    X(\omega_1, \dots, \omega_n) = X(U_1(\omega_1, \dots, \omega_n), \dots, U_n(\omega_1, \dots, \omega_n)).
    $$
    This proves that any random variable $X$ in this universe 
    depends deterministically on $U_1, \dots, U_n$.

[^2]: Or if you wish, samples the universe $\Omega$.

Let's see how that works. When no model has been defined,
we obviously need zero primitive random variables, thus $n=0$ and
`omega = pp.Omega()` is array of length 0:

```python
>>> pp.restart()
>>> pp.Omega.n
0
>>> omega = pp.Omega()
>>> omega
array([], dtype=float64)
```

If we create a new uniform random variable on $[0,1]$ now $n$ is 1.
```python
>>> U = pp.Uniform()
>>> pp.Omega.n
1
>>> omega = pp.Omega()
>>> omega
array([0.63696169])
```
Guess what? Here $U$ is exactly the first (and only)
primitive random variable:
```python
>>> U(omega)
0.6369616873214543
>>> U(omega) == omega[0]
True
```

Since internally, each call to `pp.Normal()` instantiate a new (independant)
uniform variable on $[0, 1]$, adding an independent normal variable to the model
will increase the number of primitive random variables by one:
```python
>>> N = pp.Normal()
>>> pp.Omega.n
2
>>> omega = pp.Omega()
>>> omega
array([0.26978671, 0.04097352])
```

As usual, this $\omega$ can be used to sample the random variables $U$ and $N$:
```python
>>> U(omega), N(omega)
(0.2697867137638703, -1.739498886765934)
```

Note that if you add to your model a random variable that depends deterministically
on the existing ones, you won't increase the number of primitive random variables.

```python
>>> X = U + N
>>> pp.Omega.n
2
>>> omega = pp.Omega()
>>> omega
array([0.01652764, 0.81327024])
>>> U(omega), N(omega), X(omega)
(0.016527635528529094, 0.8900118529686626, 0.9065394884971917)
```

