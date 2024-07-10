def armstrong_in(n):
    length_str = len(str(n))
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** length_str
        temp = temp//10

    return sum == n

print(armstrong_in(12))

def n_armstrong(n):
    armstrong_num = []
    num = 0
    while len(armstrong_num) < n:
        if armstrong_in(num):
            armstrong_num.append(num)
        num += 1
    return armstrong_num

first_10 = n_armstrong(11)
print(first_10)