:baby_chick: Pioupiou
================================================================================

[![test](https://github.com/boisgera/pioupiou/actions/workflows/test.yml/badge.svg)](https://github.com/boisgera/pioupiou/actions/workflows/test.yml)
![stage](https://img.shields.io/badge/stage-pre--alpha-red) 

Pioupiou is a nano probabilistic programming language, embedded into Python.

Use it to define probabilistic models :

    >>> import pioupiou as pp
    >>> a, b = 0.5, 1.0
    >>> X = pp.Uniform(0.0, 1.0)
    >>> E = pp.Normal(0.0, 0.1)
    >>> Y = a * X + b + E

and to simulate them :

    >>> n = 1000 # number of samples
    >>> omega = pp.Omega(n)
    >>> x, y = X(omega), Y(omega)
    >>> x # doctest: +ELLIPSIS
    array([6.36961687e-01, 2.69786714e-01, 4.09735239e-02, ..., 3.80007897e-01])
    >>> y # doctest: +ELLIPSIS
    array([1.09588258, 1.22942954, 1.01954509, 0.99213115, ..., 1.14366864])

That's about it! Use this data as you see fit.

![data](https://raw.githubusercontent.com/boisgera/pioupiou/master/images/xy.svg)

Getting started
--------------------------------------------------------------------------------

Install the latest version of pioupiou with:

    $ pip install --upgrade git+https://github.com/boisgera/pioupiou.git
