
import random
A = ['program', 'expert', 'math', 'umar'
     'python', 'compute', 'science', 'subject',
     'yahoo', 'answer']

word = random.choice(A)
turns = 6
currentletter = ''
name = input("What is your name?")
print("Hello, " + name)
while turns > 0:
	failed = 0
	for char in word: 
		if char in currentletter: 
			print(char) 
		else:
			print("_",)
			failed += 1
	if failed == 0:
		print("GREAT JOB! YOU WON")
		print("The word is: ", word)
		break
		
	# Ask the user to guess a letter 
	letter = str(input("Guess a letter: "))
	#set the playerguess letter to currentletter 
	currentletter += letter
	# Check to see if that letter is not in the Answer	
	if letter not in word:
		turns -= 1
		print("BAD GUESS!")
		print("You have", + turns, 'more turns!')
		if turns == 0:
			print("You Lose the game")
