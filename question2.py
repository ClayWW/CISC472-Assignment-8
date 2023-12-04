import math

def baby_giant(g, A, p):
    n = int(math.sqrt(p)+1) #square root of p and round up for range of baby and giant steps
    baby_steps = {pow(g, i, p): i for i in range(n)} #create a dictionary to store g^i mod p for i from 0 to n
    c = pow(g, n*(p-2),p) #precompute g^(-n) mod p, which is used for giant steps. -2 because of Femat's Little Theorem
    for j in range(n): #iterate through possible values of j to take the giant steps.
        y = (A * pow(c, j, p)) % p #calculate A * g^(-jn) mod p and check if it exists in the baby steps dictionary.
        if y in baby_steps:
            return j * n + baby_steps[y]  #if a match is found, return the discrete logarithm 
    return None #if no match is found

# Given values
g = 7
p = 1404693457
A = 785170121
B = 413383232

# Find Alice's secret (a)
a = baby_giant(g, A, p)

# Compute the shared secret
shared_secret = pow(B, a, p) if a is not None else None
print(shared_secret)