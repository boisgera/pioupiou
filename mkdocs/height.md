Height
================================================================================

Sources: 

  - [Anthropométrie, Adultes : Tableaux de distribution ENNS](https://www.santepubliquefrance.fr/determinants-de-sante/nutrition-et-activite-physique/articles/enns-etude-nationale-nutrition-sante/anthropometrie-adultes-tableaux-de-distribution-enns)

  - [France - Population, Female (% Of Total)
](https://tradingeconomics.com/france/population-female-percent-of-total-wb-data.html)


Code:

    >>> import numpy as np
    >>> import pioupiou as pp; pp.restart()

Display sex graphically:

    >>> @pp.randomize
    ... @np.vectorize
    ... def sex_symbol(is_female):
    ...     if is_female:
    ...         return "♀"
    ...     else:
    ...         return "♂"

Proportion of females:

    >>> proportion_female = 0.516
    >>> Is_female = pp.Bernoulli(proportion_female)
    >>> Sex_symbol = sex_symbol(Is_female)

    >>> omega = pp.Omega(10)
    >>> sexes = Sex_symbol(omega)
    >>> print("".join(sexes))
    ♂♀♀♀♂♂♂♂♂♂

Distribution of heights, conditionned by the sex:

    >>> mu_female = 161.7
    >>> sigma_female = (175.0 - 149.0) / (2 * 1.96)
    >>> Height_female = pp.Normal(mu_female, sigma_female)
    >>> mu_male = 174.4
    >>> sigma_male = (189.0 - 162.0) / (2 * 1.96)
    >>> Height_male = pp.Normal(mu_male, sigma_male)

Branching:

    >>> @pp.randomize
    ... @np.vectorize
    ... def IF(condition, then_, else_):
    ...     if condition:
    ...         return then_
    ...     else:
    ...         return else_

Combined height:

    >>> Height = IF(Is_female, Height_female, Height_male)
    >>> omega = pp.Omega(10)
    >>> print("".join(Sex_symbol(omega)))
    ♂♀♂♀♂♀♂♂♀♀
    >>> Height_female(omega)
    array([149.05760786, 154.04699223, 164.62923173, 164.20544312,
           163.64590454, 159.73782054, 180.08229688, 175.43831704,
           164.9052502 , 164.2639231 ])
    >>> Height_male(omega)
    array([177.7850035 , 172.45674883, 166.80543598, 178.44496236,
           174.83803853, 170.98942569, 174.15539547, 182.8292959 ,
           184.77709853, 171.89038855])
    >>> Height(omega)
    array([177.7850035 , 154.04699223, 166.80543598, 164.20544312,
           174.83803853, 159.73782054, 174.15539547, 182.8292959 ,
           164.9052502 , 164.2639231 ])
