##1
##Printing Even Numbers
x=int(input("enter number")) ## x=20
for i in range (1,x): #i=1,2,3,4,5,6,7,8,9....20)
    if x%2==0: ## 20%2==0 true
        if i==x-2:##  1==20-2(1==18) false , 2==20-2(2==18) false, .....18==20-2(18=18) true
            print(i,end=".")
        elif i%2==0: ## 1%2==0 false,2%2==0 true (so 2 will print),3%2==0 false,4%2==0 true ,....16%2==0 true
            print(i,end=",")
    else:
        if i==x-1:
            print(i,end=".")
        elif i%2==0:
            print(i,end=",")
O/P :2,4,6,8,10,12,14,16,18.


##2

## Program: Print Even Numbers up to N
# This program takes a number 'x' as input and prints
# all even numbers starting from 2 up to the largest even
# number less than or equal to x.
a = 2
b = 0
x = int(input("Enter a number: "))   # Taking user input # x=20

# If x is even, set b = x - 2
# If x is odd, set b = x - 1
if x % 2 == 0:  #20 %2==0
    b = x - 2  # b= 20-2  ,b=18
else:
    b = x - 1
# Loop from 2 to b, step 2
for i in range(a, b, 2): ( 2,18)
    print(i, end=",")    # Print with comma

# Finally print the last value (b)
print(b, end=".")

O/P:2,4,6,8,10,12,14,16,18.


##3

## Program: Print Even Numbers with Special Formatting
## This program prints numbers from 1 to 10,

for i in range(1, 11):          # Loop from 1 to 10
    if i == 10:                 # Rule 1: If number is 10
        print(i, end=".")
    elif i % 2 == 0:            # Rule 2: If number is even
        print(i, end=",")
O/P:2,4,6,8,10.