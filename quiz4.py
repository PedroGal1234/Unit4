#Pedro Gallino
#10/30/17
#quiz4.py - my fourth proggraming quiz on functions

def csia():
    for i in range(0,5):
        print('computer science is awesome')

def average(x,y,z):
    return ((x+y+z)/3)

def lastLetter(word):
    end = len(word)
    times = 0
    for ch in word:
        times += 1
        if times == end:
            return ch

def same(a,b):
    if a == b:
        return True
    else:
        return False
        

csia()
print(average(1,2,3))
print(lastLetter('Smedinghoff'))
print(same(2*3,7-1))
