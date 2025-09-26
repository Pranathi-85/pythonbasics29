##5

# Program: Generate Series with Increasing Difference
# This program generates a number series where:
# It starts with 1
# The difference between consecutive numbers increases by 1 each step
# Example: 1, 2, 4, 7, 11, 16, ...

x = int(input("Enter the limit: "))   # Take series limit from user
num = 1                               # First number of the series
diff = 1                              # Initial difference

while num <= x:                       # Loop until number <= limit
    print(num, end=" ")               # Print current number
    num += diff                       # Increase number by current difference
    diff += 1                         # Increment difference
O/P:
Enter the limit: 10
1 2 4 7
