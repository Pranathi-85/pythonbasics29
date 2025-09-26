# Program: Count Numbers Divisible by 6, 9, and Both (Range: 10–100)
# This program counts how many numbers between 10 and 100 (inclusive) are divisible by:
#  6
#  9
#  Both 6 and 9

count_6 = 0       # Counter for numbers divisible by 6
count_9 = 0       # Counter for numbers divisible by 9
bothcount = 0     # Counter for numbers divisible by both 6 and 9

# Loop through numbers 10 to 100
for i in range(10, 101):
    if i % 6 == 0 and i % 9 == 0:   # Divisible by both
        bothcount += 1
    if i % 6 == 0:                  # Divisible by 6
        count_6 += 1
    if i % 9 == 0:                  # Divisible by 9
        count_9 += 1

# Display the results
print("Numbers divisible by 6:", count_6)
print("Numbers divisible by 9:", count_9)
print("Numbers divisible by both 6 and 9:", bothcount)

O/P:
Numbers divisible by 6: 15
Numbers divisible by 9: 10
Numbers divisible by both 6 and 9: 5
