#Pedro Gallino
#10/23/17
#triangle.py tells you the area of a triangle

from math import sqrt
def distance(x1,y1,x2,y2):
    return sqrt(((x2-x1)**2)+((y2-y1)**2))

x1 = int(input('X1 = '))
y1 = int(input('y1 = '))
x2 = int(input('X2 = '))
y2 = int(input('Y2 = '))
x3 = int(input('X3 = '))
y3 = int(input('Y3 = '))

a = distance(x1,y1,x2,y2)
b = distance(x1,y1,x3,y3)
c = distance(x2,y2,x3,y3)
s = .5*(a+b+c)

print(sqrt(s*(s-a)*(s-b)*(s-c)))






