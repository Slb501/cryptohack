#!/usr/bin/env python3

import socket, json
from sympy import symbols, Poly
from Crypto.Util.number import inverse, long_to_bytes


HOST = "socket.cryptohack.org"
PORT = 13386
e = 11

s = socket.create_connection((HOST, PORT))

greeting = b""
while b"\n" not in greeting:
    chunk = s.recv(4096)
    if not chunk:
        break
    greeting += chunk

s.sendall(json.dumps({"option":"get_flag"}).encode() + b"\n")

resp = b""
while b"\n" not in resp:
    chunk = s.recv(16384)
    if not chunk:
        break
    resp += chunk

print("greeting: ",greeting.decode(errors='ignore').strip())



data = json.loads(resp.decode(errors='ignore').strip().splitlines()[0])


c1 = int(data["encrypted_flag"])
N = int(data["modulus"])
a1, b1 = map(int, data["padding"])


#deuxieme message 

s.sendall(json.dumps({"option":"get_flag"}).encode() + b"\n")
resp2 = b""
while b"\n" not in resp2:
    chunk = s.recv(16384)
    if not chunk:
        break
    resp2 += chunk
data2 = json.loads(resp2.decode(errors='ignore').strip().splitlines()[0])

s.close()

c2 = int(data2["encrypted_flag"])
a2, b2 = map(int, data2["padding"])



def pretty_int(x, groups=3):
    return "{:}".format(x)            



print("N = ")
print(pretty_int(N))

print("c1 = ")
print(pretty_int(c1))
print()

print("a1 = ")
print(pretty_int(a1))
print()

print("b1 = ")
print(pretty_int(b1))
print()



m = symbols('m')
poly1 = Poly((a1*m + b1)**e - c1, m,modulus=N)
poly2 = Poly((a2*m + b2)**e - c2, m, modulus=N)

# Compute GCD using sympy
from sympy import gcd
poly_gcd = gcd(poly1, poly2)


print(f"[+] GCD = {poly_gcd}")

roots = poly_gcd.nroots()
#assert len(roots) == 1
message = roots

print(message)
print(f"[+] Recovered message: {long_to_bytes(int(message))}")

