currentNumber = 1

stop = 2

rows = 3 # Rows you want in your pattern

for i in range(rows):

    for column in range(1, stop):

        print(currentNumber, end=’ ‘)

        currentNumber += 1

    print(“”)

    stop += 2
