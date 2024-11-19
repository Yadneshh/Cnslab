def simple_des_encrypt(plaintext, key):
    """Simplified DES encryption"""
    # Step 1: Permutation (P10)
    def permute(input, perm_table):
        return [input[i] for i in perm_table]

    # Step 2: Key Generation (Two Subkeys K1, K2)
    def generate_keys(key):
        p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
        p8 = [5, 2, 6, 3, 7, 4, 9, 8]
        left_shift_table = [1, 1]

        # Permute key with P10
        permuted_key = permute(key, p10)

        # Generate two subkeys by shifting and applying P8
        def left_shift(bits, shifts):
            return bits[shifts:] + bits[:shifts]

        k1 = permute(left_shift(permuted_key[:5], left_shift_table[0]) + 
                     left_shift(permuted_key[5:], left_shift_table[0]), p8)
        k2 = permute(left_shift(permuted_key[:5], left_shift_table[1]) + 
                     left_shift(permuted_key[5:], left_shift_table[1]), p8)

        return k1, k2

    # Step 3: Function F (Expansion, XOR, S-box, P4)
    def function_f(bits, subkey):
        e_p = [3, 0, 1, 2, 1, 2, 3, 0]  # Expansion/permutation table
        s_boxes = [
            [[1, 0], [0, 1], [1, 1], [0, 0]],  # S-box 1
            [[0, 1], [1, 1], [1, 0], [0, 0]]   # S-box 2
        ]
        p4 = [1, 3, 2, 0]  # P4 permutation table

        expanded = permute(bits, e_p)
        xor_result = [a ^ b for a, b in zip(expanded, subkey)]

        # S-box substitution
        def s_box_lookup(bits, s_box):
            row = (bits[0] << 1) + bits[3]
            col = (bits[1] << 1) + bits[2]
            return s_box[row][col]

        left_sbox = s_box_lookup(xor_result[:4], s_boxes[0])
        right_sbox = s_box_lookup(xor_result[4:], s_boxes[1])
        substituted = [int(b) for b in f"{left_sbox:02b}{right_sbox:02b}"]

        # Apply P4 permutation
        return permute(substituted, p4)

    # Initial Permutation (IP) and Inverse Permutation (IP⁻¹)
    ip = [1, 5, 2, 0, 3, 7, 4, 6]
    ip_inv = [3, 0, 2, 4, 6, 1, 7, 5]

    # Encryption logic
    permuted_input = permute(plaintext, ip)
    left, right = permuted_input[:4], permuted_input[4:]

    k1, k2 = generate_keys(key)

    # Round 1
    new_right = [a ^ b for a, b in zip(left, function_f(right, k1))]
    left, right = right, new_right

    # Round 2
    new_right = [a ^ b for a, b in zip(left, function_f(right, k2))]
    left, right = right, new_right

    # Combine and apply IP⁻¹
    return permute(left + right, ip_inv)

# Example
plaintext = [1, 0, 1, 0, 0, 1, 1, 1]  # Example 8-bit plaintext
key = [1, 0, 1, 0, 0, 1, 1, 1, 1, 0]  # Example 10-bit key

ciphertext = simple_des_encrypt(plaintext, key)
print("Encrypted:", ciphertext)
