# Hangman game!
# Assume the answer is "hangman"
A = ['h','a','n','g','m','a','n']
L = ['_','_','_','_','_','_','_']
play = True
turns = 6
while play == True and turns > 0:
# Ask the user to guess a letter
  letter = str(input("Guess a letter: "))
#if letter does not match, give an error bad guess
  if letter not in A:
  	turns -= 1
  	print("Bad guess!")
  	print("You have", + turns, 'more turns!')
  	if turns == 0:
  		print("You lose the game!")

# Check to see if that letter is in the Answer
  i = 0
  for currentletter in A:
# If the letter the user guessed is found in the answer,
# set the underscore in the user's answer to that letter
    if letter == currentletter:
      L[i] = letter
    i = i + 1
# Display what the player has thus far (L) with a space
# separating each letter
  print(' '.join(str(n) for n in L))

# Test to see if the word has been successfully completed,
# and if so, end the loop
  if A == L:
    play = False
print("GREAT JOB!")