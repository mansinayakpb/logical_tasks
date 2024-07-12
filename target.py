lists = [1, 2, 3, 4, 5, 6, 7, 8,]
target = int(input())
for digit in lists:
    for num in lists[digit:]:
        if (digit + num) == target:
            print('{},{}'.format(digit,num))
