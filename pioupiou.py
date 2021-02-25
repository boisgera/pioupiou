# Python 3 Standard Library
import inspect
import operator

# Third-Party Libraries
import numpy as np
import numpy.random as npr
import scipy.special as ss
import wrapt

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
# Here U is the "universal" random vector, that sums up everything there is
# to know about the universe.
    
# TODO: these functions already exist in the operator module, don't redeclare them.
def __add__(x, y):
    return x + y

def __mul__(x, y):
    return x * y

def __sub__(x, y):
    return x - y

def __rsub__(x, y):
    return y - x

def __div__(x, y):
    return x / y

def __rdiv__(x, y):
    return y / x

def __pos__(x):
    return x

def __neg__(x):
    return - x

def __bool__(x):
    return bool(x)

class RandomVariable:
    def __call__(omega):
        raise NotImplementedError()
    # Binary operators
    def __add__(self, other):
        return function(__add__)(self, other) # wrapped each and every time ? This is ugly.
        # at the moment I can't make it work otherwise. Probably because I don't understand
        # what wrapt is doing, I should probably get rid of it.
        # There is at least one level of nesting I can get rid of (the decoration
        # can be done at class definition time and the result stored in it).
    __radd__ = __add__
    def __sub__(self, other):
        return function(__sub__)(self, other)
    def __rsub__(self, other):
        return function(__rsub__)(self, other)
    def __mul__(self, other):
        return function(__mul__)(self, other)
    __rmul__ = __mul__
    def __div__(self, other):
        return function(__div__)(self, other)
    def __rdiv__(self, other):
        return function(__div__)(self, other)
    # TODO: divmod, pow, lshift, rshift, and, xor, or

    def __lt__(self, other):
        return function(operator.lt)(self, other)
    def __le__(self, other):
        return function(operator.le)(self, other)
    def __eq__(self, other):
        return function(operator.eq)(self, other)
    def __ne__(self, other):
        return function(operator.ne)(self, other)
    def __ge__(self, other):
        return function(operator.ge)(self, other)
    def __gt__(self, other):
        return function(operator.gt)(self, other)

    # Unary operators
    def __neg__(self):
        return function(__neg__)(self)
    def __pos__(self):
        return function(__pos__)(self)
    def __bool__(self):
        return function(__bool__)(self)
    # TODO : abs, invert, complex, int, long, float, oct, hex.

def randomize(value):
    if isinstance(value, RandomVariable):
        return value
    else:
        return Constant(value)

class Constant(RandomVariable):
    def __init__(self, value):
        # Yep, the value of a constant can be randomized too.
        if isinstance(value, RandomVariable): 
            self.rv = value
        else:
            self.rv = lambda u: value
    def __call__(self, u=None):
        return self.rv(u)


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
    def __call__(self, u=None):
        u = self.U(u) # arf, here the abstraction of implementation if U leaks through
        return ss.erfinv(2*u - 1) * np.sqrt(2) * self.sigma(u) + self.mu(u)

@wrapt.decorator
def function(wrapped, instance, args, kwargs):
    # if instance is not None: # Nah, forget about this ATM
    #     args = [instance] + list(args)
    all_args = list(args) + list(kwargs.values())
    if not any(isinstance(arg, RandomVariable) for arg in all_args):
        return wrapped(*args, **kwargs)
    class Deterministic(RandomVariable):
        def __init__ (self, *args, **kwargs): # TODO: I'd like these args and 
            # kwargs to have wrapped signature and be checked against it ...
            # Does it work by default ?
            self.args = [randomize(arg) for arg in args]
            self.kwargs = {k: randomize(v) for k, v in kwargs.items()}
        def __call__(self, u=None):
            u = U(u) # manage u = None
            args_values = [arg(u) for arg in self.args]
            kwargs_values = {k: v(u) for k, v in kwargs.items()}
            return wrapped(*args_values, **kwargs_values)
    return Deterministic(*args, **kwargs)

# TODO: support a decorator that transform a function into random var when
# random vars are "plugged" into it. Then use it to patch most numpy functions ?
for name in dir(np):
    item = getattr(np, name)
    if isinstance(item, np.ufunc):
        globals()[name] = function(item)

# TODO: support operations on random variables : +, -, *, etc.

# @function
# def __add__(x, y):
#     return x + y
# RandomVariable.__add__ = __add__

# ------------------------------------------------------------------------------

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

print(40*"-")
@function
def add(x, y):
    return x + y
X = add(U1, U2)
print([X() for i in range(10)])

@function
def substract(x, y):
    return x - y
Z = substract(X, X)
print([Z() for i in range(10)])

print(40*"-")
print(exp(1.0))
N1 = Normal(1.0, 0.001)
X = exp(N1)
print([X() for i in range(10)])

print(40*"-")
N1 = Normal(1.0, 0.01)
N2 = Normal(2.0, 0.02)
X = N1 + N2
#print(X.__add__)
#print(inspect.signature(X.__add__))
print([X() for i in range(10)])


print(40*"-")
U1 = Uniform()
X = U1 + 1.0
Y = 1.0 + U1
Z = X * Y
#print(X.__add__)
#print(inspect.signature(X.__add__))
print([X() for i in range(10)])
print([Y() for i in range(10)])
print([Z() for i in range(10)])

print(40*"-")
U1 = Uniform()
B = U1 >= 1/3
print([B() for i in range(20)])