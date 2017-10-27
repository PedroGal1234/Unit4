#Pedro Gallino
#10/27/17
#warmUp12.py - finds the greatest common factor of two numbers

def GCF(x,y):
    n = y
    while n>0: 
        if x%n == 0 and y%n == 0:
            return n
        else:
            n -= 1
    
print(GCF(20,30))
