#!/usr/bin/env python3

import sys

print(sys.argv)

if len(sys.argv) < 2:
    print("You've given me nothing to work with.")
else:
    print(sys.argv[1] +"? Well I disagree!")
