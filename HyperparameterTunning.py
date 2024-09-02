import pandas as pd 
while(True):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_primes(limit):
        primes = []
        for num in range(2, limit):
            if is_prime(num):
                primes.append(num)
        return primes

    if __name__ == "__main__":
        limit = 100000  # You can increase this limit to make it more CPU intensive
        primes = calculate_primes(limit)
        print(f"Calculated {len(primes)} prime numbers up to {limit}.")
