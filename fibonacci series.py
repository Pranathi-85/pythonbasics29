##1
# Fibonacci series using a for loop

# Take input from the user for the number of terms
x = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Loop to generate the Fibonacci series up to x terms
for i in range(1, x + 1):
    print(a, end=" ")  # Print the current Fibonacci number
    c = a + b          # Calculate the next Fibonacci number
    a = b              # Update a to the previous b
    b = c              # Update b to the newly calculated Fibonacci number
Input:
Enter the number of terms: 7
Output:
0 1 1 2 3 5 8 

##2

# Fibonacci Series up to a given number using while loop
# Ask the user to input a number
x = int(input("Enter the value of x: "))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Generate and print Fibonacci numbers until 'a' exceeds x
while a <= x:
    print(a, end=" ")  # Print current Fibonacci number
    c = a + b          # Compute the next Fibonacci number
    a = b              # Shift 'a' to next number
    b = c              # Shift 'b' to next number
Input:
Enter the value of x: 10
Output:
0 1 1 2 3 5 8

##3

# Fibonacci Characters Program
# This program prints letters of the alphabet according to Fibonacci sequence positions.

# Take input from the user
x = int(input("Enter the limit (x): "))

# Initialize the first two Fibonacci numbers
a = 0
b = 1

# Generate Fibonacci sequence and print corresponding characters
for i in range(1, x):
    print(chr(97 + a), end=" ")  # chr(97) = 'a', 97 + a gives the alphabet
    if a > x:  # Stop if the Fibonacci number exceeds x
        break
    c = a + b  # Next Fibonacci number
    a = b
    b = c
Input:
Enter the limit (x): 10
Output:
a b b c d f i

##4

# Program to print letters corresponding to Fibonacci numbers using a while loop

# Initialize first two Fibonacci numbers
a = 0
b = 1

# Loop until the Fibonacci number reaches 26 (number of letters in the alphabet)
while a < 26:
    # Print the character corresponding to the current Fibonacci number
    # chr(97 + a) converts 0 -> 'a', 1 -> 'b', 2 -> 'c', etc.
    print(chr(97 + a), end=" ")
    
    # Update Fibonacci numbers
    c = a + b
    a = b
    b = c
Output:
a b c f k u

##5

# Program: Fibonacci Numbers Between a Range
# This program prints Fibonacci numbers that lie between two given numbers x and y.
# Fibonacci sequence starts with 0 and 1, and each subsequent term
# is the sum of the previous two.

# Initialize first two Fibonacci numbers
a = 0
b = 1

# Take input for range limits
x = int(input("Enter the starting number (x): "))
y = int(input("Enter the ending number (y): "))

# Generate Fibonacci numbers until b exceeds y
while a <= y:
    # Print only if Fibonacci number lies in the range [x, y]
    if a >= x:
        print(a)
    c = a + b   # Next Fibonacci number
    a = b       # Update a
    b = c       # Update b
O/P:
enter number1
enter number10
0
1
5
21

##6
# Program: Fibonacci Printing on Prime Numbers in a Range

# This program checks for prime numbers between two given numbers (g and h).
# For every prime number found, it prints the current Fibonacci number.
# (Note: Logic is kept exactly as provided.)

# Function to check prime
def isprime(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

# Take input range
g = int(input("enter number: "))
h = int(input("enter number: "))

# Initialize Fibonacci starting values
a = 0
b = 1

# Loop through numbers in range [g, h]
for i in range(g, h + 1):
    if (isprime(i)):
        print(a)
    c = a + b
    a = b
    b = c
O/P:
enter number1
enter number10
0
1
1
3
8


