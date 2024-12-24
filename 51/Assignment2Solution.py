def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

def is_prime_sieve(n):
    primes = sieve_of_eratosthenes(n)
    return primes[n]

# Example usage
number = int(input("Enter a number: "))
if is_prime_sieve(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
