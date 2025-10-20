#!/usr/bin/env python3


from Crypto.Util.number import bytes_to_long, long_to_bytes
import socket
import json

host = 'socket.cryptohack.org'
port = 13375
N = 22266616657574989868109324252160663470925207690694094953312891282341426880506924648525...
e = 3

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
data = sock.recv(1024)
print(data)

T = b'VOTE FOR PEDRO'
c = bytes_to_long(T)

def cube_root_2_pow(c, k_max):
    s = c % 8
    for k in range(3, k_max):
        diff = s**3 - c
        d = diff // (2**k)
        t = (-d) % 2
        s = s + t * (2**k)
    return s

s = cube_root_2_pow(c, len(T)*8 + 8)
sign_hex = long_to_bytes(s).hex()

payload = {
    "option": "vote",
    "vote": sign_hex
}

sock.send(json.dumps(payload).encode())
flag = sock.recv(1024)
print(flag)
