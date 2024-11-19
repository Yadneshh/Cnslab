def advanced_columnar_encrypt(text, key):
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    rows = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
    return ''.join(row[i] for i, _ in sorted_key for row in rows if i < len(row))

# Example
text = "HELLO"
key = "3214"
print("Encrypted:", advanced_columnar_encrypt(text, key))
