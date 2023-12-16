from random import randint
import math

def is_prime_number(num):
    for i in range(2, math.floor(math.sqrt(num))):
        if num % i == 0:
            return False
    return True

def find_next_prime_number(m):
    x = m
    while True:
        if is_prime_number(x):
            return x
        elif x == 9999:
            return find_next_prime_number(randint(1000, 9999))
        else:
            x += 1

def are_relative_primes(e, fi):
    for i in range(2, min(e, fi) + 1):
        if e % i == 0 and fi % i == 0:
            return False
    return True

def find_euler_totient(fi):
    max_val = 99999 if fi - 1 > 99999 else fi - 1
    while True:
        e = randint(10000, max_val)
        if are_relative_primes(e, fi):
            return e

def find_modular_inverse(e, fi):
    for d in range(1, fi):
        if (d * e) % fi == 1:
            return d
    return -1

# Example values 
p_value = 6761
q_value = 9461
n_value = p_value * q_value
fi_value = (p_value - 1) * (q_value - 1)
e_value = 36141

plain_text_value = 123420
cipher_text = plain_text_value ** e_value % n_value

print(find_modular_inverse(e_value, fi_value))
