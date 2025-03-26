# # Day 11

# name = "oiio"
# st = '''fghjk
# ghj
# oiuy'''

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# # to get to now the index of st it is difficult to count he spaces left to use for loop

# for i in st :
#     print(i)

# # Day 12

# name = "harry"
# print(name[0:5])
# print(name[-1 : len(name)-3])
# print(name[-3:-1])
# print(name[-4 : -2])

# # Day 13

# a = "ghjk"
# b = "!!! ghjk !!!!! "
# c = "!!! ghjk !!!!! jiop"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(b.rstrip("!"))
# print(c.rstrip("!"))
# print(a.replace("ghjk" , "qwer"))
# blogheading = "introduction to abc"
# print(blogheading.capitalize())

# str1 = "Welcome to the conlose!!!"
# print(len(str1))
# print(str1.center(50))
# print(len(str1.center(50)))
# print(a.count("ghjk"))
# print(str1.endswith("!!!"))
# print(str1.endswith("to",4 ,10))

# print(str1.startswith("We"))

# str2 ="He's name is Dan. He si good boy"
# print(str2.find("is"))  #The find() method searches for the first occurrence 
#                         #of the given value and returns the index where it is present. 
#                         #If given value is absent from the string then return -1.

# print(str2.find("ishh"))
# # print(str2.index("ishh"))
# # As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())
# str1 = "Welcome"
# print(str1.isalpha())
# str1 = "Welcome003"
# print(str1.isalpha())

# str1 = "hello world"
# print(str1.islower())

# str1 = "We wish you a Merry Christmas"
# print(str1.isprintable())
# str1 = "We wish you a Merry Christmas\n"
# print(str1.isprintable())

# str1 = "         "       #using Spacebar
# print(str1.isspace())
# str2 = "  "       #using Tab
# print(str2.isspace())

# str1 = "World Health Organization" 
# print(str1.istitle())

# str2 = "To kill a Mocking bird"
# print(str2.istitle())

# str1 = "Python is a Interpreted Language" 
# print(str1.swapcase())

# str1 = "His name is Dan. Dan is an honest man."
# print(str1.title())

# # Day 14 

# # conditional statements like if, if-else, elif, nested if-else



# # Day 16

# # Case statement


# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     # case x:       in this method also we can do
#     #     if x == 0:
#     #         print("x is zero")
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)


# Day 17

# name = 'Abhishek'
# for i in name:
#   print(i)
#   if(i =="b"):
#     print("This is something special!")
    
# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#   print(color)
#   for i in color:
#     print(i)

# for k in range(5):
#   print(k + 1)
  
# for k in range(1, 20001):
#   print(k)

  
# for k in range(1, 12, 3):
#   print(k)

# Day 18

# i = int(input("Enter the number: "))
# print(i)
# while(i<=38):
#   i = int(input("Enter the number: "))
#   print(i)

# print("Done with the loop")

# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1
# else:
#   print("I am inside else")

# Day 19

# for i in range(12):
#   if(i == 10):
#     print("Skip the iteration")
#     continue
#   print("5 X", i, "=", 5 * i)
  
# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if(i%50 == 0):
#     break


# Day 20  functions

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
