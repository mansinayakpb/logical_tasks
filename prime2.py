def f_prime(numbers):
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

print(f_prime([7, 9, 3, 9, 10, 11, 27]))
print(f_prime([10007, 1009, 1007, 27, 147, 77, 1001, 70]))
print(f_prime([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]))
