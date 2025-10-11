#!/usr/bin/python3

KEY1 = int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313", 16)
X = int("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", 16) # KEY2 ^ KEY1
Y = int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", 16) # KEY2 ^ KEY3
Z = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", 16) # FLAG ^KEY1 ^ KEY3 ^KEY2

KEY2 = KEY1 ^ X
KEY3 = KEY2 ^ Y
FLAG = Z ^ KEY1 ^ KEY2 ^ KEY3

flag_hex = hex(FLAG)[2:]
if len(flag_hex) % 2 != 0:
	flag_hex = '0' + flag_hex
print(bytes.fromhex(flag_hex).decode())