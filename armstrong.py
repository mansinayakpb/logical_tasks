def armstrong_in(number):
    length_str = len(str(number))
    temp = number
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** length_str
        temp = temp//10

    return sum == number


print(armstrong_in(12))


def n_armstrong(number):
    armstrong_num = []
    num = 0
    while len(armstrong_num) < number:
        if armstrong_in(num):
            armstrong_num.append(num)
        num += 1
    return armstrong_num


first_10 = n_armstrong(11)
print(first_10)