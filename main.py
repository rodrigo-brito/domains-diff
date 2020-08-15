#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("example of usage: ./main.py old.txt new.txt")

oldDomains = []
with open(sys.argv[1]) as domains:
    for domain in domains:
        oldDomains.append(domain.rstrip())

newDomains = []
with open(sys.argv[2]) as domains:
    for domain in domains:
        newDomains.append(domain.rstrip())

includes = set(newDomains).difference(oldDomains)

for include in includes:
	if ".com.br" in include:
		print(include)