# Program: Prime Number Checker
# This program checks whether a given number 'x' is prime or not.
# A prime number is a number greater than 1 that has exactly
# two divisors: 1 and itself.

x = int(input("Enter a number: "))  # Take input from user
count = 0                           # Initialize divisor counter
# Loop to count number of divisors of x
for i in range(1, x + 1):
    if x % i == 0:
        count += 1
# If count of divisors is 2 → prime, else not prime
if count == 2:
    print("prime")
else:
    print("not prime")
O/P:
Enter a number: 13
    prime

##8

# Program: Print Alphabets Using ASCII Values
# This program prints alphabets starting from 'a' based on even numbers.
# It takes an input number 'x' and prints the characters corresponding
# to ASCII values (97 + i) for every even i from 0 to x.

x = int(input("Enter a number: "))  # Take input from user

# Loop through 0 to x with step 2 (even numbers)
for i in range(0, x + 1, 2):
    print(chr(97 + i), end=" ")     # Convert number to corresponding ASCII character and print
O/P:
Enter a number: 25
a c e g i k m o q s u w y

##9

# Program: Print Alphabets with Increasing ASCII Steps
# This program prints lowercase alphabets starting from 'a' (ASCII 97),
# but the step between consecutive letters increases by 1 each time.
# Example sequence: a c f j o ...

ch = 97      # Starting ASCII value ('a')
i = 2        # Initial step increment

# Loop until character exceeds 'z'
while ord('z') >= ch:
    print(chr(ch), end=" ")  # Convert ASCII to character and print
    ch = ch + i               # Increase ASCII value by step i
    i += 1                    # Increment step by 1
O/P:
a c f j o u

#24/09

##10

##printing 1 to 20 prime numbers
# Program: Print Prime Numbers in a Range
# This program prints all prime numbers between 3 and 18 (inclusive).
# A prime number is a number greater than 1 that has exactly two divisors: 1 and itself.
# Loop through numbers from 3 to 18
for x in range(3, 19):
    c = 0  # Counter to count number of divisors

    # Loop to count divisors of x
    for y in range(1, x + 1):
        if x % y == 0:
            c += 1

    # If number of divisors is 2 → prime
    if c == 2:
        print(x, end=" ")  # Print prime number
O/P:3 5 7 11 13 17

##11

# Program: Print Prime Numbers in a Range
# This program prints all prime numbers between two user-specified numbers (a and b).
# A prime number is a number greater than 1 that has exactly two divisors: 1 and itself.
# Taking input from user
a = int(input("Enter the  number ))
b = int(input("Enter the  number ))

# Loop through all numbers from a to b-1
for i in range(a, b):
    # Check if i is prime
    for j in range(2, i):
        if i % j == 0:  # If divisible by any number other than 1 and itself
            break
    else:
        # Executed if the loop is not broken → i is prime
        print(i)

O/P:
enter number 1
enter number 20

##12

# Program: Print Prime Numbers in a Range with Count
# This program prints all prime numbers between two user-specified numbers (a and b)
# and counts the total number of primes found in that range.
# A prime number is a number greater than 1 with exactly two divisors: 1 and itself.

# Initialize prime counter
c = 0
# Take input from user
a = int(input("Enter the starting number ))
b = int(input("Enter the ending number ))

# Loop through all numbers from a to b
for i in range(a, b + 1):
    # Check if i is prime
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        # i is prime
        c += 1
        print(i, end=" ")  # Print prime number
        c%2==0
O/P:
enter number1
enter number20
1 2 3 5 7 11 13 17 19

##13

# Program: Print Alternate Prime Numbers in a Range
# This program prints every alternate prime number between two
# user-specified numbers 'a' and 'b'.
# It defines a function to check if a number is prime.

# Take input from user
a = int(input("Enter the starting number "))
b = int(input("Enter the ending number  "))

# Function to check if a number is prime
def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True
# Counter for alternate prime numbers
c = 0

# Loop through the range a to b (inclusive)
for i in range(a, b + 1):
    if isprime(i)==True:
        c += 1
        # Print only alternate prime numbers (odd count)
        if c % 2 == 1:
            print(i,end=" ")
o/p:
Enter the starting number (a): 2
Enter the ending number (b): 20
2 5 11 17

##14

# Program: Prime Numbers between 2 and 27
# This program prints all prime numbers between 2 and 27.
# It defines a function isprime() to check if a number is prime.

# Function to check if a number is prime
def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# Loop from 2 to 27 and print prime numbers
for i in range(2, 27):
    if isprime(i):
        print(i, end=" ")