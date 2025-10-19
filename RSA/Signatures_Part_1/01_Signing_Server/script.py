#!/usr/bin/env python3

import socket
import json
from Crypto.Util.number import long_to_bytes

host = "socket.cryptohack.org"
port = 13374

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)
print(data.decode())

request = {'option': 'get_secret'}
s.send(json.dumps(request).encode())
data = s.recv(1024)
response = json.loads(data.decode())
sk_hex = response['secret']
sk = int(sk_hex,16)


request = {'option': 'sign', 'msg':sk_hex}
s.send(json.dumps(request).encode())
data = s.recv(1024)
response = json.loads(data.decode())
sign = int(response['signature'],16)

request = {'option': 'get_flag', 'secret': response['signature']}
s.send(json.dumps(request).encode())
data = s.recv(1024)
response = json.loads(data.decode())
print(f"Flag response: {response}")


request = {'option': 'get_pubkey'}
s.send(json.dumps(request).encode())
data = s.recv(1024)
response = json.loads(data.decode())
N = int(response['N'],16)
e = int(response['e'],16)

print(f"sk: {sk}")
print(f"sign: {sign}")
print(f"N: {N}")
print(f"e: {e}")

assert sk ==  pow(sign, e, N)

flag = long_to_bytes(sign).decode()
print(f"Flag: {flag}")
