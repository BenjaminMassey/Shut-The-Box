## Simple Shut the Box game written in Python 3
## Copyright 2014 by Benjamin Massey
## Protected under the MIT OpenSource license

## Need to be able to generate random numbers to get the dice rolls
import random

## Create the board values
board = dict()
for i in range(1, 10):
    board[str(i)] = i

## Need to keep tracks of the inputed values
numInputs = dict()

## Variable used to put inputed values into numInputs
dictnum = 0

## Variable to check when game is over
gameOver = False

## Function used to show the player the current board
def show_board():
    print("\nHere are the remaining pieces of the board:")
    for i in range(1, 9):
        print(board[str(i)], end = " ")
    print(board["9"], "\n")

## Roll the two dice, add them up, tell the player their total and give us the total to use later
def dice_numbers():
    global total
    total = 0
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    dice = die1 + die2
    print("This is the number you need to add up to:", dice)
    return dice

## Get the numbers that the player wants to use
def player_numbers():
    global dice
    global total
    global dictnum
    number = input()
    ## If can't be done, they manually end the game by inputing 'impossible'
    if number == "impossible":
        return False
    ## Make sure they don't use the same number multiple times
    if board[number] == "X":
        print("That number has already been used, try again.")
    else:
        total = total + int(number)
        ## Make sure to undo total changes and restart the function if they make the total too big
        if total > dice:
            print("That would put you over your number of", dice)
            total = total - int(number)
            player_numbers()
        ## When given number is met, finish up striking board and put input into numInputs
        elif total == dice:
            board[number] = "X"
            dictnum += 1
            numInputs[dictnum] = int(number)
        ## Player is still adding up to make the number, strike input, add into numInputs and restart function
        else:
            board[number] = "X"
            dictnum += 1
            numInputs[dictnum] = int(number)
            player_numbers()

## Introductory Paragraph
print("This is a simple shut the box game.")
print("You will have a board of numbers 1 through 9.")
print("Two dice will be rolled and added up every turn.")
print("You will need to add up the numbers available on the board to equal the given random number.")
print("The numbers you choose will then be taken off the board, and the next turn will begin.")
print("The game will end either when the board is completely gone, or when you can't make the given number.")
print("If you can't make the given number, type 'impossible' and the game will end.")
print("Your score will be the sum of the remaining numbers, lower scores being better.")
print("Good luck!")

## Main game loop; only run while game isn't over
while gameOver == False:
    show_board()
    dice = dice_numbers()
    ## This is when the player types in 'impossible', the usual ending to the game
    if player_numbers() == False:
        endScore = 45 - sum(numInputs.values())
        print("\nYou ended the game with a score of", endScore)
        gameOver = True
    ## This next section checks to see if all numbers are striked; special message for lucky winners
    numXs = 0
    for i in range(1,10): 
        if board[str(i)] == "X":
            numXs += 1
    if numXs == 9:
        gameOver = True
        print("\nYou ended the game with the highest score, 0! Congratulations!")
