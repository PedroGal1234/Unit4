#Pedro Gallino
#10/27/17
#factorial.py - finds factorial using recursion

def factorial(n):
    if n == 1:
        return(n)
    else:
        return n*factorial(n-1)
        
        
print(factorial(5))





