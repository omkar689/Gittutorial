# Day 31  Set

# s = {2, 4, 6, 2}
# print(s)
# print(type(s))

# info = {"dfg", 23, 50.6, True, 5 }
# print(info)
# print(type(info))

# # gf = {}
# # print(type(gf))    this will show dict

# gf = set()
# print(type(gf))     


# Day 32 Set methods

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}     # all elements in both set will print but the repeated 1 will print only 1 time
# cities3 = cities.union(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}      # common in both set will print
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.intersection(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.intersection_update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}     # common in both set will not print and uncommon in both will print
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities.symmetric_difference_update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}       # common in both set will not print and only set1 will print
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
# print(cities.difference(cities2))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Delhi", "Madrid"}
# print(cities2.issubset(cities))

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Helsinki", "Warsaw", "Seoul"}
# cities.update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul")
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# item = cities.pop()
# print(cities)
# print(item)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

# info = {"Carla", 19, False, 5.9}
# if "Carla" in info:
#     print("Carla is present.")
# else:
#     print("Carla is absent.")


# Day 33 Dictonary

# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.items())
# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 


# Day 34 Dictonary methods

# ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
# ep2 = {222: 67, 566: 90}

# # ep1.update(ep2)
# # ep1.clear()
# # ep1.pop(122)
# ep1.popitem()
# # del ep1[122]
# print(ep1) 


# Day 35 else in for

# i = 0
# while i<7:
#   print(i)
#   i = i + 1
#   # if i == 4:
#   #   break

# else:
#   print("Sorry no i")

# for x in range(5):
#     print ("iteration no {} in for loop".format(x+1))
# else:
#     print ("else block in loop")
# print ("Out of loop")


# Day 36  Error handling

# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")
## except Exception as e:
##   print("e")

# print("Some imp lines of code")
# print("End of program")

# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")


# Day 37 

# def func1():
#   try:
#     l = [1, 5, 6, 7]
#     i = int(input("Enter the index: "))
#     print(l[i])
#     return 1
#   except:
#     print("Some error occurred")
#     return 0

#   finally:
#     print("I am always executed")
#   # print("I am always executed")


# x = func1()
# print(x)


# Day 38


a = input("Enter any value between 5 and 9 ")

if(a == "quit"):
    print("quit")
elif(int(a)<5 or int(a)>9):
    raise ValueError("Value should be between 5 and 9")
 