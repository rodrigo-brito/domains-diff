#!/usr/bin/env python3

import sys

def count_vowels(sentence):
    count = 0
    for letter in sentence:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

if len(sys.argv) < 3:
    print("example of usage: ./main.py old.txt new.txt [max_size] [vowels]")

size = 10
vowels = 2

if len(sys.argv) > 3:
    size = int(sys.argv[3])

if len(sys.argv) > 4:
    vowels = int(sys.argv[4])

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
        prefix = include.replace(".com.br", "")
        if len(prefix) <= size and count_vowels(prefix) >= vowels:
            print(include)