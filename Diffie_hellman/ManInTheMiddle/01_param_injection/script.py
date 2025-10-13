#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
from pwn import *
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

context.log_level = 'debug' 
"""
nc socket.cryptohack.org 13371 pour savoir ce qui se passe en se connectant au serveur

Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x4aae07ec69f534927e9bdc481077a4807af576f959f27b20b3b889cb995ad53ce0dc6569c8d5edbe27a248aefad188dea901a2be1a1fa538492c4f867b2a8117f16e3276880743280fdda0de0245626e41b0c2d34394bc599cc2a4dcd5e2a9c00fa32678406a360b5227f8cf48601057819c2cff7cc49275cfc663ca4a52533aab60e71b53c005479bd5ebc179949dde5eb4b263eaf897839bc598e253180b786024589e17f73c784a844d10c25a7b10624608e11abf2ecc107847ce7877b287"}
Send to Bob: 
>> Je lui renvoie les infos d'alice
>> {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x4aae07ec69f534927e9bdc481077a4807af576f959f27b20b3b889cb995ad53ce0dc6569c8d5edbe27a248aefad188dea901a2be1a1fa538492c4f867b2a8117f16e3276880743280fdda0de0245626e41b0c2d34394bc599cc2a4dcd5e2a9c00fa32678406a360b5227f8cf48601057819c2cff7cc49275cfc663ca4a52533aab60e71b53c005479bd5ebc179949dde5eb4b263eaf897839bc598e253180b786024589e17f73c784a844d10c25a7b10624608e11abf2ecc107847ce7877b287"}
Intercepted from Bob: {"B": "0x5de9a78918661cf5e65baf6e63d676277be58306a0dddc2542475ba8d9daff5883be9a2852999e2085797df38dff185cff80ad710257725d627630dc99f93c6a4bc6b756fd571f0a91bc291f29a1b01a2222399cd495023c97852d9a84d66554182de22e1285a14d5e1709246a9252582825380e1d902f386cdb04fa70807b2df8b7fd45242c0718596c51a6b2417363efa557a9a3dd3367e1ffb73f40dc3d48de6f891694b308df856e26924e430ebbef5fd58301690836c4a67b3307ce74c2"}
Send to Alice:
>> Je vais lui renvoyer les informations de Bob avec B = 1. Du coup elle va calculer sa clé secrète avec 1**sa clé mod p et donc shared_secret = 1
>> {"B":"0x1"}
Intercepted from Alice: {"iv": "c6e53278c84a3a547a13e6fc933d41a2", "encrypted_flag": "d4591256126484ad8eaae350db1588d859bae01db7226e7be15de8e671e4709d"}

Hop, voila le travail, plus qu'a utiliser
"""


