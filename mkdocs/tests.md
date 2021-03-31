
Misc API Tests 
================================================================================

**Warning:** this document is a very rough draft.


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

    >>> restart()
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

    >>> restart()
    >>> U1 = Uniform(0.0, 1.0)
    >>> U2 = Uniform(0.0, U1)
    >>> omega = Omega(10)
    >>> for u2 in U2(omega):
    ...     print(u2)
    0.5196674564404565
    0.0007388109615460543
    0.03513087464975646
    0.0005550901476646821
    0.5934070594518621
    0.16033064738516523
    0.5236352151856017
    0.39499409807791175
    0.16293087393547157
    0.395243164429411

    >>> restart()
    >>> N = Normal(1.5, (2.7)**2)
    >>> ns = N(Omega(10000))
    >>> print("mean:", np.mean(ns))  
    mean: 1.4950310577047152
    >>> print("std dev:", np.std(ns))
    std dev: 2.705182786283677
    
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