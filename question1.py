def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g,x,y = extended_gcd(b%a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception("Mod inverse does not exist")
    else:
        return x % m
    
def find_Y(g, c1, p):
    for Y in range(1,p):
        if pow(g, Y, p) == c1:
            return Y
    return None

p = 20876441
g = 5

#part 1
c1 = 9916780
y = find_Y(g, c1, p)
d = pow(c1, y, p)

#part 2
c1_m2 = 7350174
c2_m2 = 13786334
e = mod_inverse(d, p)
m2 = (e * c2_m2) % p

#part 3
m3 = 12345
m4 = 382695
c1_m3 = 8698838
c2_m3 = 17288353
c2_m4 = (m4 * mod_inverse(m3, p) * c2_m3) % p
c1_m4 = c1_m3

print(f"Shared Secret (from part 1): {d}")
print(f"Decrypted message M2 (from part 2): {m2}")
print(f"Encrypted message M4 (from part 3): (C1, C2) = ({c1_m4}, {c2_m4})")


