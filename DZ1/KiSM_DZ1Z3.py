"""Dekriptirajte šifrat dobiven supstitucijskom šifrom, i to Cezarovom šifrom s ključnom riječi. 
Poznato je da je otvoreni tekst pisan na hrvatskom jeziku, te da je ključna riječ jedan grad u
Hrvatskoj."""

import copy

def set_difference(keyword, alphabet):
    keyword_set = set(keyword)
    alphabet_set = set(alphabet)
    difference_set = alphabet_set - keyword_set
    return ''.join(sorted(difference_set))

def rotate_string(s, n):
    n = n % len(s)
    return s[n:] + s[:n]

def generate_mapping(keyword, alphabet):
    result = set_difference(keyword, alphabet)
    combined = keyword + result
    mappings = []

    for i in range(26):
        rotated_combined = rotate_string(combined, i)
        mapping = {}
        for j in range(len(alphabet)):
            mapping[rotated_combined[j]] = alphabet[j]
        mappings.append(copy.deepcopy(mapping))

    return mappings

def decrypt_text(text, mapping):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            decrypted_text += mapping[char] if char in mapping else char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    keyword = "DUBROVNIK"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = "WKZTSKZQYUMAZAUZPZVDTQMAOZUENKEAUVDFVDAQZAFVDZRNVACENUVRLMKDTAMFMODTNVBZMBWMPTCAUZYAZWMKMKZDTAZVDTNKVPBTRUVDZDTUKZNCVMOMBZCZQMKTREQZVFZATVSCKZACVXVSZOM"

    mappings = generate_mapping(keyword, alphabet)

    for i, mapping in enumerate(mappings):
        decrypted_text = decrypt_text(cipher, mapping)
        print(f"Decryption {i + 1}: {decrypted_text}")
        print(f"Mapping Used: {mapping}\n")

if __name__ == "__main__":
    main()
