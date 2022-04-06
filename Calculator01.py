# This is Python Calculator 

print("Fastcal.1.0 \n Hi, Welcome To Python Calculator Project")
print("") 
print("What is Your Job ? ")
print("1. Add       :   + ")
print("2. Subtract  :   - ")
print("3. Multiply  :   * ")
print("4. Divide    :   / ")
print("5. Power     :   ^ ")
print("6. Remainder :   % ")
print("7. Terminate : if You can Exit")
print(" ")

Choice = int(input("Slelct Your Operation : "))

if Choice == 1:
    num1 = int(input("Enter Your 1st Operand : "))
    num2 = int(input("Enter Your 2nd operand : "))
    #print(num1 + num2)
    out = num1 + num2
    print("Your Result is : \n " , num1 , "+", num2 , "=" , out)
elif Choice == 2:
    num1 = int(input("Enter Your 1st Operand : "))
    num2 = int(input("Enter Your 2nd operand : "))
    out = num1 - num2
    print("Your Result is : \n " , num1 , "-", num2 , "=" , out)
elif Choice == 3:
    num1 = int(input("Enter Your 1st Operand : "))
    num2 = int(input("Enter Your 2nd operand : "))
    out = num1 * num2
    print("Your Result is : \n " , num1 , "*", num2 , "=" , out)
elif Choice == 4:
    num1 = int(input("Enter Your 1st Operand : "))
    num2 = int(input("Enter Your 2nd operand : "))
    out = num1 / num2
    print("Your Result is : \n " , num1 , "/", num2 , "=" , out)
elif Choice == 5:
    num1 = int(input("Enter Your 1st Operand : "))
    num2 = int(input("Enter Your 2nd operand : "))
    out = num1 ^ num2
    print("Your Result is : \n " , num1 , "^", num2 , "=" , out)
elif Choice == 6:
    num1 = int(input("Enter Your 1st Operand : "))
    num2 = int(input("Enter Your 2nd operand : "))
    out = num1 % num2
    print("Your Result is : \n " , num1 , "%", num2 , "=" , out)
elif Choice == 7:
    print("Programe is Exit Successful!!!")
    exit()
else:
    print("Invalid Operation")
    