#  Ask the user for a number — if they type text, ask again (handle ValueError). 
while True:
    try:
        number=int(input("Enter the valid number: "))
        print("input number is valid: ", number)
        break
    except:
        print("invalid input try it again : ")
        

