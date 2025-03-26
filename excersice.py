# # excersice 2

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# a = int(time.strftime('%H'))
# print(a)
# if (a < 12):
#     print("Good Morning")
# elif (a >= 12 or a == 6 ):
#     print("Good Afternoon")
# elif (a >= 6 or a == 9 ):
#     print("Good Evening")
# else:
#     print("Good Night")


moneyprice = 0
print("1 : Which of the three banks will be merged with the other two to create India's third-largest bank?") 
options = print({"A" : "Punjab National Bank", "B" : "Indian Bank" , "C" : "Bank of Baroda", "D" : "Dena Bank"})
Answer = input("Enter the capital letter options : ")
if Answer == "B":
    moneyprice = 1000
    print("Your Answer is right and U won the moneyprice of Rs " ,moneyprice )
else:
    print("Your answer is wrong and the moneyprice is of Rs " ,moneyprice)
    print("U are out of this game try next time")
    exit()

choice =  input("If you want to continue, type 'Yes'; otherwise, type 'No': ")
if choice.lower() == "yes":
    print("Next question will appear")
else:
    print("U exited the game and won the amount of Rs", moneyprice)
    exit()

print("2 : What is the name of the weak zone of the earth's crust?")
options =print({"A": "Seismic", "B": "Cosmic", "C" : "Formic", "D" : "Anaemic"})
Answer = input("Enter the capital letter options : ")
if Answer == "A":
    moneyprice += 1000
    print("Your Answer is right and U won the moneyprice of Rs " ,moneyprice )
    
else:
    print("U exited the game and won the amount of Rs", moneyprice)
