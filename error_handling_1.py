
# Build a calculator that doesn't crash on divide-by-zero, but shows a message
# instead.
try:
    number=int(input("Enter the number : ")) 
    operator_sy=(input("Enter the operator : "))
    number1=int(input("Enter the number : ")) 

    if number + number1 and operator_sy== "+":
            number3=number + number1
            print("The Sum of number: ", number3)
    elif number * number1 and operator_sy=="*":
            number3=number * number1
            print("The product of number : ", number3 )
    elif number / number1 and operator_sy=="/":
            number3=number / number1
            print("The Number is divided by : ", number3)

    elif number ** number1 and operator_sy=="**":
            number3 = number ** number1
            print("power of two number is :", number3)
except:
    print("You cannot divided by zero")