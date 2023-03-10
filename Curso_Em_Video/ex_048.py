sum = 0
for i in range(1, 501, 2) :
    if i % 3 == 0 :
        print(i, end = ' ')
        sum += i
print('\nA soma é', sum)
