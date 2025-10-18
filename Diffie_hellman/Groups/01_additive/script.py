#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def decrypt_flag(shared_secret: int, iv_hex: str, ciphertext_hex: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]

    ciphertext = bytes.fromhex(ciphertext_hex)
    iv = bytes.fromhex(iv_hex)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    
    try:
        return unpad(plaintext, 16).decode('utf-8')
    except (ValueError, UnicodeDecodeError):
        return None


'''
nc socket.cryptohack.org 13380
Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x35989bea8b0af260c1d9cd4b75426bd42dd68f5bd39414ff87e2037ee202d764c74ad8b0f3dc4baa81f938a9052469d9946090dd112772c014a5c10e6594b0706b78b1a117eee4d994e134060f18828334dfd3fd704a6f5b04378d6ed0211a2a5dbd271bcbb2506a8baaa3e3660e3acce54b77f9af5dc0cfa60965e0c12eb91790c3e8acff8205c04778b109dee94404aba78293b4665a9890111a8a2c4b01e9e6540d884a8e427ca838e8b6b50474285d9784870ca450e955eaec41843b0fe6"}
Intercepted from Bob: {"B": "0x1beae7930caa88d92f2adbff4963bf7190a5c3a5967f4074cb6b39b52ce0b9cafef44992b1ffe1a5992051f48fff1dc6c2e2ddc8e5103a2630c976da7897f4b83d650c6a5d039ccbf4fcacb45a69fb6f2a28ce846411d1c33af91a700d1bcf5a4e9430b25b5f4c5ac41698a012b01b2359f3158a880bb762da9e11eb01dd831f06e26bc2a45f387d4998a84f7cbfb31005d4cc01b71adf051076d7b0cc8f32650ea35a4551c2480970a6122c1734f94bde36ad093c4faa556cb0bda8aac35ef3"}
Intercepted from Alice: {"iv": "37384cd571b3a77164ed9e19447c2c02", "encrypted": "f08752ab43bda0a5a6fb8cbdd7bd0ed5a944401eb7c37f74d08d8ec5355ad788f733416fea3d2b9cb67ec5170e3373ee"}

'''
p_hex = "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"
g_hex = "0x02"
A_hex = "0x35989bea8b0af260c1d9cd4b75426bd42dd68f5bd39414ff87e2037ee202d764c74ad8b0f3dc4baa81f938a9052469d9946090dd112772c014a5c10e6594b0706b78b1a117eee4d994e134060f18828334dfd3fd704a6f5b04378d6ed0211a2a5dbd271bcbb2506a8baaa3e3660e3acce54b77f9af5dc0cfa60965e0c12eb91790c3e8acff8205c04778b109dee94404aba78293b4665a9890111a8a2c4b01e9e6540d884a8e427ca838e8b6b50474285d9784870ca450e955eaec41843b0fe6"
B_hex = "0x1beae7930caa88d92f2adbff4963bf7190a5c3a5967f4074cb6b39b52ce0b9cafef44992b1ffe1a5992051f48fff1dc6c2e2ddc8e5103a2630c976da7897f4b83d650c6a5d039ccbf4fcacb45a69fb6f2a28ce846411d1c33af91a700d1bcf5a4e9430b25b5f4c5ac41698a012b01b2359f3158a880bb762da9e11eb01dd831f06e26bc2a45f387d4998a84f7cbfb31005d4cc01b71adf051076d7b0cc8f32650ea35a4551c2480970a6122c1734f94bde36ad093c4faa556cb0bda8aac35ef3"
iv = "37384cd571b3a77164ed9e19447c2c02"
encrypted_flag =  "f08752ab43bda0a5a6fb8cbdd7bd0ed5a944401eb7c37f74d08d8ec5355ad788f733416fea3d2b9cb67ec5170e3373ee"

p = int(p_hex, 16)
g = int(g_hex, 16)
A = int(A_hex, 16)
B = int(B_hex, 16)

g_inv = pow(g, -1, p)
a = (A * g_inv) % p

shared_secret = (a * B) % p

flag = decrypt_flag(shared_secret, iv, encrypted_flag)
print(flag)