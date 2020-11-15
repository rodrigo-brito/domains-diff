#!/usr/bin/env python3

import sys, os
import argparse
from flashtext import KeywordProcessor

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--file', action='store', default=0, type=str, required=True)
my_parser.add_argument('--old-file', action='store', type=str)
my_parser.add_argument('--vowels', action='store', default=0, type=int)
my_parser.add_argument('--max-size', action='store', default=10, type=int)
my_parser.add_argument('--keywords', action='store', default="lists/keywords.txt", type=str)
args = my_parser.parse_args()

# setup keyword processor
keywords = KeywordProcessor(case_sensitive=False)
keywords.add_keyword_from_file("lists/keywords.txt")

def count_vowels(sentence):
    count = 0
    for letter in sentence:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

domains = []
with open(args.file) as input:
    for domain in input:
        domains.append(domain.rstrip())

if args.old_file:
    newDomains = []
    with open(args.old_file) as domains:
        for domain in domains:
            newDomains.append(domain.rstrip())
    domains = set(newDomains).difference(domains)

for include in domains:
    if ".com.br" in include:
        prefix = include.replace(".com.br", "")
        if len(prefix) <= args.max_size and count_vowels(prefix) >= args.vowels and (not args.keywords or prefix in keywords):
            print(include)