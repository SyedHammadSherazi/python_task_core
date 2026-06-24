# "Raise a custom error if an entered age is less than 0."
age=int(input("Enter your age:"))
if age<0:
    raise ValueError("your age is less then zero")
else:
    print("age is greater then zero requirement is less then zero ")