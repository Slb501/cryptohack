#!/usr/bin/env python3

from Crypto.PublicKey import RSA

#python3 -m venv ~/myenv
#source ~/myenv/bin/activate


f = open("privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem")
key = RSA.import_key(f.read())
print(key.d)

