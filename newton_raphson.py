#! /usr/bin/env python
"""
Newton-Raphson
"""


def newton_raphson(number, guess, threshold):
    sq_root = guess - ((guess**2 - number) / (2 * guess))
    if abs(sq_root**2 - number) <= threshold:
        return sq_root
    else:
        return newton_raphson(number, sq_root, threshold)


sq_root = str(newton_raphson(312, 5, .001))
print('The square root of 312 is approximately ' + sq_root)
