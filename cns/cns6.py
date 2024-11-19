def columnar_encrypt(text, key):
    sorted_key = sorted(key)
    columns = [''] * len(key)
    for i, char in enumerate(text):
        columns[i % len(key)] += char
    return ''.join(columns[sorted_key.index(k)] for k in key)

# Example
text = "HELLO"
key = "3214"
print("Encrypted:", columnar_encrypt(text, key))
