#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import json
def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('utf-8')
    else:
        return plaintext.decode('utf-8', errors='replace')

    
"""
nc socket.cryptohack.org 13379
Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
Send to Bob: {"supported":["DH64"]}
Intercepted from Bob: {"chosen": "DH64"}
Send to Alice: {"chosen": "DH64"}
Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x674f9bbabc48cd8d"}
Intercepted from Bob: {"B": "0xb0474b841afb4d6e"}
Intercepted from Alice: {"iv": "42ec73835ae43797fa73803c035158fb", "encrypted_flag": "a398f814b44b69a83d2c9a0d8c35eaf65bc39b405af361a1f6ebeaec967c5809"}
"""
p_hex = "0xde26ab651b92a129"
g_hex = "0x2"
A_hex = "0x674f9bbabc48cd8d"
B_hex = "0xb0474b841afb4d6e"
iv = "42ec73835ae43797fa73803c035158fb"
encrypted_flag = "a398f814b44b69a83d2c9a0d8c35eaf65bc39b405af361a1f6ebeaec967c5809"

p = int(p_hex, 16)
g = int(g_hex, 16)
public_A = int(A_hex, 16)
public_B = int(B_hex, 16)
"""
# J'ai utilisé le site alpertron.com pour calculer les logs discret

a = 2953274130565991911
b = 8003835188138823828

shared_secret = pow(public_B, a, p)

print(decrypt_flag(shared_secret, iv, encrypted_flag))
"""


from sympy.ntheory.residue_ntheory import *
a = discrete_log(p, public_A, g) 
print(a)
shared_secret = pow(public_B, a, p)
print(decrypt_flag(shared_secret, iv, encrypted_flag))