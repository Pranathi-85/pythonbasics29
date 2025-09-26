# 22/09
# reversing
# Program: Fitbit Game
# Description: This program prints "fit", "bit", or "fitbit"
# based on certain rules applied to numbers from 1 to x.

x = int(input("Enter a number: "))  # Taking user input
flag = 0  # Initial flag set to 0

for i in range(1, x + 1):  # Looping from 1 to x
    if i % 10 == 1:  # Rule 1: If number ends with 1
        print(1)
    if i % 5 == 0:  # Rule 2: If divisible by 5
        print("fitbit")
        if flag:  # flag toggles → becomes 1
            flag = 0
        else:
            flag = 1
    elif i % 2 == flag:  # Rule 3: If number % 2 == flag
        print("fit")
    else:  # Otherwise print "bit"
        print("bit")
O / P:
Enter
a
number: 10
1
bit
fit
bit
fit
fitbit
bit
fit
bit
fit
fitbit
