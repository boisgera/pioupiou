#!/usr/bin/env python

# Python Standard Library
import doctest
import platform
import sys
import re

# Third-Party Libraries
import strictyaml

# Test Files
# ------------------------------------------------------------------------------
mkdocs_content = strictyaml.load(open("mkdocs.yml").read())["nav"].data
mkdocs_files = []
for value in [list(item.values())[0] for item in mkdocs_content]:
    if isinstance(value, str): # page
        mkdocs_files.append(value)
    else: # section
        mkdocs_files.extend([list(item.values())[0] for item in value])
mkdocs_files = ["mkdocs/" + file for file in mkdocs_files]
extra_testfiles = []
test_files = mkdocs_files + extra_testfiles

# Run the Tests
# ------------------------------------------------------------------------------
verbose = "-v" in sys.argv or "--verbose" in sys.argv

fails = 0
tests = 0
for filename in test_files:
    options = {"module_relative": False, "verbose": verbose}
    _fails, _tests = doctest.testfile(filename, **options)
    fails += _fails
    tests += _tests

if fails > 0 or verbose: # pragma: no cover
   print()
   print(60*"-")
   print("Test Suite Report:", end=" ")
   print("{0} failures / {1} tests".format(fails, tests))
   print(60*"-")
if fails: # pragma: no cover
    sys.exit(1)
 
