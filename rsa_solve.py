p = 833798983855161463343002937180389
q = 77550609119954621515805419275242
e = 65537
cifra = 7022848098469230958320047471

import gmpy2
dp = gmpy2.invert(e, (p-1))
dq = gmpy2.invert(e, (q-1))
qinv = gmpy2.invert(q, p)

def dec(c):
  m1 = pow(c, dp, p)
  m2 = pow(c, dq, q)
  h = (qinv * (m1 - m2)) % p 
  m = m2 + h * q
  return long_to_bytes(m)

import sys
import os
from Crypto.Util.number import long_to_bytes
c = int(hex(cifra), 16)
m = dec(c)
print(bytes(m).decode())
