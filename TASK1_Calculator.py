print("*****Calculator*****")
print("Press 1 for addition ")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("Press 5 for floor division")

num1 = eval(input("Enter First  number : "))
num2 = eval(input("Enter second number : "))

choice = eval(input("enter a number between 1-5 : "))

if choice == 1:
    print ("the addition of the given two numbers is",num1+num2)
elif choice == 2:
    print ("The subtraction of the given two numbers is",num1-num2)
elif choice == 3:
    print ("The multiplication of the given two numbers is",num1*num2)
elif choice == 4:
    print ("The division of the given two numbers is",num1/num2)
elif choice == 5:
    print("The floor division of the two numbers is",num1//num2)    
else:
    print ("Invalid Input from the User")