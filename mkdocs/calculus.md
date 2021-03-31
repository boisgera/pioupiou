Calculus
================================================================================

```python
import pioupiou as pp
```

Custom Functions
--------------------------------------------------------------------------------

```python
pp.restart()
U1 = pp.Uniform()
U2 = pp.Uniform(1.0, 2.0)
@pp.randomize
def add(x, y):
    return x + y

X = add(U1, U2)
```

```python
>>> omega = pp.Omega(10)
>>> X(omega)
array([2.45281524, 1.27252521, 1.8983778 , 1.05011321, 2.54292569,
       2.0884112 , 2.4698147 , 2.27095778, 1.84333688, 2.35775964])
```

```python
@pp.randomize
def substract(x, y):
    return x - y

Z = substract(X, X)
```

```python
>>> omega = pp.Omega(10)
>>> Z(omega)
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```

```python
>>> pp.restart()
>>> print(pp.exp(1.0))
2.718281828459045
>>> N1 = pp.Normal(1.0, (0.001)**2)
>>> X = pp.exp(N1)
```

```python
>>> omega = pp.Omega(10)
>>> X(omega)
array([2.71923434, 2.71661479, 2.71355749, 2.71249422, 2.72070221,
       2.72197555, 2.71901739, 2.719944  , 2.71857969, 2.72240226])
```

```python
pp.restart()
N1 = pp.Normal(1.0, (0.01)**2)
N2 = pp.Normal(2.0, (0.02)**2)
X = N1 + N2
```

```python
>>> omega = pp.Omega(10)
>>> X(omega)
array([3.02149701, 2.93831437, 3.00397961, 2.94207534, 3.02113554,
       2.99493823, 3.02459988, 3.00819522, 2.99059112, 3.01124626])
```

```python
pp.restart()
U1 = pp.Uniform()
X = U1 + 1.0
Y = 1.0 + U1
Z = + (X * Y)
W = - Z
```

```python
>>> omega = pp.Omega(10)
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
```

```python
>>> pp.restart()
>>> U = pp.Uniform()
>>> import builtins
>>> V = builtins.bool(U) # doctest: +ELLIPSIS
Traceback (most recent call last):
...
TypeError: ...
>>> V = pp.bool(U)
```

```python
pp.restart()
U1 = pp.Uniform()
B = (U1 >= 1/3)
```

```python
>>> omega = pp.Omega(10)
>>> B(omega) # doctest: +NORMALIZE_WHITESPACE
array([ True, False, False, False, True, True, True, True, True, True])
```

```python
pp.restart()
U, C = pp.Uniform(), pp.Constant(1.0)
T1 = (U <= 1.0)
T2 = (1.0 < U)
T3 = (U <= C)
T4 = (U < 1.0)
T5 = (1.0 <= U)
```

```python
>>> omega = pp.Omega()
>>> T1(omega)
True
>>> T1(omega) == (not T2(omega))
True
>>> T1(omega) == T3(omega)
True
>>> T4(omega) == (not T5(omega))
True
```

```python
pp.restart()
X, Y = pp.Uniform(), pp.Uniform()
W = (X == Y)
Z = (X != Y) 
```

```python
>>> omega = pp.Omega()
>>> X(omega), Y(omega)
(0.6369616873214543, 0.2697867137638703)
>>> W(omega), Z(omega)
(False, True)
>>> W(omega) != Z(omega)
True
```

Operators
--------------------------------------------------------------------------------

```python
pp.restart()
X, Y, Z = pp.Constant(1.0), pp.Constant(2.0), pp.Constant(4.0)
```

```python
>>> omega = pp.Omega()
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
>>> (pp.Constant(5.0) // pp.Constant(2.0))(omega)
2.0
>>> (5.0 // pp.Constant(2.0))(omega)
2.0
>>> (5.0 // pp.Constant(2.0))(omega)
2.0
```