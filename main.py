#!/usr/bin/env python3

oldDomains = []
with open('lists/lista-processo-liberacao.2020.6.txt') as domains:
    for domain in domains:
        oldDomains.append(domain.rstrip())

newDomains = []
with open('lists/lista-processo-liberacao.2020.7.txt') as domains:
    for domain in domains:
        newDomains.append(domain.rstrip())

includes = set(newDomains).difference(oldDomains)

for include in includes:
	if ".com.br" in include:
		print(include)