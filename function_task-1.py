# Write a function is_prime(n) that returns whether a number is prime
def _prime_num(n):
    if n==1:
        return False
    elif n==2:
        return True
    else:
     for x in range(2,n):
        if n % x==0:
            return False
        return True
print(_prime_num(7)) 
# print(_prime_num(8))     