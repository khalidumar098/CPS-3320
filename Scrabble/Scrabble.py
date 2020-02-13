def letter_Score(letter): 
	letter = letter.lower()
	if letter in "aeilonsrut":

		return 1

	elif letter in "dg":
		
		return 2

	elif letter in "bcmp":

		return 3

	elif letter in "fhvwy":

		return 4

	elif letter in "k":

		return 5

	elif letter in "jx":

		return 8
	
	elif letter in "qz":

		return 10

	else:

		return 0


def word_Score(word):
	total = 0
	for letter in word:
		total += letter_Score(letter)
	return total



name = input("What is your name?")
print("Hello, " + name)
a = str(input("Enter a word: "))
print("You enter: ", a)
print("Your total score is: ", word_Score(a))
