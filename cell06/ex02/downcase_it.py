#!/usr/bin/env python3
import sys
def downcase_it(words):
    return words.lower()
if len(sys.argv) > 1:
    print(downcase_it(sys.argv[1]))
else:
    print("none")
