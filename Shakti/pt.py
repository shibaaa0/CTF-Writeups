#from secret import e, msg
from Crypto.Util.number import *
from gmpy2 import *
from Crypto.PublicKey import RSA
msg='shibaaa{}'.encode()
p = getPrime(2048)
q = getPrime(2048)
n = p * q
e=65537
phi = (p - 1) * (q - 1)
d = invert(e, phi)

m = bytes_to_long(msg)
ct = pow(m, e, n)

with open("ciphertext1.txt", "w") as f:
    f.write(str(ct))

key = RSA.construct((int(n), int(e), int(d), int(p), int(q)))
pem = key.export_key('PEM')
with open("private_key1.pem", "wb") as f:
    f.write(pem)
