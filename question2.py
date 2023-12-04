# Given values
g = 7
p = 1404693457
A = 785170121
B = 413383232

# Calculating the shared secret
# The shared secret s = A^b mod p = B^a mod p. 
# We can calculate this as s = B^A mod p or s = A^B mod p
shared_secret = pow(B, A, p)

# Output the shared secret
print(f"The shared secret is: {shared_secret}")