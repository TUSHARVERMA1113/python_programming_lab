print("The character pattern ")  
asciiValue = int(input("Enter the ASCII value to print pattern: "))  
# User - define value  
if (asciiValue >= 65 or asciiValue <=122):  
    for i in range(0, 5):  
        for j in range(0, i + 1):  
            # It will convert the ASCII value to the character  
            alphabate = chr(asciiValue)  
            print(alphabate, end=' ')  
        print()  
else:  
    print("Enter the valid character value")  
