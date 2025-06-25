#!/usr/bin/env python3
import sys
parameter_count = len(sys.argv) - 1
if parameter_count < 2:
    print("none")
else:
    for parameter in reversed(sys.argv[1:]):
        print(parameter)
