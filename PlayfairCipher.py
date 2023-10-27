### Encrypt the plaintext using Playfair's keyword cipher

### Shift if same row: Cell on the right
### Shift if same column: Cell below
### Order of letter elsewhere: Same row as letter 1 first

def create_playfair_matrix(key):
    key = key.replace("J", "I")
    key = "".join(dict.fromkeys(key))  
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper()
    matrix = []
    for char in key:
        if char in alphabet:
            matrix.append(char)
            alphabet = alphabet.replace(char, "")
    for char in alphabet:
        matrix.append(char)
    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def find_coordinates(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plain_text, key):
    matrix = create_playfair_matrix(key)
    encrypted_text = []
    plain_text = plain_text.upper().replace("J", "I")
    plain_text = "".join(filter(str.isalpha, plain_text))
    if len(plain_text) % 2 != 0:
        plain_text += "X"  

    for i in range(0, len(plain_text), 2):
        char1, char2 = plain_text[i], plain_text[i+1]
        row1, col1 = find_coordinates(matrix, char1)
        row2, col2 = find_coordinates(matrix, char2)
        if row1 == row2:
            encrypted_char1 = matrix[row1][(col1 + 1) % 5]
            encrypted_char2 = matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_char1 = matrix[(row1 + 1) % 5][col1]
            encrypted_char2 = matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_char1 = matrix[row1][col2]
            encrypted_char2 = matrix[row2][col1]
        encrypted_text.append(encrypted_char1)
        encrypted_text.append(encrypted_char2)

    return "".join(encrypted_text)

### Enter key and plain text here:
key = "CRYPTOLOGY"
plain_text = "BEAUFORT"
encrypted_text = playfair_encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)
