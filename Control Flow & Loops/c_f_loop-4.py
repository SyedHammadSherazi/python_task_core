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

