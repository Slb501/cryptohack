from pathlib import Path 
from cryptography import x509
from cryptography.hazmat.backends import default_backend 

p = Path("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der") 
data = p.read_bytes()
cert = x509.load_der_x509_certificate(data, default_backend()) 
pub = cert.public_key()
numbers = pub.public_numbers()
print(numbers.n)
