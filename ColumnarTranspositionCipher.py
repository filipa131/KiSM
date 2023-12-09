from itertools import permutations
from collections import defaultdict
import math

def generate_bigrams(col1, col2):
    return [col1[i] + col2[i] for i in range(len(col1))]

### Enter cipher and number of columns
ciphertext = "SSPSOEFJPZAAKAKAAALTAKEOANLIIIUEPBIIOKVISRAOSRJFHSPTJEAS"
num_columns = 8  

num_rows = math.ceil(len(ciphertext) / num_columns)

table = [['' for _ in range(num_columns)] for _ in range(num_rows)]

index = 0
for j in range(num_columns):
    for i in range(num_rows):
        if index < len(ciphertext):
            table[i][j] = ciphertext[index]
            index += 1

print("Table: \n")
for row in table:
    print(' '.join(row))
print()
print()

bigrams_to_check = [
    'AK', 'AN', 'AS', 'AT', 'AV', 'CI', 'DA', 'ED', 'EN', 'IC', 'IJ', 'IN',
    'IS', 'JA', 'JE', 'KA', 'KO', 'LI', 'NA', 'NE', 'NI', 'NO', 'OD', 'OJ',
    'OS', 'OV', 'PO', 'PR', 'RA', 'RE', 'RI', 'ST', 'TA', 'TI', 'VA', 'ZA'
]

frequency_table = defaultdict(lambda: defaultdict(int))

num_columns = len(table[0])
for i in range(num_columns):
    for j in range(num_columns):
        if i != j:  
            column1 = [row[i] for row in table] 
            column2 = [row[j] for row in table] 
            bigrams = generate_bigrams(column1, column2)  
            for bigram in bigrams:
                if bigram in bigrams_to_check:
                    frequency_table[i + 1][j + 1] += 1  

print("Table of the most frequent bigrams: \n")
print("   | ", end="")
for i in range(1, num_columns + 1):
    print(f"{i:3}", end="")
print("\n--------------------------------------")
for i in range(1, num_columns + 1):
    print(f"{i:2} | ", end="")
    for j in range(1, num_columns + 1):
        print(f"{frequency_table[i][j]:3}", end="")
    print()
print()
print()

def decrypt_transposition(ciphertext, key):
    num_columns = len(key)
    num_rows = -(-len(ciphertext) // num_columns)

    decrypted_text = [''] * len(ciphertext)
    index = 0

    for row in range(num_rows):
        for col in key:
            decrypted_text[index] = table[row][col - 1]
            index += 1

    return ''.join(decrypted_text)

### Enter the permutation you believe is correct
perm = [4, 7, 8, 5, 1, 3, 6, 2]

decrypted = decrypt_transposition(ciphertext, perm)
print(f"Decrypted message: {decrypted}\n")