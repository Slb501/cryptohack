#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from OpenSSL.crypto import load_certificate, FILETYPE_PEM
import hashlib
import json
import requests



#python3 -m venv ~/myenv
#source ~/myenv/bin/activate


    #générer une empreinte cryptographique

f = open("transparency_afff0345c6f99bf80eab5895458d8eab.pem")
key = RSA.import_key(f.read()).public_key()


sha256 = hashlib.sha256(key.exportKey(format="DER"))
fp = sha256.hexdigest()
print("fingerprint:", fp)

    #rechercher le certificat 


#faire ressembler la requête HTTP à celle d’un navigateur
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
url = "https://crt.sh/?spkisha256={hash}&output=json"

#requete
req = requests.get(url.format(hash=fp), headers={'User-Agent': user_agent})
content = req.content.decode('utf-8')
data = json.loads(content)
id = data[0]["id"]
download_url = "https://crt.sh/?d={id}"
req = requests.get(download_url.format(id=id), headers={'User-Agent': user_agent})
PEMcert = req.content.decode('utf-8')
    #obtenir le nom du sous domaine
cert = load_certificate(FILETYPE_PEM, PEMcert) 
CN = cert.get_subject().commonName 
print("Nom du domaine: ", CN)


    #obtenir le flag
flag_url = "https://" + CN
req = requests.get(flag_url, headers={'User-Agent': user_agent})
flag = req.content.decode('utf-8')
print("Flag:", flag)
