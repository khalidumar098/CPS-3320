#importing random
import random
A = ['program', 'expert', 'math', 'umar'
     'python', 'compute', 'science', 'subject',
     'yahoo', 'answer']

word = random.choice(A)
turns = 6
currentletter = ''
#welcoming the user by asking his/her name
name = input("What is your name?")
print("Hello, " + name)
#checking if turns more than zero
while turns > 0:
	#counter
	failed = 0
	for char in word: 
		#see if character exist
		if char in currentletter: 
			print(char)
		#if not print _ and increased failed counter
		else:
			print("_",)
			failed += 1
	if failed == 0:
		print("GREAT JOB! YOU WON")
		print("The word is: ", word)
		break
		
	# Ask the user to guess a letter 
	letter = str(input("Guess a letter: "))
	#Set the playerguess letter to currentletter 
	currentletter += letter
	# Check to see if that letter is not in the word	
	if letter not in word:
		turns -= 1
		print("BAD GUESS!")
		#how many turns are left
		print("You have", + turns, 'more turns!')
		#if turns equal to zero then print
		if turns == 0:
			print("You Lose the game")
