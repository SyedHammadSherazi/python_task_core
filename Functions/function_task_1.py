# Write a function is_prime(n) that returns whether a number is prime  
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(7))   # True
print(is_prime(8))   # False
