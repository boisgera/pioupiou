# Python 3 Standard Library
import inspect
import operator

# Third-Party Libraries
import numpy as np
import numpy.random as npr
import scipy.special as ss
import wrapt

# We need to support : random init, custom seed it, continuation (save/restore)
# What should be the default ? Init at 0 or None ? I'd rather fo with 0 here,
# right ? And the experts could set the seed to None to get a random init.
# But by default we are deterministic.

class UniverseType: # actually, looks like a random VECTOR, the only one in town so far.
    def __init__(self): 
        self.restart(0)
    def restart(self, seed=0):
        self.ss = np.random.SeedSequence(seed)
        self.rng = npr.default_rng(self.ss)
        self.n = 0
    def save(self):
        return self.ss.entropy
    load = restart
    def __call__(self, omega=None):
        if omega is not None:
            return omega
        else:
            return self.rng.uniform(size=self.n)

Universe = UniverseType() # the universe (as long as we sample the variables only once ;
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
    def __call__(self, omega=None):
        return self.rv(omega)


class Uniform(RandomVariable):
    def __init__(self, low=0.0, high=1.0):
        self.n = Universe.n
        Universe.n += 1
        self.low = randomize(low)
        self.high = randomize(high)
    def __call__(self, omega=None):
        omega = Universe(omega)
        u_n = omega[self.n] # localized abstraction leak HERE.
        return self.low(omega) * (1 - u_n) + self.high(omega) * u_n

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
        mu = self.mu(omega)
        sigma = self.sigma(omega)
        return ss.erfinv(2*u - 1) * np.sqrt(2) * sigma + mu

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
        def __call__(self, omega=None):
            omega = Universe(omega) # manage u = None
            args_values = [arg(omega) for arg in self.args]
            kwargs_values = {k: v(omega) for k, v in kwargs.items()}
            return wrapped(*args_values, **kwargs_values)
    return Deterministic(*args, **kwargs)

for name in dir(np):
    item = getattr(np, name)
    if isinstance(item, np.ufunc):
        globals()[name] = function(item)
