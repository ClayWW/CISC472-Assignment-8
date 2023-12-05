from hashlib import sha256

# function for extended gcd, returns gcd of a and b and bezout's coefficients
def extended_gcd(a, b):
    # base case for recursion, when a is 0
    if a == 0:
        return (b, 0, 1)
    else:
        # recursively find gcd and coefficients
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

# function to find modular inverse of a under modulo m
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    # if gcd is not 1, no modular inverse exists, raise exception
    if g != 1:
        raise Exception("Mod inverse does not exist")
    else:
        # return modular inverse
        return x % m

# function to hash a message and truncate it to match the order length
def hash(message, order):
    # hash message using sha256
    hashed = sha256(message.encode('utf-8')).hexdigest()
    # truncate the hash to the length of the order
    truncated_hashed = hashed[:len(str(order))]
    return int(truncated_hashed, 16)

order = 131
r = 125

hash_m1 = hash('Applied Crypto', order)
hash_m2 = hash('University of Delaware', order)
hash_m3 = hash('Blue - Hens', order)

s1 = 46
s2 = 21

# calculate k using the signatures and hashes of msg1 and msg2
# the formula for k is derived from ecdsa equations
k_numerator = (hash_m1 - hash_m2) % order
k_denominator = (s1 - s2) % order
k = (k_numerator * mod_inverse(k_denominator, order)) % order

# calculate private key d
d = ((s1 * k - hash_m1) * mod_inverse(r, order)) % order
# calculate s3 for msg3
s3 = 1+((hash_m3 + r * d) * mod_inverse(k, order)) % order

sig_m3 = (r, s3)
print("Signature of message 3: ", sig_m3)
