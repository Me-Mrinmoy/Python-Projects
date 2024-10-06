'''This is a simple snake, water and gun game 
in pyton--'''

import random
# Snake Water Gun or Rock Paper Chessars-- 
def gameWin(comp, you):
    # if two values are equal, declare a tie!
    if comp == you:
       return None
    
   # Check for all possibilities when computer choose s(Snake)
    elif comp == 's':
      if you == 'w':
        return False
      elif you == 'g':
         return True
      
    # Check for all possibilities when computer choose w(Water)  
      elif comp == 'w':
         if you == 'g':
            return False
         elif you == 's':
            return True
         
    # Check for all possibilities when computer choose g(Gun)     
         elif comp == 'g':
          if you == 's':
            return False
    elif you == 'w':
            return True
print("Comp Turn: Snake(s) Water(w) or Gun(g)?")         
randNo= random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo== 3:
    comp = 'g' 

# a = input("Comp turn: Snake(s) Water(w) or Gun(g)?")
you = input("Your turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
   print("The game is a tie")
elif a:
   print("You Win!")
else:
   print("You Lose!")    
