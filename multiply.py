#Pedro Gallino
#10/25/17
#multiply.py - multiplying game

from random import randint

numCorrect = 0

while numCorrect < 5:
    num1 = randint(0,12)
    num2 = randint(0,12)
    question = 'What is '+ str(num1) + 'x' + str(num2) + '?'
    awnser = int(input(question))
    if num1*num2 == awnser:
        print('Correct!')
        numCorrect += 1
    else:
        print('Sorry thats Incorrect')
print("Congratiolations! You Win!")

