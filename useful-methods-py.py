import math
from collections import Counter

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
print(f"Factorial of {n} is {factorial}\n")

#Flatten a list
#[i for sub in lst for i in sub]
lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(f"Before flatten: {lst}")
lst = [i for sub in lst for i in sub]
print(f"After: {lst}\n")

#Find even numbers
#[x for x in range(10) if x % 2 == 0]
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers between 0 & 10: {evens}\n")

#Merge two dictionaries
#{**d1, **d2}
d1 = {1: "language", 2: "of", 3: "one"}
d2 = {4: "understood", 5: "by", 6: "none"}
d3 = {**d1, **d2}
print(f"Merged dicts: {d3.values()}\n")

#Count items
#Counter(lst)
duplicates = [1, 1, 2, 3, 5, 5, 5, 5]
countIterable = Counter(duplicates)
print(f"Count iterable: {countIterable}\n")

#Get unique elements
#set(lst)
setDuplicates = set(duplicates)
print(f"Unique elements of duplicates: {setDuplicates}\n")

#List to string
#''.join(lst)
stringDuplicates = ' '.join(d3.values())
print(f"List to string for d3 values: {stringDuplicates}")