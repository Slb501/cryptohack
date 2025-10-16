from Crypto.Util.number import bytes_to_long
from hashlib import sha256


#python3 -m venv ~/myenv
#source ~/myenv/bin/activate


f = open("private_0a1880d1fffce9403686130a1f932b10.key")
for line in f:
    line = line.strip()
    if line.startswith("N ="):
        N = int(line.split("=")[1].strip())
    elif line.startswith("d ="):
        d = int(line.split("=")[1].strip())


flag = b"crypto{Immut4ble_m3ssag1ng}"

mHash = sha256(flag).digest()
int_Hash = bytes_to_long(mHash)

sign = pow(int_Hash, d, N)
print(sign)
