### Decrypt the ciphertext obtained with Vigenere's cipher from plaintext in Croatian

from collections import defaultdict

### Enter cipher text here:
ciphertext = '''VYOXTVLNVKIKLKCTMAXSWUCTXEXGSZSLNKBEHGZULEXDOYBVBQISQFCVGZZFCQOYQWKZFGVAXBCPQAXBCXQJMZCJDRTCTGJVMRFGHCBTWZQYWLZPQETJJURGKFBGTRSRYPMZSCCFQFGRGBRVMJYURZSCCFJZNGOXQQN'''

def find_repeat_sequences(text, sequence_length=3):
    sequences = defaultdict(list)

    for i in range(len(text) - sequence_length + 1):
        sequence = text[i:i + sequence_length]
        sequences[sequence].append(i)

    return {sequence: positions for sequence, positions in sequences.items() if len(positions) > 1}

def find_probable_key_length(repeat_sequences):
    distances = []
    for positions in repeat_sequences.values():
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                distances.append(positions[j] - positions[i])

    probable_lengths = set()  
    for distance in distances:
        for factor in range(2, distance + 1):
            if distance % factor == 0:
                probable_lengths.add(factor)

    return list(probable_lengths)  

sequences = find_repeat_sequences(ciphertext, sequence_length=3)
probable_lengths = find_probable_key_length(sequences)

def calculate_ic(text, key_length):
    segment_ic_values = []

    for i in range(key_length):
        segment = text[i::key_length]
        segment = segment.upper()
        
        letter_frequencies = [0] * 26
        total_letters = 0

        for char in segment:
            if 'A' <= char <= 'Z':
                letter_frequencies[ord(char) - ord('A')] += 1
                total_letters += 1

        ic = 0.0

        for j in range(26):
            ic += (letter_frequencies[j] * (letter_frequencies[j] - 1)) / (total_letters * (total_letters - 1))

        segment_ic_values.append(ic)

    return segment_ic_values

best_key_length = None
best_avg_ic = 0.0
for key_length in probable_lengths:
    ic_values = calculate_ic(ciphertext, key_length)
    avg_ic = sum(ic_values) / len(ic_values)
    if(avg_ic > best_avg_ic):
        best_avg_ic = avg_ic
        best_key_length = key_length

def generate_substrings(text, m):
    substrings = []
    for i in range(m):
        substring = text[i::m]
        substrings.append(substring)

    return substrings

substrings = generate_substrings(ciphertext, best_key_length)

def count_letters(text):
    letter_count = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    text = text.upper()
    for char in text:
        if 'A' <= char <= 'Z':
            letter_count[char] += 1
    return letter_count

letter_frequencies = {'A': 0.115, 'I': 0.098, 'O': 0.090, 'E': 0.084, 'N': 0.066, 'S': 0.056, 'R': 0.054, 
                    'J': 0.051, 'T': 0.048, 'U': 0.043, 'D': 0.037, 'K': 0.036, 'V': 0.035, 'L': 0.033, 
                    'M': 0.031, 'P': 0.029, 'C': 0.028, 'Z': 0.023, 'G': 0.016, 'B': 0.015, 'H': 0.008, 
                    'F': 0.003, 'Q': 0.000, 'X': 0.000, 'Y': 0.000, 'W': 0.000}
letter_frequencies = dict(sorted(letter_frequencies.items(), key=lambda item: item[0]))

def calculate_index_of_max_weighted_sum(text):
    max_i = 0
    max_total_weighted_sum = 0.0
    letter_frequencies_list = list(letter_frequencies.values())

    letter_count = count_letters(text)  
    values_list = list(letter_count.values())
    rotations = [values_list]

    for i in range(1, len(values_list)):
        rotated_list = values_list[-i:] + values_list[:-i]
        rotations.append(rotated_list)
        
    total_weighted_sum = 0

    for i in range(26):
        total_weighted_sum = 0
        for j in range(26):
            total_weighted_sum += letter_frequencies_list[j] * rotations[i][j]
        total_weighted_sum /= 26
        if(total_weighted_sum > max_total_weighted_sum):
            max_total_weighted_sum = total_weighted_sum
            max_i = i

    return max_i

key = ''
for i, substring in enumerate(substrings):
    index = calculate_index_of_max_weighted_sum(substring)
    key += chr(65 + 26 - index)
print("Key: " + key)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    key = key.upper()

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)

print("Decrypted text: " + vigenere_decrypt(ciphertext, key))