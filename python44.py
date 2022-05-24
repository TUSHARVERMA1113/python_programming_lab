# hourglass star pattern
n = 5

# downward pyramid
for i in range(n-1):
    for j in range(i):
        print(' ', end='')
    for k in range(2*(n-i)-1):
        print('*', end='')
    print()
