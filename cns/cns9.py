def rsa_encrypt_decrypt(p, q, e, plaintext):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    # Encrypt
    encrypted = [pow(ord(char), e, n) for char in plaintext]

    # Decrypt
    decrypted = ''.join(chr(pow(c, d, n)) for c in encrypted)

    return encrypted, decrypted

# Example
p, q, e = 3, 11, 7
text = "HI"
encrypted, decrypted = rsa_encrypt_decrypt(p, q, e, text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
