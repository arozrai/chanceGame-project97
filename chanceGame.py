import random

number=random.randrange(9)
chances=5

print("I have picked a number between 1 to 9, you have 5 chances to guess that number!")
while(chances<=5):
    guess=int(input("Guess the number i have chosen: "))
    if(guess==number):
        print("YOU WIN!!!")
        break
    elif(guess>number):
        print("My number is lower than ",guess)
        chances=chances-1
    else:
        print("My number is higher than ",guess)
        chances=chances-1

if (chances<=0):
    print("YOU LOSE, MY NUMBER WAS ",number)