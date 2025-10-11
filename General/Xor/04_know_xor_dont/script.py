#!/usr/bin/python3


hex_str = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_bytes = bytes.fromhex(hex_str)
partial_flag = b"crypto{"

xored = []
for i, c in enumerate(cipher_bytes):
    xored_byte = c ^ partial_flag[i % len(partial_flag)]
    xored.append(xored_byte)
xored = bytes(xored)
print(xored.decode())

key = b"myXORkey"
xored_result = []
for i, c in enumerate(cipher_bytes):
    xored_byte = c ^ key[i % len(key)]
    xored_result.append(xored_byte)

xored_result = bytes(xored_result)
print(xored_result)