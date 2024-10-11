import random
secret_number = random.randint(1, 10)
guessed = False
while guessed == False:
    guess = int(input("Guess a number between 1 and 10 "))
    if guess == secret_number: 
        print("You habe chosen..... Wisely")
        guessed == True
    else: 
        print("Thats the wrong number silly")
