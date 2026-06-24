# FizzBuzz: 1 to 50 — "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both. 
for numbers_according_to_fizz in range(1,51):
    if (numbers_according_to_fizz % 3 == 0)  and (numbers_according_to_fizz  % 5 == 0):
        print("The number is FizzBuzz : ",numbers_according_to_fizz )
    elif numbers_according_to_fizz % 3==0:
        print("The number is Fizz : ", numbers_according_to_fizz)
    elif numbers_according_to_fizz % 5==0:
        print("This number is Buzz : ", numbers_according_to_fizz) 
