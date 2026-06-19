# Guess-the-number game: the program picks a number, the user keeps guessing
# until correct (while loop)
number=9
guess_number=None

while guess_number != number:
    guess_number = int(input("Enter the Guess Number : "))

    if guess_number == number:
           print ("congratulations your number is match")
    elif guess_number != number:
        print("your guess number is not match")

# while guess_number==number and new_number == number:
#     print("you win this game : ")
#     if new_number !=number:
#         input(new_number)
#     elif new_number == number:
#         print("you win this game")
#     else:
#         print("This is number is not correct")
