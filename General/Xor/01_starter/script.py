#!/usr/bin/python3
from pwn import *

input = "label"

as_list = list(input)
for i in range(len(as_list)):
    as_list[i] = chr(ord(as_list[i]) ^ 13) 

output = ''.join(as_list)
print(output)