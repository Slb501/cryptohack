#!/usr/bin/python3

p = 28151
card = p - 1

for i in range(1,card):
    power = 1
    res = pow(i, power, p)
    while res != 1 :
        power += 1
        res = pow(i, power, p)
    if power == card :
        print(i)
        break