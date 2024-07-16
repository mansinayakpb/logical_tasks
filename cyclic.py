# cyclic

number = int(input("Enter Number:"))


def cyclic(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number




print(cyclic(number))
