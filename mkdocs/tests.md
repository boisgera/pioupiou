
Misc API Tests 
================================================================================

**Warning:** the interface is unstable


    >>> from pioupiou import *
    >>> import pioupiou as pp
    >>> import numpy as np

Random Variables
--------------------------------------------------------------------------------



The universe
--------------------------------------------------------------------------------

A random variable 

    >>> restart()
    >>> U = Uniform(0.0, 1.0)
    >>> omega = Omega()
    >>> u = U(omega)
    >>> u
    0.6369616873214543

    >>> omega = Omega()
    >>> u = U(omega)
    >>> u
    0.2697867137638703

The universe is literally the source of the randomness of every variable :
sample `Universe` to get an `omega` and use it as an argument of a random
variable.
Once you have create a random variable, you can sample the universe
to get an `omega` 

    >>> restart()
    >>> U = Uniform(0.0, 1.0)
    >>> omega = Omega()
    >>> u = U(omega)
    >>> u
    0.6369616873214543

--------------------------------------------------------------------------------

    >>> restore()
    >>> U1 = Uniform(0.0, 1.0)
    >>> omega = Omega(10)
    >>> for u1 in U1(omega):
    ...     print(u1)
    0.6369616873214543
    0.2697867137638703
    0.04097352393619469
    0.016527635528529094
    0.8132702392002724
    0.9127555772777217
    0.6066357757671799
    0.7294965609839984
    0.5436249914654229
    0.9350724237877682

    >>> restore()
    >>> U2 = Uniform(0.0, U1)
    >>> omega = Omega(10)
    >>> for u2 in U2(omega):
    ...     print(u2)
    0.40572019111539415
    0.0727848709235085
    0.0016788296637499191
    0.0002731627361638972
    0.6614084819688684
    0.833122743851587
    0.3680069644406481
    0.5321652324874805
    0.2955281313457811
    0.8743604377283316

    >>> restore()
    >>> N = Normal(1.5, 2.7)
    >>> ns = N(Omega(10000))
    >>> print("mean:", np.mean(ns))  
    mean: 1.4950310577047152
    >>> print("std dev:", np.std(ns))
    std dev: 2.705182786283677

    >>> restore()
    >>> X, Y, Z = Uniform(), Uniform(1.0, 2.0), Normal()
    >>> print("dimension of the universe:", Omega.n)
    dimension of the universe: 3

    >>> restore()
    >>> U1 = Uniform()
    >>> U2 = Uniform(1.0, 2.0)
    >>> @function
    ... def add(x, y):
    ...     return x + y
    >>> X = add(U1, U2)
    >>> omega = Omega(10)
    >>> X(omega)
    array([2.45281524, 1.27252521, 1.8983778 , 1.05011321, 2.54292569,
           2.0884112 , 2.4698147 , 2.27095778, 1.84333688, 2.35775964])
    
    >>> @function
    ... def substract(x, y):
    ...     return x - y
    >>> Z = substract(X, X)
    >>> omega = Omega(10)
    >>> Z(omega)
    array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

    >>> restore()
    >>> print(exp(1.0))
    2.718281828459045
    >>> N1 = Normal(1.0, 0.001)
    >>> X = exp(N1)
    >>> omega = Omega(10)
    >>> X(omega)
    array([2.71923434, 2.71661479, 2.71355749, 2.71249422, 2.72070221,
           2.72197555, 2.71901739, 2.719944  , 2.71857969, 2.72240226])

    >>> restore()
    >>> N1 = Normal(1.0, 0.01)
    >>> N2 = Normal(2.0, 0.02)
    >>> X = N1 + N2
    >>> omega = Omega(10)
    >>> X(omega)
    array([3.02149701, 2.93831437, 3.00397961, 2.94207534, 3.02113554,
           2.99493823, 3.02459988, 3.00819522, 2.99059112, 3.01124626])

    >>> restore()
    >>> U1 = Uniform()
    >>> X = U1 + 1.0
    >>> Y = 1.0 + U1
    >>> Z = + (X * Y)
    >>> W = - Z
    >>> omega = Omega(10)
    >>> X(omega)
    array([1.63696169, 1.26978671, 1.04097352, 1.01652764, 1.81327024,
           1.91275558, 1.60663578, 1.72949656, 1.54362499, 1.93507242])
    >>> Y(omega)
    array([1.63696169, 1.26978671, 1.04097352, 1.01652764, 1.81327024,
           1.91275558, 1.60663578, 1.72949656, 1.54362499, 1.93507242])
    >>> Z(omega)
    array([2.67964357, 1.6123583 , 1.08362588, 1.03332843, 3.28794896,
           3.6586339 , 2.58127852, 2.99115835, 2.38277811, 3.74450529])
    >>> W(omega)
    array([-2.67964357, -1.6123583 , -1.08362588, -1.03332843, -3.28794896,
           -3.6586339 , -2.58127852, -2.99115835, -2.38277811, -3.74450529])

    >>> pp.restart()
    >>> U = pp.Uniform()
    >>> import builtins
    >>> V = builtins.bool(U) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: ...
    >>> V = pp.bool(U)

    >>> restore()
    >>> U1 = Uniform()
    >>> B = (U1 >= 1/3)
    >>> omega = Omega(10)
    >>> B(omega) # doctest: +NORMALIZE_WHITESPACE
    array([ True, False, False, False, True, True, True, True, True, True])

    >>> pp.restart()
    >>> U, C = Uniform(), Constant(1.0)
    >>> T1 = (U <= 1.0)
    >>> T2 = (1.0 < U)
    >>> T3 = (U <= C)
    >>> T4 = (U < 1.0)
    >>> T5 = (1.0 <= U)
    >>> omega = Omega()
    >>> T1(omega)
    True
    >>> T1(omega) == (not T2(omega))
    True
    >>> T1(omega) == T3(omega)
    True
    >>> T4(omega) == (not T5(omega))
    True

    >>> pp.restart()
    >>> X, Y = Uniform(), Uniform()
    >>> W = (X == Y)
    >>> Z = (X != Y) 
    >>> omega = Omega()
    >>> X(omega), Y(omega)
    (0.6369616873214543, 0.2697867137638703)
    >>> W(omega), Z(omega)
    (False, True)
    >>> W(omega) != Z(omega)
    True



Operators
--------------------------------------------------------------------------------

    >>> import pioupiou as pp; pp.restart()

    >>> X, Y, Z = pp.Constant(1.0), pp.Constant(2.0), pp.Constant(4.0)
    >>> omega = Omega()

    >>> (X + Y)(omega)
    3.0
    >>> (X + 2.0)(omega)
    3.0
    >>> (2.0 + X)(omega)
    3.0

    >>> (X - Y)(omega)
    -1.0
    >>> (X - 2.0)(omega)
    -1.0
    >>> (2.0 - X)(omega)
    1.0

    >>> (Y * Z)(omega)
    8.0
    >>> (Y * 4.0)(omega)
    8.0
    >>> (4.0 * Y)(omega)
    8.0

    >>> (X / Y)(omega)
    0.5
    >>> (X / 2.0)(omega)
    0.5
    >>> (1.0 / Y)(omega)
    0.5

    >>> (Constant(5.0) // Constant(2.0))(omega)
    2.0
    >>> (5.0 // Constant(2.0))(omega)
    2.0
    >>> (5.0 // Constant(2.0))(omega)
    2.0

Universe reboot & restore
--------------------------------------------------------------------------------

    >>> import pioupiou as pp; pp.restart()
    >>> U = pp.Uniform()
    >>> omega = pp.Omega()
    >>> x1 = U(omega)
    >>> state = pp.save()
    >>> omega = pp.Omega()
    >>> x2 = U(omega)
    >>> pp.restart(state)
    >>> x3 = U(omega)
    >>> x2 == x3
    True
    
Distributions
--------------------------------------------------------------------------------

### Bernoulli

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

### Uniform

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

### Normal

    >>> pp.restart()
    >>> N = pp.Normal()
    >>> omega = pp.Omega()
    >>> N(omega)
    0.3503492272565639

    >>> pp.restart()
    >>> N = pp.Normal(0.0, 1.0)
    >>> omega = pp.Omega()
    >>> N(omega)
    0.3503492272565639

    >>> pp.restart()
    >>> N = pp.Normal(1.0, 0.1)
    >>> omega = Omega(1000)
    >>> n = N(omega)
    >>> n # doctest: +ELLIPSIS
    array([1.03503492, 0.93865418, 0.82605011, ..., 0.969454  ])
    >>> np.mean(n)
    1.004904221840834
    >>> np.std(n)
    0.09904019518744091

### Exponential

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

### Cauchy

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

Constants
--------------------------------------------------------------------------------

    >>> import pioupiou as pp; pp.restart()

Constant distributions :

    >>> C = Constant(np.pi)
    >>> omega = Omega()
    >>> C(omega)
    3.141592653589793

Yes, you can randomize a constant random variable ! 😀
This is a bit silly, but since we want to be able to randomize all distribution
parameters, it is the most consistent choice.

    >>> X = pp.Uniform()
    >>> C = Constant(X)
    >>> omega = Omega()
    >>> X(omega) == C(omega)
    True


Vectorization
--------------------------------------------------------------------------------

Pioupiou supports vectors (NumPy arrays) of (independent) samples :

    >>> pp.restart()

A call to `Omega` without arguments generate a single sample `omega`.

    >>> X = pp.Uniform()
    >>> omega = pp.Omega()
    >>> X(omega)
    0.6369616873214543

With an integer size instead, you get one-dimensional arrays of samples :

    >>> omega = pp.Omega(1)
    >>> X(omega)
    array([0.26978671])
    >>> omega = pp.Omega(2)
    >>> X(omega)
    array([0.04097352, 0.01652764])

Arbitrary shapes are possible with a tuple size :

    >>> omega = pp.Omega((2,))
    >>> X(omega)
    array([0.81327024, 0.91275558])
    >>> omega = pp.Omega((2,3))
    >>> X(omega)
    array([[0.60663578, 0.72949656, 0.54362499],
           [0.93507242, 0.81585355, 0.0027385 ]])


🎉 Randomize Everything!
--------------------------------------------------------------------------------

Constants, random variables, functions, etc.

    >>> pp.restart()

The `randomize` function turns constant values into (constant) random variables :

    >>> c = 1.0
    >>> C = randomize(1.0)
    >>> omega = Omega()
    >>> C(omega) == c
    True

Obviously, randomizing a random variable doesn't do anything :

    >>> U = Uniform()
    >>> X = randomize(U)
    >>> omega = Omega()
    >>> X(omega) == U(omega)
    True

Randomizing a function makes it able to take random variables as inputs ;
it then produces a random variable :

    >>> @randomize
    ... def sum(x, c):
    ...     return x + c
    >>> Y = sum(X, C)
    >>> omega = Omega()
    >>> Y(omega) == X(omega) + C(omega)
    True

The randomized function can still accept fixed (non-random) values 
or even a mix of deterministic and random values :

    >>> sum(1.0, 2.0) 
    3.0
    >>> Z = sum(X, 2.0)
    >>> omega = Omega()
    >>> Z(omega) == X(omega) + 2.0
    True


### Randomization meets Vectorization

If you want to keep pioupiou happy and working for you, only randomize functions 
that accept NumPy arrays (of consistent sizes). If your function doesn't do that
by default, use the `vectorize` decorator provided by NumPy before you 
randomize them. 🐥 Please !

    >>> pp.restart()
    >>> X, Y = pp.Uniform(), pp.Uniform()

So don't do

    >>> @pp.randomize
    ... def max(x, y):
    ...     if x <= y:
    ...         return y
    ...     else:
    ...         return x
    >>> Z = max(X, Y)

unless you want to break everything :

    >>> omega = pp.Omega()
    >>> Z(omega)
    0.6369616873214543
    >>> omega = pp.Omega(10)
    >>> Z(omega) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: ...

But instead do :

    >>> pp.restart()
    >>> X, Y = pp.Uniform(), pp.Uniform()
    >>> import numpy as np
    >>> @pp.randomize
    ... @np.vectorize
    ... def max(x, y):
    ...     if x <= y:
    ...         return y
    ...     else:
    ...         return x
    >>> Z = max(X, Y)


It will work as expected :

    >>> omega = pp.Omega(10)
    >>> X(omega)
    array([0.63696169, 0.26978671, 0.04097352, 0.01652764, 0.81327024,
           0.91275558, 0.60663578, 0.72949656, 0.54362499, 0.93507242])
    >>> Y(omega)
    array([0.81585355, 0.0027385 , 0.85740428, 0.03358558, 0.72965545,
           0.17565562, 0.86317892, 0.54146122, 0.29971189, 0.42268722])
    >>> Z(omega)
    array([0.81585355, 0.26978671, 0.85740428, 0.03358558, 0.81327024,
           0.91275558, 0.86317892, 0.72949656, 0.54362499, 0.93507242])
    >>> all(max(X(omega), Y(omega)) == Z(omega))
    True


**TODO:** document somewhere that additional random variables can make the universe
"grow" and make samples of omega obsolete. The safe way to proceed is to 
model EVERYTHING and then to sample (and of course, adding random variables
that depend deterministically on random variables is OK too).

**TODO.** After the randomization of functions that depends deterministically
of their arguments, document the creation of components that inherit from
`RandomVariable` and can grow the universe (do NOT merely depend on their
arguments, but also on some hidden, random source).
