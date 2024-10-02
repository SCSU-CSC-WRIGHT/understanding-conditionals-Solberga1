##########=====Temperature Check=====##########

#Get the temperature
temp_celcius=float(input("What is the temperature in celcius today: "))

#Establish the weather of the day
if temp_celcius>30:
    print("It's a hot day.")
else:
    print("The weather is cool.")

##########=====Number Comparison=====##########

#Get the user's numbers
number_1=float(input("Please enter a number: "))
number_2=float(input("Please enter another number: "))

#Establish if the numbers are larger than one another or if they're equal
if number_1>number_2:
    print("Your first number is larger.")
elif number_1<number_2:
    print("Your second number is larger.")
else:
    print("Your numbers are equal.")

##########=====Password Checker=====##########

#Set the admin password
password="abc123"

#User enters password
user_password=input("Enter your password: ")

#Determine if password is proper
if password==user_password:
    print("Access granted.")
else:
    print("Access denied.")

##########=====Simple Calculator=====##########

#Get User's numbers
user_num1=float(input("Please choose a number: "))
user_num2=float(input("Please choose a second number: "))

#Get operator
op=input("Enter an operator: ")

#Do the math
if op=="+":
    print(user_num1+user_num2)
elif op=="*":
    print(user_num1*user_num2)
elif op=="-":
    print(user_num1-user_num2)
else:
    print(user_num1/user_num2)

##########=====Positive, Negative, or Zero=====##########

#Asks user for number
num_choice=float(input("Enter any number: "))

#Determine what kind of number was entered
if num_choice>0:
    print("You chose a positive number.")
elif num_choice<0:
    print("You chose a negtive number")
else:
    print("You chose 0")

##########=====Day of the Week=====##########

#Assign each day of the week a number 1-7
sunday=int(1)
monday=int(2)
tuesday=int(3)
wednesday=int(4)
thursday=int(5)
friday=int(6)
saturday=int(7)

#User picks their number 1-7
day_choice=int(input("Please enter a number 1-7: "))

#State the day
if day_choice==1:
    print("Your day is Sunday.")
elif day_choice==2:
    print("Your day is Monday")
elif day_choice==3:
    print("Your day is Tuesday")
elif day_choice==4:
    print("Your day is Wednesday.")
elif day_choice==5:
    print("Your day is Thursday.")
elif day_choice==6:
    print("Your day is Friday")
elif day_choice==7:
    print("Your day is Satuday.")
else:
    print("Error: your number is not within the given range")