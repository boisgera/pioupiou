#!/bin/bash
import doctest
import sys

failure, count = doctest.testfile("README.md")
if failure:
    sys.exit(count)
else:
    doctest.testfile("tests.md")
