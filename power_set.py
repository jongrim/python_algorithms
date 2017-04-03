#! /usr/bin/env python


def power_set(items):
    n = len(items)

    for i in range(2**n):
        combo = []
        for j in range(n):
            if (i >> j) % 2 == 1:  # >> effectively does (i // 2*j)
                combo.append(items[j])
        yield combo


items = ['rock', 'paper', 'scissors']
for i in power_set(items):
    print(i)
