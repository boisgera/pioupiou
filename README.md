Pioupiou
================================================================================

[![test](https://github.com/boisgera/pioupiou/actions/workflows/test.yml/badge.svg)](https://github.com/boisgera/pioupiou/actions/workflows/test.yml)

    >>> import numpy as np
    >>> from pioupiou import *

The universe
--------------------------------------------------------------------------------

A random variable 

    >>> U = Uniform(0.0, 1.0)
    >>> u = U()
    >>> u
    0.6369616873214543

    >>> u = U()
    >>> u
    0.2697867137638703

The universe is literally the source of the randomness of every variable :
sample `Universe` to get an `omega` and use it as an argument of a random
variable.
Once you have create a random variable, you can sample the universe
to get an `omega` 

    >>> Universe.restart()
    >>> omega = Universe()
    >>> u = U(omega)
    >>> u
    0.6369616873214543

--------------------------------------------------------------------------------

    >>> Universe.restart()
    >>> U1 = Uniform(0.0, 1.0)
    >>> for n in range(10):
    ...     print(U1())
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

    >>> Universe.restart()
    >>> U2 = Uniform(0.0, U1)
    >>> for n in range(10):
    ...     print(U2())
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

    >>> Universe.restart()
    >>> N = Normal(1.5, 2.7)
    >>> s = [N() for i in range(10000)]
    >>> print("mean:", np.mean(s))  
    mean: 1.4950310577047152
    >>> print("std dev:", np.std(s))
    std dev: 2.705182786283677

    >>> Universe.restart()
    >>> X, Y, Z = Uniform(), Uniform(1.0, 2.0), Normal()
    >>> print("dimension of the universe:", Universe.n)
    dimension of the universe: 3

    >>> Universe.restart()
    >>> U1 = Uniform()
    >>> U2 = Uniform(1.0, 2.0)
    >>> @function
    ... def add(x, y):
    ...     return x + y
    >>> X = add(U1, U2)
    >>> print([X() for i in range(10)])
    [1.9067484010853246, 1.057501159464724, 2.7260258164779945, 2.336132336751178, 2.4786974152531913, 1.8185920542916802, 1.8909898518930337, 1.905311067032503, 2.4046401425989785, 1.7223991117350432]
    >>> @function
    ... def substract(x, y):
    ...     return x - y
    >>> Z = substract(X, X)
    >>> print([Z() for i in range(10)])
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    >>> Universe.restart()
    >>> print(exp(1.0))
    2.718281828459045
    >>> N1 = Normal(1.0, 0.001)
    >>> X = exp(N1)
    >>> print([X() for i in range(10)])
    [2.7192343432437776, 2.7166147876215536, 2.713557490426163, 2.7124942218733623, 2.7207022084297448, 2.721975546967326, 2.719017389882115, 2.719943997947149, 2.718579688242829, 2.7224022572035995]

    >>> Universe.restart()
    >>> N1 = Normal(1.0, 0.01)
    >>> N2 = Normal(2.0, 0.02)
    >>> X = N1 + N2
    >>> print([X() for i in range(10)])
    [2.991234328698495, 2.939976784719813, 3.036058532707301, 3.0149314353211336, 3.031389171415428, 2.9534457078177256, 2.974076754815227, 2.9874767340828736, 3.013029448690265, 2.9908472339825285]

    >>> Universe.restart()
    >>> U1 = Uniform()
    >>> X = U1 + 1.0
    >>> Y = 1.0 + U1
    >>> Z = X * Y
    >>> print([X() for i in range(10)])
    [1.6369616873214543, 1.2697867137638703, 1.0409735239361946, 1.016527635528529, 1.8132702392002724, 1.9127555772777218, 1.6066357757671799, 1.7294965609839985, 1.543624991465423, 1.9350724237877683]
    >>> print([Y() for i in range(10)])
    [1.8158535541215322, 1.002738500170148, 1.8574042765875693, 1.0335855753054644, 1.729655446429944, 1.175655620602559, 1.8631789223498867, 1.5414612202490918, 1.2997118905373848, 1.4226872211976584]
    >>> print([Z() for i in range(10)])
    [1.0574413460647132, 1.2640128858165947, 2.7909859349704345, 2.7132332870402167, 2.609469058395303, 1.9145635741681477, 3.9888475276151443, 3.923708639344742, 2.8410517814471183, 2.724015822618484]

    >>> Universe.restart()
    >>> U1 = Uniform()
    >>> B = U1 >= 1/3
    >>> print([B() for i in range(10)])
    [True, False, False, False, True, True, True, True, True, True]