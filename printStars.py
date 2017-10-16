#Pedro Gallino
#10/16/17
#printStars.py - print lines of stars equal to an intiger

def stars(num1):
    i = 1
    space = num1
    while i<num1+1:
        print(' '*space,'*'*i)
        i += 2
        space = space-1

stars(30)
