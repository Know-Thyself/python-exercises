def encrypt(text, n):
    odd = ''
    even = ''
    while n > 0:
        for idx, char in enumerate(text):
            if idx % 2 == 0:
                even += char
            else:
                odd += char
        n -= 1
        return encrypt(f'{odd}{even}', n)
    return text


# Pseudocode for the decrypt function:
# 1. Split the text into two parts: odd and even
# 2. Initialize an empty string called decrypted
# 3. Iterate over half of the characters (rounded down) in the text
#    - Swap the characters between the odd and even parts by appending even[i] + odd[i] to decrypted
# 4. If the length of the text is odd, append the last character from even to decrypted
# 5. If n is greater than 1, recursively call the decrypt function with the decrypted text and n-1
#    - Repeat the decryption process n-1 times
# 6. Return the decrypted text


def decrypt(text, n):
    while n > 0:
        odd = text[:len(text) // 2]  # Extract the first half of the text
        even = text[len(text) // 2:]  # Extract the second half of the text
        decrypted = ''
        for i in range(len(text) // 2):
            decrypted += even[i] + odd[i]  # Swap the characters from even and odd

        if len(text) % 2 != 0:  # Check if the length is odd
            decrypted += even[-1]  # Append the last character from even to the decrypted text
        n -= 1
        return decrypt(decrypted, n)
    return text  # Return the decrypted text


# Example usage:
print(encrypt("This is a test!", 1))
print(encrypt("This is a test!", 2))
print(encrypt("This is a test!", 3))
print(encrypt('this', 1))
print(encrypt('012345', 1))
print(decrypt('hsti', 1))
decrypted_text = decrypt('hsi  etTi sats!', 1)
print(decrypted_text)
print(decrypt("135024", 1))
