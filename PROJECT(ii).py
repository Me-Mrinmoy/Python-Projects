import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
  userGuess = int(input("Enter your guess:"))
  if(userGuess==randNumber):
        print("You guessed it right")
  else:
    if(userGuess>randNumber):
       print("You guessed it wrong! Enter a smaller number")
    else:
       print("You guessed it wrong! Enter a larger number")
    guesses += 1
    print(f"You guessed the number in {guesses} guesses")

with open("myscore.txt", "r") as f:
   myscore = int(f.read())

if (guesses<myscore):
   print("You have just roken the high score!")
   with open("myscore.txt", "w") as f:
     f.write(str(guesses))   
     