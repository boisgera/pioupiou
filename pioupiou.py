import numpy as np
import numpy.random as npr
import scipy.special as ss

class Universe: # actually, looks like a random VECTOR, the only one in town so far.
    def __init__(self, seed=None, n=0):
        self.seed = seed
        self.rng = npr.default_rng(self.seed)
        self.n = 0
    def __call__(self, u=None):
        if u is not None:
            return u
        else:
            return self.rng.uniform(size=self.n)

U = Universe() # the universe (as long as we sample the variables only once ;
# otherwise the "true" univers is the cartesian product of this one).
    
class RandomVariable:
    def __call__(omega):
        raise NotImplementedError()

# Nota: we could also have a function that would instanciante a Constant
# random variable when the argument is not already random (and return the
# initial random variable). Or even accept that a random variable can be
# plugged into a constant (that would be silly apparently, but actually
# a more consistent interface). The `constant` function would avoid doing
# this of course and use `Constant` only when needed.
class Constant(RandomVariable):
    def __init__(self, value):
        # TODO : check numeric value or throw. NOPE. If random, let go through.
        self.value = value
    def __call__(self, u=None):
        return self.value

class Uniform(RandomVariable):
    def __init__(self, low=0.0, high=1.0):
        self.n = U.n
        U.n += 1
        if not isinstance(low, RandomVariable):
            low = Constant(low)
        if not isinstance(high, RandomVariable):
            high = Constant(high)
        self.low = low
        self.high = high
    def __call__(self, u=None):
        if u is None:
            u = U()
        u_n = u[self.n]
        return self.low(u) * (1 - u_n) + self.high(u) * u_n

class Normal(RandomVariable):
    def __init__(self, mu=0.0, sigma=1.0):
        self.U = Uniform()
        if not isinstance(mu, RandomVariable):
            mu = Constant(mu)
        if not isinstance(sigma, RandomVariable):
            sigma = Constant(sigma)
        self.mu = mu
        self.sigma = sigma
    def __call__(self, omega=None):
        u = self.U(omega)
        return ss.erfinv(2*u - 1) * np.sqrt(2) * self.sigma(omega) + self.mu(omega)

# TODO: support a decorator that transform a function into random var when
# random vars are "plugged" into it. Then use it to monkey-patch most numpy 
# functions ?

# TODO: support operations on random variables : +, -, *, etc.

U1 = Uniform(0.0, 1.0)
for n in range(10):
    print(U1())
print(40*"-")
U2 = Uniform(0.0, U1)
for n in range(10):
    print(U2())
print(40*"-")
g = Normal(1.5, 2.7)
s = [g() for i in range(10000)]
print("mean:", np.mean(s))    
print("std dev:", np.std(s))
print(40*"-")
print("dimension of the universe:", U.n)
