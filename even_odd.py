number = int(input("enter no."))
def odd_even(number):
    odd = sum(int(digit) for digit in str(number) if int(digit) % 2 != 0)
    even = sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)
    return {"odd_sum": odd, "even_sum": even}
print(odd_even(number)) 