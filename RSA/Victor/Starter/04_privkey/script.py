#!/usr/bin/python3

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi_N = (p - 1) * (q - 1)
e = 65537

def pgcd(x,y):
    x = abs(x)
    y = abs(y)
    while (y != 0):
        r = x % y
        x = y
        y = r
    return (x)

def Bezout(x, y):
    u0, u1, v0, v1 = 1, 0, 0, 1
    while (y != 0):
        q = x // y
        r = x % y
        x, y = y, r
        u0, u1 = u1, u0 - q * u1
        v0, v1 = v1, v0 - q * v1
    if x < 0:
        x, u0, v0 = -x, -u0, -v0
    return x, u0, v0

def inverse(x, n):
    if pgcd(x, n) != 1:
        print(f"{x} modulo {n} n'est pas inversible")
        return
    a, b, c = Bezout(x, n)
    return b % n

print(inverse(e, phi_N))