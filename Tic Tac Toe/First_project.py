#Author: Muhammad Umar Khalid
#Major: Computer Science
#Professor: Robert Domanski
#Date:  03//02/2020

import sys

#Creating menu so user can make a choice: 
def menu():
	print("\n")
	print("		    	********** Welcome to Tic-Toc-Toe game **********")
	print()

	choice = input("""
					A: Play the Game!
					B: See game rules!
					C: About me	
					D: Quit

					Please enter your choice: """)
	print("\n")
	if choice == "A" or choice == "a":
		playGame()
	elif choice == "B" or choice == "b":
		gameRules()
		menu()
	elif choice == "C" or choice == "c":
		About()
		menu()
	elif choice == "D" or choice == "d":
		print("Babye!")
		sys.exit
	else:
		print("You must only select either A, B, C, or D.")
		print("Please try again")
		menu()



#Function for game rules
def gameRules():
	print("Rules for Tic-Toc-Toe:")
	print("  1. The game is played on a grid that's 3 squares by 3 squares.")
	print("  2. You are X, your friend is O. Players take turns putting their marks in empty squares.")
	print("  3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
	print("  4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n ")



#Function for intro about me
def About():
	print("Hi, My name is Muhammad Umar Khalid major in compter science.\nI love to do coding and fix things. My favourite sport is cricket\n ")



#initializing the board for save the values
board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

#Game is still going or not 
game_going = True

#who the winner
winner = None

#Who the current player
current_player = "X"

#variables to count how many times player won
count = 0
count1 = 0



#Play game function
def playGame():
	global count
	global count1
	board_display()
		#loop util the game stop
	while game_going:
		#will handle a turn for players
		handler(current_player)
		#check if game is finish
		game_over()
		#Will flip to the other player
		flip()

    #print the result won or tie
	if winner == "X" or winner == "O":
 		print("\nGreat job: " + winner + "'s won!")
 		if winner == "X":
 			count += 1
 			print("The player: " + winner + "'s won " + str(count) + " times!")			
 		else:
 			count1 += 1
 			print("The player: " + winner + "'s won " + str(count1) + " times!")
	elif winner == None:
		print("The result is tie.")
	#calling the restart function
	restart()




#This will restart the game with empty values so user can play again
def restart():
	global board
	global game_going
	again = input("Do you want to play again?(y/n)")
	if again == "Y" or again == "y":
		print("Game is resetting!")
		print("\n")
		#clear te board
		board.clear()
		#game is going 
		game_going = True
		#print the new board
		board = ["-", "-", "-",
				 "-", "-", "-",
				 "-", "-", "-"]
		playGame()
	else:
		print("\nBabye! Thanks for playing :)")
		sys.exit




#This will display the board of game
def board_display():
	print("               " + board[0] + " || " + board[1] + " || " + board[2] + "          " + "1 | 2 | 3") 
	print("               " + board[3] + " || " + board[4] + " || " + board[5] + "          " + "4 | 5 | 6")
	print("               " + board[6] + " || " + board[7] + " || " + board[8] + "          " + "7 | 8 | 9")




def handler(player):
	print("\n")
	#get the player position
	print(player + "'s turn.")
	inp = input("Please choose a position from 1-9: ")
	print("You choose position no: " + inp)
	print("\n")

	valid = False
	while not valid:
		#Input validation
		while inp not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			print("Invalid Input!")
			inp = input("Please choose a position from 1-9: ")
		#Get correct index to our board list	
		inp = int(inp) - 1
		#check the spot is it available
		if (board[inp] == "-"):
			valid = True
		else:
			print("Already fill, please select another position. ")
	#put game pieces on board		
	board[inp] = player
	#display the board
	board_display()



#check to see if game is over
def game_over():
	check_winner()
	check_tie()



#function to see if somebody has won the game
def check_winner():
	#set global variables
	global winner
	#check if there is a winner in row, column or diagonal
	row = checkRows()
	column = checkColumns()
	diagonal = checkDiagonals()
  # Get the winner
	if row:
		winner = row
	elif column:
		winner = column
	elif diagonal:
		winner = diagonal
	else:
		winner = None



# Check the rows for a win
def checkRows():
  # Set global variables
  global game_going
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_going = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if there was no winner
  else:
    return None



# Check the columns for a win
def checkColumns():
  # Set global variables
	global game_going
  # Check if any of the columns have all the same value (and is not empty)
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, flag that there is a win
	if column_1 or column_2 or column_3:
		game_going = False
  # Return the winner
	if column_1:
		return board[0] 
	elif column_2:
		return board[1] 
	elif column_3:
		return board[2] 
  # Or return None if there was no winner
	else:
		return None



# Check the diagonals for a win
def checkDiagonals():
  # Set global variables
	global game_going
  # Check if any of the columns have all the same value (and is not empty)
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
	if diagonal_1 or diagonal_2:
		game_going = False
  # Return the winner
	if diagonal_1:
		return board[0] 
	elif diagonal_2:
		return board[2]
  # Or return None if there was no winner
	else:
		return None



# Check if there is a tie
def check_tie():
  # Set global variables
	global game_going
  # If board is full
	if "-" not in board:
		game_going = False
		return True
  # Else there is no tie
	else:
		return False
	



# Flip the current player from X to O, or O to X
def flip():
  # Global variables we need
	global current_player
  # If the current player was X, make it O
	if current_player == "X":
		current_player = "O"
  # Or if the current player was O, make it X
	elif current_player == "O":
		current_player = "X"




#main funtion
if __name__ == '__main__':
	print(menu())