
#returns (u,v),  
#p*u+q*v=gcd(p,q)
def egcd(p,q):
    if p == 0:
        return 0,1
    u1,v1 = egcd(q%p,p)
    u = v1 - (q // p) * u1
    v = u1
    return u,v


print(egcd(12,8))
print(egcd(26513,32321))

