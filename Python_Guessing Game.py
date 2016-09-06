import random

rand1=int(input("Please Guess your first number? "))
guess= (random.randint(0,9))

'''This code will congratulate player if his first guess in right. Also program will
exit the game.'''
print(guess)
if guess==rand1:
    print("Congratulations!!! ")
    quit()
if guess==rand1-1:
    print("Hot")
elif guess==rand1-2:
    print("Warm")
elif guess != rand1:
    print("Sorry, You lost. Try again ")

import random
rand2=int(input("Please Guess your second number? "))
guess= (random.randint(0,9))   
8
print(guess)
if guess==rand2:
    print("Congratulations!!! ")
    quit()
if guess==rand2-1:
    print("Hot")
elif guess==rand2-2:
    print("Warm")
elif guess != rand2:
    print("Sorry, You lost. Try again. ")

import random

rand3=int(input("Please Guess your third number? "))
guess= (random.randint(0,9))    
print(guess)
if guess==rand3:
    print("Congratulations!!! Good bye!!! ")
    quit()
if guess==rand3-1:
    print("Hot")
    print (" ")
elif guess==rand3-2:
    print("Warm")
    print (" ")
    quit()
elif guess != rand3:
    print("Sorry, You lost. Good Bye!!! ")
    quit()
if guess== rand1 or rand2 or rand3:
    print("Congratulations!!! Good bye!!! ")
    quit()
    print (" ")
elif guess!= rand1 or rand2 or rand3:
    print("Sorry, You lost. Try again. ")
else:
    print("Cold")












