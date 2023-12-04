from hashlib import sha256

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

def hash(message, order):
    hashed = sha256(message.encode('utf-8')).hexdigest()
    truncated_hashed = hashed[:len(str(order))]
    return int(truncated_hashed, 16)

order = 131
r = 125

hash_m1 = hash('Applied Crypto', order)
hash_m2 = hash('University of Delaware', order)
hash_m3 = hash('Blue - Hens', order)

s1 = 46
s2 = 21

k = (hash_m1 - hash_m2) * mod_inverse(s1-s2, order) % order
s3 = (k * s1 - hash_m1) * mod_inverse(r, order) % order

sig_m3 = (r, s3)
print("Signature of message 3: ", sig_m3)