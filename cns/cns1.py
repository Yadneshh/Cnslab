def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Example
text = "HELLO"
shift = 3
print("Encrypted:", caesar_cipher(text, shift))
print("Decrypted:", caesar_cipher(caesar_cipher(text, shift), -shift))
