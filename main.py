print('''
               Made by shashi
            |------------------------------------------|
            |1 - Addition                              |
            |2 - Subtraction                           |
            |3 - Division                              |
            |4 - Multiplication                        |                               
            |------------------------------------------|

            ''')

a = int(input("Choose your operator 1,2,3,4 : "))

num1 = int(input("Enter your first number : "))

num2 = int(input("Enter your second number : "))

if a == 1:
    print("The Addition of " ,num1, "+" ,num2, "=", num1 + num2)

elif a == 2:
    print("The Subtraction of " ,num1, "-" ,num2, "=", num1 - num2)

elif a == 3:
    print("The Division of " ,num1, "/" ,num2, "=", num1 / num2)

elif a == 4:
    print("The Multiplication of " ,num1, "*" ,num2, "=", num1 * num2)

else :
    print("Invalid input")
