#!/usr/bin/env python
import sys
output = sys.stdin.read()
for line in output.splitlines():
    if line.startswith("TOTAL"):
        print(line[-4:].strip())
