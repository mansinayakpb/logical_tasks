l = [1, 2, 3, 4, 5, 6, 7, 8,]
target = int(input())
for i in l:
    for j in l[i:]:
        if (i + j) == target:
            print('{},{}'.format(i,j))