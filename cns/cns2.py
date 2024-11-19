def polyalphabetic_cipher(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            result += char
    return result

# Example
text = "HELLO"
key = "KEY"
encrypted = polyalphabetic_cipher(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", polyalphabetic_cipher(encrypted, key))
