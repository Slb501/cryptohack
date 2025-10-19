#!/usr/bin/python3

from pwn import * # pip install pwntools
from Crypto.Util.number import *
import codecs
import base64
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    type = received["type"]
    encoded = received["encoded"]

    if type == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif type == "hex":
        decoded = bytes.fromhex(encoded).decode()
    elif type == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif type == "bigint":
        decoded = long_to_bytes(int(encoded, 16)).decode()
    elif type == "utf-8":
        decoded = bytes(encoded).decode()

    to_send = {
    "decoded": decoded
    }

    json_send(to_send)

json_recv()




