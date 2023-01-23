def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.append(num)
    return primes


limit = int(input('Enter the limit: '))
print(find_primes(limit))
