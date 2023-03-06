import random
import time

print("""

Welcome to Number Guessing Game offered by KBTech.
In this game, you have to guess a number between 1 to 50.
Please remember, you have only five attempts to guess the number.
Lets Start...

""")

Rand_Number=random.randint(1,50)
Attempts=5
Counter=0


while True:
    Guess=int(input("Please Enter Your Guess Number: \n"))
    if Attempts!=0:

        if Guess>Rand_Number:
            print("Comparing Results...\n")
            time.sleep(1)
            print("Your Guessed Number is greater than our number: \n")
            Attempts-=1
            Counter+=1
        elif Guess<Rand_Number:
            print("Comparing Results...\n")
            time.sleep(1)
            print("Your Guessed Number is smaller than our number: \n")
            Attempts-=1
            Counter+=1
        else:
            print("Comparing Results... \n")
            time.sleep(1)
            print("Congratulations... You have correctly guessed the number: \n")
            Attempts-=1
            Counter+=1
            break
    else:
        print("You Attempts have been finished... \n")
        break
    
