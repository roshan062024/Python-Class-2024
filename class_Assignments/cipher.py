text = "attack is planned to happen on next sunday"
shift = 3

encrypted_text = ''.join([chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() else \
                          chr((ord(char) - ord('A') + shift) % 26 + ord('A')) if char.isupper() else char \
                          for char in text])

print("Original:", text)
print("Encrypted:", encrypted_text)