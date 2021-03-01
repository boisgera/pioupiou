#!/usr/bin/env python
import sys
output = sys.stdin.read()
for line in output.splitlines():
    if line.startswith("Total"):
        print(line[-4:].strip())
