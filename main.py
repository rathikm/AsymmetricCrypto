from math import gcd
import random

def prob_append(prob, arr, el):
  r = random.uniform(0, 1)
  if r < prob:
    arr.append(el)

def rsa(p, q):
  n = p * q
  tot_n = (p - 1) * (q - 1)
  rel_primes = []
  for i in range(1, tot_n):
    if gcd(i, tot_n) == 1:
      prob_append(0.25, rel_primes, i)
  e = random.choice(rel_primes)
  d = pow(e, -1, tot_n)
  return ((e, n), (d, n))

def el_gamal_encrypt(p, n, k):
  return (k * p) % n

def el_gamal_decrypt(c, n, k):
  k_inv = pow(k, -1, n)
  return (k_inv * c) % n

def diffie_hellman(nums):
  return (nums[1], nums[0])

def encrypt(datastream, pub):
  cipherstream = []
  for i in datastream:
    cipherstream.append(pow(i, pub[0], pub[1]))
  return cipherstream

def decrypt(cipherstream, priv):
  datastream = []
  for i in cipherstream:
    datastream.append(pow(i, priv[0], priv[1]))
  return datastream

def encode_str(s):
  arr = []
  for c in s:
    if c.isalpha():
      arr.append(ord(c) - 65)
  return arr

def decode_str(arr):
  s = ""
  for c in arr:
    s += chr(c + 65)
  return s

def s_o_e(n):
  table = [i for i in range(2, n)]
  primes = []
  while len(table) > 0:
    el = table[0]
    for j in table:
      if j != el and j % el == 0 and j >= pow(el, 2):
        #print(el, j)
        table.remove(j)
    primes.append(el)
    #print(el)
    table.remove(el)
  return primes


def miller_test(n, d):
  a = random.randint(2, n-2)
  x = pow(a, d, n)
  if x == 1 or x == n-1:
    return True
  while d != n-1:
    x = (x*x) % n
    d *= 2
    if (x == 1):
      return False
    if (x == n-1):
      return True


# test_str = "hello world"
# pub, priv = rsa(17, 11)
# encoded_pt = encode_str(test_str)
# ciphertext = encrypt(encoded_pt, pub)
# decrypted = decode_str(decrypt(ciphertext, priv))
# print(decrypted)
n = 26
base = 5
alice = random.randint(1, n)
bob = random.randint(1, n)
a = pow(base, alice, n)
b = pow(base, bob, n)
a, b = diffie_hellman((a, b))
e_key = pow(a, alice, n)
message = 20
ciphertext = el_gamal_encrypt(message, n, e_key)
d_key = pow(b, -1 * bob, n)
plaintext = el_gamal_decrypt(ciphertext, n, d_key)

print(s_o_e(100))
