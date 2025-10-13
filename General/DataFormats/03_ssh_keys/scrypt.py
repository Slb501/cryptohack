from Crypto.PublicKey import RSA

#python3 -m venv ~/myenv
#source ~/myenv/bin/activate


f = open("bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub")
key = RSA.import_key(f.read())
print(key.n)


