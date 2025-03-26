# # Day 21

# def average(a, b):
#     print("Average is = ", (a+b)/2)

# average(2,3)  this is keyword argument

# def average(a=2, b=3):
#     print("Average is = ", (a+b)/2)  # this is default argument

# def average(a, b, c):
#     print("Average is = ", (a+b+c)/2)
# average(2,3) required argument becz correct position order shld be passed
# average(2,3,6)


# def average(*numbers):
#     print(type(numbers))
#     sum =0
#     for i in numbers:
#         sum +=i
#         return sum/len(numbers)  ## return arguments
# #     print("average of numbers is = ", sum/len(numbers))
# # average(3,9,8)        ## this is variable-length argumets

# def name(**name):
#   print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")


# Day 22

# marks = [3, 5, 6, "Harry", True, 6, 7 , 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

# if "6" in marks:
#   print("Yes")
# else:
#   print("No")

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")

# print(marks[0:7])
# print(marks[1:9])
# print(marks[1:9:3])

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [i for i in names if len(i)>4]
# print(namesWith_O)

# Day 23

# l = [11, 45, 1, 2, 4, 6, 1, 1]
# print(l)
# l.append(7)
# l.sort(reverse=True)
# l.sort()
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# print(m)
# l.insert(1, 899)
# m = [900, 1000, 1100]
# k = l + m
# print(k)
# l.extend(m)
# print(l)


# Day 24

# tup = (1, 2, 76, 342, 32, "green", True)
# # tup[0] = 90
# print(type(tup), tup)
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[2])
# # print(tup[34])

# if  3421 in tup:
#   print("Yes 342 is present in this tuple")
# print(tup[1:4])
# print(tup)
# tup2 = tup[1:4]
# print(tup2)


# Day 25

# tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# # res = tuple1.count(3)
# # res = tuple1.index(3)
# # res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)  #(no u want , start index, end index)
# print(len(tuple1))
# print('Count of 3 in tuple1 is:', res)


# Day 26 excersice 2 ans
# Day 27 excersice 3 

# Day 28 - f string

# letter = "Hey my name is {1} and I am from {0}"
# country = "India"
# name = "Harry"

# print(letter.format(country, name))
# print(f"Hey my name is {name} and I am from {country}")
# print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
# price = 49.09999
# txt = f"For only {price:.2f} dollars!"
# print(txt)
# # print(txt.format())
# print(f"{2 * 30}")
# print(type(f"{2 * 30}"))


# Day 29  docstring

# def square(n):
# #   print(n)  if docstring is below any statement rather than starting of below function then it is displayed as None
#   '''Takes in a number n, returns the square of n'''
#   print(n**2)
# square(5)
# print(square.__doc__)


# Day 30 Recursion

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
# def factorial(n):
#   if (n == 0 or n == 1):
#     return 1
#   else:
#     return n * factorial(n - 1)


# print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence

def Fibonacci(n):
    
    if n <= 0:
        return n
    elif n == 1 or n == 2:
        return 1
    
    else:
        
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(9))

 
# Driver Program
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....