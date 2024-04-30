from random import randint
def randomizer():
    return randint(1,20)
print('Hello! What is your name?')
name=input()
print('Well, '+name+',I am thinking of a number between 1 and 20. ')
print('Take a guess.')
x=0
cnt=0
guess=randomizer()
while x!=guess:
    x=int(input())
    cnt+=1
    if x<guess:
        print('Your guess is too low.')
        print('Take a guess.')
    elif x>guess:
        print('Your guess is too high.')
        print('Take a guess.')
    elif x==guess:
        print('Good job, '+name+'! You guessed my number in '+ str(cnt)+' guesses!')
        break