#Pedro Gallino
#10/23/17
#warmUp11.py - does prime functions

def isPrime(n):
    x = 2
    while x < n:
        if n%x == 0:
            return False
        n += 1
    return True

print(isPrime(5))
