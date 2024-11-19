def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    direction = 1
    rail = 0
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    return "".join("".join(row) for row in fence)

# Example
text = "HELLO"
rails = 3
print("Encrypted:", rail_fence_encrypt(text, rails))
