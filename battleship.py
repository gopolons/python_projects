#import a randint function which takes a random number
from random import randint
#create a board
board = []
#create a board as a list
for x in range(0, 5):
  board.append(["O"] * 5)
#create a board as a board with pretty O's
def print_board(board):
  for row in board:
    print(" ").join(row)
#printing the board
print_board(board)
#takes a random variable for the battleship row out of the randint
def random_row(board):
  return randint(0, len(board) - 1)
#takes a random variable for the battleship col out of the randint
def random_col(board):
  return randint(0, len(board[0]) - 1)
#setting variables for the ship variables
ship_row = random_row(board)
ship_col = random_col(board)

# print(ship_row)
# print(ship_col)
#can be used for debugg - show the position of the random variables

#creates a loop for 4 turns (0, 1, 2, 3)
for turn in range(4):
#making sure here that the number input is a integer rather than text
  guess_row = input("Guess Row: ")
  if not guess_row.isalpha():
    guess_row = int(guess_row)
  else:
    print("Invalid answer.")
    guess_row = 228

  guess_col = input("Guess Col: ")
  if not guess_col.isalpha():
    guess_col = int(guess_col)
  else:
    print("Invalid answer.")
    guess_col = 228
#the move itself
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
    print("Game Over")
    break
#condition for being within boundaries
  elif guess_row not in range(5) or \
      guess_col not in range(5):
    print("Oops, that's not even in the ocean.")
#condition for hitting the same thing
  elif board[guess_row][guess_col] == "X":
    print("You guessed that one already.")
  else:
    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"
  print("Turn " + str(turn + 1))
  print_board(board)
#condition for ending the game
if turn == 3:
  print("Game Over")

#in theory the code can be improved via putting spaces in between moves and the following:

# Make multiple battleships: you'll need to be careful 
# because you need to make sure that you don’t place battleships 
# on top of each other on the game board. 
# You'll also want to make sure that you balance the size of the board 
# with the number of ships so the game is still challenging and fun to play.
# Make battleships of different sizes: this is trickier than it sounds. 
# All the parts of the battleship need to be vertically or horizontally touching 
# and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.
# Make your game a two-player game.
# Use functions to allow your game to have more features like rematches, statistics and more!