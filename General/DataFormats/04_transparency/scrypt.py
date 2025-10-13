from Crypto.PublicKey import RSA

#python3 -m venv ~/myenv
#source ~/myenv/bin/activate

import hashlib

f = open("transparency_afff0345c6f99bf80eab5895458d8eab.pem")
key = RSA.import_key(f.read()).public_key()

#todo ajouter des explications

sha256 = hashlib.sha256(key.exportKey(format="DER"))
print(sha256.hexdigest())

#https://0xffsec.com/handbook/information-gathering/subdomain-enumeration/#certificate-transparency



