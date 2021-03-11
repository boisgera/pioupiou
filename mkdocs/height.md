Height
================================================================================


![Height](images/height.svg)



Imports:

```python
import numpy as np
import pioupiou as pp; pp.restart()
```

Models
--------------------------------------------------------------------------------

Sex as a symbol (♀ or ♂), for fun !

```python
def sex_symbol(is_female):
    if is_female:
        return "♀"
    else:
        return "♂"
sex_symbol = pp.randomize(np.vectorize(sex_symbol))
```

Proportion of females in the population:

```python
proportion_female = 0.516
Is_female = pp.Bernoulli(proportion_female)
Sex_symbol = sex_symbol(Is_female)
```

Distribution of heights (sex-dependent):

```python
mu_female = 161.7
sigma_female = (175.0 - 149.0) / (2 * 1.96)
Height_female = pp.Normal(mu_female, sigma_female)
mu_male = 174.4
sigma_male = (189.0 - 162.0) / (2 * 1.96)
Height_male = pp.Normal(mu_male, sigma_male)
```

Combined height:

```python
Is_male = pp.logical_not(Is_female)
Height = Is_female * Height_female + Is_male * Height_male
```

Simulation
--------------------------------------------------------------------------------

Sexes:

```python
>>> omega = pp.Omega(1000)
>>> Sex_symbol(omega) # doctest: +ELLIPSIS
array(['♂', '♀', '♀', '♀', '♂', '♂', '♂', '♂', '♂', '♂', '♂', '♀', ...)
```

Height (sex-dependent):

```python
>>> Height_female(omega) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
array([146.93582968, 167.97025732, 161.63754187, 160.62997627, ...])
>>> Height_male(omega) # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
array([188.17949253, 163.69348513, 183.98172232, 170.37550933, ...])    
```

Combined height:
```python
>>> height = Height(omega)
>>> height # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
array([188.17949253, 167.97025732, 161.63754187, 160.62997627, ...])
```

Visualization
--------------------------------------------------------------------------------

<div class="viz">
```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.DataFrame({"Height [cm]": height})
_  = sns.displot(df, x="Height [cm]", stat="density", kde=True, aspect=16/9)
_ = plt.title("Height Distribution in France")
plt.gcf().subplots_adjust(top=0.95)
plt.savefig("height.svg")
```
</div>

References
--------------------------------------------------------------------------------

  - [Anthropométrie, Adultes : Tableaux de distribution ENNS](https://www.santepubliquefrance.fr/determinants-de-sante/nutrition-et-activite-physique/articles/enns-etude-nationale-nutrition-sante/anthropometrie-adultes-tableaux-de-distribution-enns) (in French)

  - [France - Population, Female (% Of Total)
](https://tradingeconomics.com/france/population-female-percent-of-total-wb-data.html)