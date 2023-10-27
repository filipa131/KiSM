### Determine the key K in the Hill cipher if m = 2.

import numpy as np

### Enter plain text and cipher text here:
plaintext = "HEBERN"
ciphertext = "TTRBKZ"

pairs = [(plaintext[i:i+2], ciphertext[i:i+2]) for i in range(0, len(plaintext), 2)]

matrices1 = []
matrices2 = []

for i in range(len(pairs) - 1):
    pt1, ct1 = pairs[i]
    pt2, ct2 = pairs[i+1]
    
    matrix1 = [[ord(pt1[0]) - 65, ord(pt1[1]) - 65],
               [ord(pt2[0]) - 65, ord(pt2[1]) - 65]]
    
    matrix2 = [[ord(ct1[0]) - 65, ord(ct1[1]) - 65],
               [ord(ct2[0]) - 65, ord(ct2[1]) - 65]]
    
    matrices1.append(matrix1)
    matrices2.append(matrix2)

matrices1 = [np.array(matrix) for matrix in matrices1]
matrices2 = [np.array(matrix) for matrix in matrices2]

def determinant_inverse_mod_26(matrix):
    det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    for i in range(1, 27):
        if (det * i) % 26 == 1:
            return i
    else:
        return -1
    
def key(matrix1, matrix2):
    pom = np.zeros((2, 2), dtype=int)
    pom[0][0] = matrix1[1][1]
    pom[0][1] = -matrix1[0][1]
    pom[1][0] = -matrix1[1][0]
    pom[1][1] = matrix1[0][0]

    return np.dot(determinant_inverse_mod_26(matrix1), np.dot(pom, matrix2)) % 26

for mat in matrices1:
    if(determinant_inverse_mod_26(mat) == -1):
        continue
    else: 
        print(f"Key:\n {key(matrices1[i], matrices2[i])}")