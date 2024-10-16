def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

def prime_numbers_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Get input from user
limit = int(input("Enter the upper limit to find prime numbers: "))

# Generate prime numbers
if limit <= 1:
    print("There are no prime numbers up to 1.")
else:
    primes = prime_numbers_up_to(limit)
    print(f"Prime numbers up to {limit}: {primes}")
