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


# Ulazni polinomi
polynomial1 = [1, 1, 0, 1, 1, 1, 0, 1]  # x^7 + x^6 + x^4 + x^3 + x^2 + 1
polynomial2 = [1, 1, 1, 0, 0, 0, 1]     # x^6 + x^5 + x^4 + 1

# Množenje polinoma
result = multiply_polynomials(polynomial1, polynomial2)

# Ispis rezultata
print("Rezultat množenja polinoma:")
print(print_polynomial(result))

# Polinom g(x) = x^8 + x^4 + x^3 + x + 1
g_x = [1, 0, 0, 0, 1, 1, 0, 1, 1]

# Dijeljenje polinoma
remainder = divide_polynomials(result, g_x)

# Ispis ostataka
print("\nOstatak pri dijeljenju polinoma polinomom g(x):")
print(print_polynomial(remainder))

# Konverzija ostataka u heksadecimalni i binarni oblik
hex_result = ''.join(str(i) for i in remainder[::])
hex_result = hex(int(hex_result, 2))[2:].upper()
print(f"\nHeksadecimalni zapis ostataka: {hex_result}")
print(f"Binarni zapis ostataka: {bin(int(hex_result, 16))[2:]}")
