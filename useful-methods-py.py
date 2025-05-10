import math

#Swap two variables
#a, b = b, a
a, b = 1, 2
print(f"Before swap: a-{a}, b-{b}")
a, b = b, a 
print(f"After: a-{a}, b-{b}\n")

#Reverse a string
#: s[::-1]
s = [1, 2, 3, 4, 5]
print(f"Before reverse: {s}")
s = s[::-1]
print(f"After: {s}\n")

#Check Palindrome
#s == s[::-1]
print(f"Palindrome: {s == s[::-1]}\n")

#Get Factorial
#math.prod(range(1, n+1))
n = 5
factorial = math.prod(range(1, n+1))
print(f"Factorial of {n} is {factorial}")

#Flatten a list
#[i for sub in lst for i in sub]
lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(f"Before flatten: {lst}")
lst = [i for sub in lst for i in sub]
print(f"After: {lst}\n")