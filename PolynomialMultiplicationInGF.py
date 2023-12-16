from pyfinite import ffield

# Definiranje polja GF(2^8)
GF = ffield.FField(8, gen=0b100011011)  # x^8 + x^4 + x^3 + x + 1

# Funkcija za množenje polinoma u polju GF(2^8)
def multiply_polynomials(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] ^= GF.Multiply(poly1[i], poly2[j])
    return result

# Funkcija za dijeljenje polinoma u polju GF(2^8) --> vraća ostatak dijeljenja
def divide_polynomials(dividend, divisor):
    while len(dividend) >= len(divisor) and dividend != [0] * len(dividend):
        degree_diff = len(dividend) - len(divisor)
        leading_term = dividend[0]
        quotient = [leading_term] + [0] * (degree_diff - 1)

        divisor_shifted = divisor[:] + [0] * degree_diff
        multiplication_result = multiply_polynomials(quotient, divisor_shifted)
        dividend = [dividend[i] ^ multiplication_result[i] for i in range(len(dividend))]

        # Remove leading zeros in the dividend
        while len(dividend) > 0 and dividend[0] == 0:
            dividend.pop(0)

    return dividend

# Funkcija za pretvorbu binarnog zapisa u polinom
def print_polynomial(poly):
    polynomial_str = ""
    degree = len(poly) - 1

    for i, coef in enumerate(poly):
        if coef != 0:  # Provjeri je li koeficijent različit od nule
            if coef == 1:
                if i == degree:
                    term = f"x^{degree - i}"
                else:
                    term = f"x^{degree - i} + " if degree - i > 1 else "x + "
            elif coef == -1:
                if i == degree:
                    term = f"-x^{degree - i}"
                else:
                    term = f"-x^{degree - i} + " if degree - i > 1 else "-x + "
            else:
                if i == degree:
                    term = f"{coef}x^{degree - i}"
                else:
                    term = f"{coef}x^{degree - i} + " if degree - i > 1 else f"{coef}x + "
            
            polynomial_str += term
    
    # Zamijeni x^0 sa 1
    polynomial_str = polynomial_str.replace("x^0", "1") 

    # Ako je polinom prazan, postavi ga na 0 umjesto praznog stringa
    if polynomial_str == "":
        polynomial_str = "0"
    else:
        # Ukloni mogući višak znakova + i razmaka na kraju polinoma
        polynomial_str = polynomial_str.rstrip(" +")

    return polynomial_str

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

### Ovdje unesite svoje koeficijente 
a = ['03', '7F', 'DA', '8C'] # a0, a1, a2, a3 
b = ['05', '60', '8C', 'EB'] # b0, b1, b2, b3

a_index = [[0, 3, 2, 1],
    [1, 0, 3, 2],
    [2, 1, 0, 3],
    [3, 2, 1, 0]]

sum =  [[0 for _ in range(4)] for _ in range(4)]

for i in range (4):
    for j in range (4):
        hex_num1 = a[a_index[i][j]] 
        hex_num2 = b[j]
        dec_num1 = int(hex_num1, 16)  
        dec_num2 = int(hex_num2, 16)  

        bin_num1 = bin(dec_num1)[2:]
        bin_num2 = bin(dec_num2)[2:]

        polynomial1 = [int(bit) for bit in bin_num1]  
        polynomial2 = [int(bit) for bit in bin_num2]

        # Množenje polinoma
        result = multiply_polynomials(polynomial1, polynomial2)

        # Polinom g(x) = x^8 + x^4 + x^3 + x + 1
        g_x = [1, 0, 0, 0, 1, 1, 0, 1, 1]

        # Dijeljenje polinoma
        remainder = divide_polynomials(result, g_x)

        # Konverzija ostataka u heksadecimalni oblik
        hex_result = ''.join(str(i) for i in remainder[::])
        hex_result = hex(int(hex_result, 2))[2:].upper()
        sum[i][j] = hex_result

for i in range (4):
    binary_list = hex_to_binary(sum[i])

    # Zbrajanje polinoma
    sum_poly = binary_list[0]
    for poly in binary_list[1:]:
        sum_poly = add_polynomials(sum_poly, poly)
    sum_poly = [poly.lstrip('0') if poly != '00000000' else '0' for poly in sum_poly]

    sum_polynomial = binary_to_polynomial(sum_poly)

    binary_number = ''.join(sum_poly)
    hex_result = hex(int(binary_number, 2))[2::].upper()
    print(f"d{i}: {hex_result}")