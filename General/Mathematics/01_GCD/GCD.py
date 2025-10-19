#!/usr/bin/env python3

def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)

print("test: ", gcd(12,8))
print("result: ", gcd(66528, 52920))

