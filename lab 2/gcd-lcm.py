def gcd(m,n):
    if m<n:
        (m,n)=(n,m)

    while (m%n) !=0:
        return gcd(n,m%n)
    return n

def lcm(a,b):
    return (a // gcd(a,b))* b

print(gcd(11,41))
print(lcm(13,41))
    