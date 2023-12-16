def hex_to_binary(hex_list):
    binary_list = []
    for hex_val in hex_list:
        binary_val = bin(int(hex_val, 16))[2:].zfill(8) 
        binary_list.append(binary_val)
    return binary_list

# Funkcija za zbrajanje polinoma u polju GF(2^8)
def add_polynomials(poly1, poly2):
    result = []
    for i in range(len(poly1)):
        # Zbrajanje bitova polinoma i korištenje XOR operacije
        sum_bit = bin(int(poly1[i], 2) ^ int(poly2[i], 2))[2:].zfill(8)
        result.append(sum_bit)
    return result

def binary_to_polynomial(bin_list):
    polynomial = []
    for i, coeff in enumerate(bin_list[::]):
        if coeff == '1':
            power = len(bin_list) - i - 1
            if power == 0:
                polynomial.append('1')  # Dodajemo konstantu 1 ako je potencija 0
            else:
                polynomial.append(f"x^{power}")  
    return polynomial

# Lista heksidecimalnih vrijednosti koje treba zbrojiti u polju GF(2^8)
hex_list = ['60', '8D', '7A', '37']

binary_list = hex_to_binary(hex_list)

# Zbrajanje polinoma
sum_poly = binary_list[0]
for poly in binary_list[1:]:
    sum_poly = add_polynomials(sum_poly, poly)
sum_poly = [poly.lstrip('0') if poly != '00000000' else '0' for poly in sum_poly]

# Ispis
print(sum_poly)
sum_polynomial = binary_to_polynomial(sum_poly)

if sum_polynomial:
    print("Polinom:", ' + '.join(sum_polynomial))
else:
    print("Polinom: 0")

binary_number = ''.join(sum_poly)
hex_result = hex(int(binary_number, 2))[2::].upper()
print("Heksadecimalni rezultat zbrajanja:", hex_result)