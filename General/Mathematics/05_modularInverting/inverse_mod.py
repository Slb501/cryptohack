
def egcd(p,q):
    if p == 0:
        return q,0,1
    r,u1,v1 = egcd(q%p,p)
    u = v1 - (q // p) * u1
    v = u1
    return r,u,v


def inverse_mod(x,p):
    r,u,_ = egcd(x, p)
    if r != 1 :
        raise ValueError(f"No inverse exists for {a} mod {p}")
    return u % p



print(inverse_mod(3,13))
