def playfair_cipher_encrypt(key, text):
    key = "".join(dict.fromkeys(key.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ")).replace("J", "I")
    matrix = [key[i:i + 5] for i in range(0, 25, 5)]
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'

    def find_position(char):
        for i, row in enumerate(matrix):
            if char in row:
                return i, row.index(char)

    encrypted_text = ""
    for i in range(0, len(text), 2):
        row1, col1 = find_position(text[i])
        row2, col2 = find_position(text[i + 1])
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text

# Example
text = "HELLO"
key = "KEY"
print("Encrypted:", playfair_cipher_encrypt(key, text))
