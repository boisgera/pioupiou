#!/usr/bin/env python

import seaborn as sns ; sns.set_theme(style="whitegrid", font="Roboto")
import matplotlib as mpl
# mpl.rcParams['font.family'] = 'sans-serif'
# mpl.rcParams['font.sans-serif'] = ['Gentium']
import matplotlib.pyplot as plt
import pandas as pd
import pioupiou as pp

# TODO: use more from test.py (automate iteration on files to begin with)

# Helpers
# ------------------------------------------------------------------------------

def fetch_code(src):

    # TODO: refactor here, that's a cut-and-paste from test.py (test runner)
    lines = src.splitlines()
    code, prompt = False, False
    for i, line in enumerate(lines):
        if line.startswith("```python"):
            code = True
            prompt = lines[i+1].startswith(">>> ")
            lines[i] = ""
        elif line.startswith("```"):
            code = False
            lines[i] = ""
        elif code == True:
            if not prompt: 
                if line.startswith(" "): # heuristic for line continuation
                    lines[i] = "... " + line
                else:
                    lines[i] = ">>> " + line
            lines[i] = 4 * " " + lines[i]
    src = "\n".join(src)

    code = ""
    fences = False
    for line in src.splitlines():
        line = line.strip()
        if line.startswith(">>> ") or line.startswith("... "):
            code += line[4:] + "\n"
    return code

def fetch_viz_code(src):
    code = ""    
    add = False
    for line in src.splitlines():
        #line = line.strip()
        if add and not line.strip().startswith("```") and not line.strip().startswith("</div>"):
            code += line + "\n"
        if line == '<div class="viz">':
            add = True
        if line == '</div>':
            add = False
    return code
        
# ------------------------------------------------------------------------------

src = open("../index.md").read()
code = fetch_code(src)
exec(code)
plt.close("all")

# Height
# ------------------------------------------------------------------------------
src = open("../height.md").read()
code = fetch_code(src)
exec(code)
plt.close("all")

# Gaussians
# ------------------------------------------------------------------------------
src = open("../gaussians.md").read()
code = fetch_code(src)
exec(code)
plt.close("all")

# ------------------------------------------------------------------------------
src = open("../volatility.md").read()
code = fetch_code(src)
exec(code)
plt.close("all")
