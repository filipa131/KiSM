def square_and_multiply(base, exponent, modulus=None):
    result = 1

    binary_exponent = bin(exponent)[2:]

    for bit in binary_exponent:
        print(f"Result at the beginning of iteration: {result}")
        print(f"Current bit in binary exponent: {bit}")

        result = (result ** 2) % modulus if int(bit) == 0 else (result ** 2 * base) % modulus

        print(f"Result after squaring/multiplying: {result}")
        print("----------")

    return result

# Example usage:
base = 2
exponent = 3280337
modulus = 18597437 

result = square_and_multiply(base, exponent, modulus)
print(f"{base}^{exponent} mod {modulus} = {result}")
