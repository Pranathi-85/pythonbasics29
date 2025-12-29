# 1. Use map() with a lambda to add 5 to every element of the following nested list
# [[1, 2], [3, 4], [5, 6]]

lst=[[1,2], [3,4], [5,6]]
result=list(map(lambda x: [i + 5 for i in x], lst))
print(result)
# only  add 5 to add 2,4,6
lst=[[1,2], [3,4], [5,6]]
result=list(map(lambda x: x[1]+5, lst))
print(result)


# 2. Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
# filter() to keep only the keys whose values are greater than 50.

d={"apple":100,"banana":40,"cherry":150}

result = dict(filter(lambda x: x[1] > 50, d.items()))
print(result)


# 3. Use functools.reduce() with a lambda to find the largest number from a given
# list Dynamically.

from functools import reduce
num=[45,10,5,8,80]

largest=reduce(lambda a,b: a if a>b else b,num)
print(largest)

# 4. What happens if the lambda passed to reduce() accepts only one parameter or
# three parameters? Explain the output or error

#reduce() always combines two values at a time, so lambda must accept exactly two parameters.
#one parameter
"""from functools import reduce

nums = [1, 2, 3]

reduce(lambda a: a, nums) #here lambda passing only one parameter  but reduce() need two values

#o/p
#TypeError: <lambda>() takes 1 positional argument but 2 were given

#three parameters

from functools import reduce

nums = [1, 2, 3]

reduce(lambda a,b,c: a+b+c, nums) ##here lambda passing three parameter
# but reduce() need two values .python confuses where another value come from
 
#o/p
#TypeError: <lambda>() missing 1 required positional argument: 'c'

# 5. Use map() on a string to convert each character into its ASCII value
# (using ord()). Print the result list.

s="python"
result= list(map(ord,s))
print(result)
"""
# 6. Use filter() to remove all vowels from a string and print the final string.

p="String"
vowels="aeiouAEIOU"
result="".join(filter(lambda ch: ch  not in vowels,p))
print(result)

# 7. Use reduce() to concatenate a list of characters into a single string.
# Example input: ['P', 'y', 't', 'h', 'o', 'n'].
from functools import reduce
p=['P', 'y', 't', 'h', 'o', 'n']
result=reduce(lambda a,b: a+b,p)
print(result)

# 8. Given a list of integers, use map() with id() to print the memory address
# of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

p=[10,350,10,350,20]

result=map(id,p)
print(result)

# 9. Explain the difference between:
# map(str, [1, 2, 3])
# map(lambda x: str(x), [1, 2, 3])
# Which one is faster and why?

p=list(map(str, [1, 2, 3]))
q=list(map(lambda x: str(x), [1, 2, 3]))
print(p)
print(q)

# 10. Given a list of numbers:
# [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers

l=[5,10,15,20,25,30]
result=list(map(lambda x: x**2,l))
print(result)

l=[5,10,15,20,25,30]
result=list(filter(lambda x: x%5==0,l))
print(result)

l=[5,10,15,20,25,30]
result=reduce(lambda x,y: x+y,l)
print(result)

lst=[[1,2], [3,4], [5,6]]
result=list(map(lambda x: x[1]+5, lst))
print(result)


