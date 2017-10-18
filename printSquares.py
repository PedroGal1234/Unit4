#Pedro Gallino
#10/18/17
#/printSquares.py - prints a patern of squares

def printSquares(num1,num2):
    for i in range(0,num2):
        if i == 0:
            print('+--'*num1+('+'))
            print('|  '*num1+('|'))
            print('+--'*num1+('+'))
        else:
            print('|  '*num1+('|'))
            print('+--'*num1+('+'))

printSquares(4,4)
