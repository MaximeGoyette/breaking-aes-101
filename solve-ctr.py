import base64

cipherflag = base64.b64decode('Cc2TTGTiAbdCEbaQQmYPe5PVkl5qZZr2ejU0voyaNpXl8Y4xuXA5')

plaintext = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
ciphertext = base64.b64decode('LuCzaij4U+caFuCXFGVXKZSHx1luPMLzKTVtvNSYNMSxod41uXMl6fktuUaxdb7n31W6y7Z0k7OVxXEqPM+2GC/k5pN+OHJFueue70yBFs/o+xml7AUGlhxy828EtiRPa6OZml+AIbuid+c=')

xor = lambda p, k: ''.join([chr(ord(p[i])^ord(k[i%len(k)])) for i in xrange(len(p))])

key = xor(plaintext, ciphertext)
flag = xor(cipherflag, key)

print flag # FLAG-{319f7f7b93f34fe89d2a8c9cc0511eab}