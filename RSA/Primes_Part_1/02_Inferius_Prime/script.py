#!/usr/bin/env python3

from Crypto.Util.number import inverse, long_to_bytes
import primefac

n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

p,q = list(primefac.primefac(n))
print(f"p:{p} \nq:{q}")

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print(decrypted)


