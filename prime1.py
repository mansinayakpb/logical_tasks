def fprime(numbers):
    def primey(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    primes = []
    for num in numbers:
        if primey(num):
            primes.append(num)
    return primes

print(fprime([7, 9, 3, 9, 10, 11, 27]))