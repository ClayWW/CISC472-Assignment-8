from ecdsa import *

print(datetime.datetime.now())
print()

C = CurveOverFp(0, 1, 1, 2833)
base_point = Point(1341, 854)
n = 131
public_key = Point(991, 1988)

print('public key:', public_key)
print()
print('C.contains(base_point)', C.contains(base_point))
print()

messages = []

msg_1 = 'Applied Crypto'
r_1, s_1 = 125, 46
sig_1 = (public_key, r_1, s_1)

v = verify(msg_1, C, base_point, n, sig_1)
print('Verify (\"' + msg_1 + '\")', v)

msg_2 = 'University of Delaware'
r_2, s_2 = 125, 21
sig_2 = (public_key, r_2, s_2)

v = verify(msg_2, C, base_point, n, sig_2)
print('Verify (\"' + msg_2 + '\")', v)

msg_to_sign = 'Blue - Hens'
print()
print('Can you sign \"' + msg_to_sign + '\"?')
print()


r = int(input('r: '))
s = int(input('s: '))
input_sig = (public_key, r, s)
print()

if verify(msg_to_sign, C, base_point, n, input_sig):
    print('Correct!!!')
else:
    print('Incorrect signature...')
