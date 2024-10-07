import random

print("Welcome to Connect Four")
print("-----------------------")

possibleLetters = ["A","B","C","D","E","F","G"]
gameBoard = [["","","","","","",""], ["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""],["","","","","","",""]]
rows = 6
cols = 7

def printGameBoard():
  print("\n     A    B    C    D    E    F    G  ", end="")
  for x in range(rows):
    print("\n   +----+----+----+----+----+----+----+")
    print(x, " |", end="")
    for y in range(cols):
      if(gameBoard[x][y] == "🔵"):
        print("",gameBoard[x][y], end=" |")
      elif(gameBoard[x][y] == "🔴"):
        print("", gameBoard[x][y], end=" |")
      else:
        print(" ", gameBoard[x][y], end="  |")
  print("\n   +----+----+----+----+----+----+----+")

def modifyTurn(spacePicked, turn):
  gameBoard[spacePicked[0]][spacePicked[1]] = turn

turnCounter = 0
while True:
  printGameBoard()
  if turnCounter % 2 == 0:
    turn = "🔴"
  else:
    turn = "🔵"

  columnLetter = input("Player " + turn + ", choose a column (A-G): ")
  while columnLetter.upper() not in possibleLetters:
    print("Invalid column. Please enter a valid column (A-G)")
    columnLetter = input("Player " + turn + ", choose a column (A-G): ")
  columnLetter = columnLetter.upper()
  columnIndex = possibleLetters.index(columnLetter)

  for x in range(rows-1, -1, -1): # Check if we have to change the turn
    if gameBoard[x][columnIndex] == "":
      modifyTurn([x, columnIndex], turn)
      break

  turnCounter += 1