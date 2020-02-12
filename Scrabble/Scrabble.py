def letter_Score(letter): 

	if letter in "aeilonsrutAEILONSRUT":

		return 1

	elif letter in "dgDG":
		
		return 2

	elif letter in "bcmpBCMP":

		return 3

	elif letter in "fhvwyFHVWY":

		return 4

	elif letter in "kK":

		return 5

	elif letter in "jxJX":

		return 8
	
	elif letter in "qzQZ":

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
