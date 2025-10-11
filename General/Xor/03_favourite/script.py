#!/usr/bin/python3


hex_str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_bytes = bytes.fromhex(hex_str)

for i in range(256):
    xored = bytes([b ^ i for b in cipher_bytes])
    try:
        flag = xored.decode()
        if flag[:6] == "crypto":
            print(flag)
            break
    except UnicodeDecodeError:
        continue