#Author: Muhammad Umar Khalid
#Major: Computer Science
#Professor: Robert Domanski
#Date:  04/02/2020

#import necessary modules
import os, sys
from PIL import Image, ImageFilter
#Creating menu so user can make a choice: 
def menu():
	print("\n")
	print("		    	********** Welcome to Project2 Pillow Library **********")
	print()

	choice = input("""
					A: See the Image
					B: Image Detail
					C: Resized Image
					D: Resized Image using thumbnail to keep the aspect ratio	
					E: Crop the Image
					F: Rotate the Image
					G: Color Transform to greyScale and cmyk 
					H: Flip the Image (Mirror version)
					I: Change Image type/format
					J: Blurr the Image
					K: Paste an image
					L: About me
					M: Quit

					Please enter your choice: """)
	print("\n")
	if choice == "A" or choice == "a":
		imageSee()
		menu()
	elif choice == "B" or choice == "b":
		imgDetail()
		menu()
	elif choice == "C" or choice == "c":
		resize()
		menu()
	elif choice == "D" or choice == "d":
		resizeTh()
		menu()
	elif choice == "E" or choice == "e":
		crop()
		menu()
	elif choice == "F" or choice == "f":
		rotate()
		menu()
	elif choice == "G" or choice == "g":
		transform()
		menu()
	elif choice == "H" or choice == "h":
		flip()
		menu()
	elif choice == "I" or choice == "i":
		type()
		menu()
	elif choice == "J" or choice == "j":
		blur()
		menu()
	elif choice == "K" or choice == "k":
		copy()
		menu()
	elif choice == "L" or choice == "l":
		About()
		menu()
	elif choice == "M" or choice == "m":
		print("Babye!")
		sys.exit
	else:
		print("You must only select either A, B, C, D, E, F, G, H, I, J, K, L or I!")
		print("Please try again!")
		menu()




#Function to see the image 
def imageSee():
	try:
		#Making sure that path is correct and image is in the same folder, directory 
		img = Image.open("img1.jpg")
		print("Opening!")
		img.show()
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")





#Function for paste an Image 
def copy():
	try:
		img = Image.open("img1.jpg")
		logo = Image.open("logo.png")
		image_copy = img.copy()
		#validate input
		try:
			inp = int(input("Enter x coordinate in upper left: \n"))
			inp1 = int(input("Enter y coordinate in upper left: \n"))
			image_copy.paste(logo, (inp, inp1))
			image_copy.save("pasted_image.jpg")
			print("Image created successfully!")
			image_copy.show()
		except ValueError:
			print("Input is not valid, enter Int only!")
			inp = int(input("Enter x coordinate in upper left: \n"))
			#paste function 
			inp1 = int(input("Enter y coordinate in upper left: \n"))
			image_copy.paste(logo, (inp, inp1))
			image_copy.save("pasted_image.jpg")
			print("Image created successfully!")
			image_copy.show()
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")






#Function to see the image detail
def imgDetail():
	try:
		img = Image.open("img1.jpg")
		print("The Image format is: ", img.format)
		print("The Image size in pixel (width, height) is: ", img.size)
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")
	





#Function to change the image format
def type():
	try:
		img = Image.open("img1.jpg")
	#Getting input
		inp = input("Enter dib, eps, gif, jpeg, pcx, png, sgi Image file formats: ")
		#validate input
		while inp not in ["bmf", "dib", "eps", "gif", "jpeg", "pcx", "png", "sgi"]:
			print("Invalid Input!")
			inp = input("Please enter supported image-format: ")
		img.save("new." + inp)
		print("New Image format created successfully!, check your folder. ")
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")



#Function for blurriness
def blur():
	try:
	# creating a image object  
		img = Image.open("img1.jpg")
		#validate int input
		try:  	
			inp = int(input("Enter the radius for blurriness of the image: \n"))
		# applying the Gaussian Blur filter 
			img_blur = img.filter(ImageFilter.GaussianBlur(radius = inp)) 
			img_blur.save("new_blur.jpg")
			print("Image created successfully!")  
			img_blur.show()
		except ValueError:
			print("Input is not valid, enter int only!")
			inp = int(input("Enter the radius for blurriness of the image: \n"))
		# applying the Gaussian Blur filter 
			img_blur = img.filter(ImageFilter.GaussianBlur(radius = inp)) 
			img_blur.save("new_blur.jpg")  
			print("Image created successfully!")
			img_blur.show()
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")






#Function to resize the image 
def resize():
	try:
		img = Image.open("img1.jpg")
		#validate input
		try:
			#Getting Input
			inp = int(input("Enter width: \n"))
			inp1 = int(input("Enter height: \n"))	
			new_image = img.resize((inp, inp1))
			new_image.save("newimg_size.jpg")
			print("The original image: ", img.size) # Output: (1920, 1080)
			print("The new image: ", new_image.size) # Output: (inp, inp1)
			new_image.show()
		except ValueError:
			print("Input is not valid, enter int only!")
			inp = int(input("Enter width: \n"))
			inp1 = int(input("Enter height: \n"))	
			new_image = img.resize((inp, inp1))
			new_image.save("newimg_size.jpg")
			print("The original image: ", img.size) # Output: (1920, 1080)
			print("The new image: ", new_image.size) # Output: (inp, inp1)
			new_image.show()
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")






#Function to resize the image and kept original aspect ratio of the image
def resizeTh():
	try:
		img = Image.open("img1.jpg")
	#validate input
		try:
			#Getting Input
			inp = int(input("Enter width: \n"))
			inp1 = int(input("Enter height: \n"))
			img.thumbnail((inp, inp1))
			img.save("img_thumbnail.jpg")
			print("The new image which kept the aspect ratio of the original image: ", img.size) # Output: (inp, inp1)
			img.show()
		except ValueError:
			print("Input is not valid, enter int only!")
			inp = int(input("Enter width: \n"))
			inp1 = int(input("Enter height: \n"))
			img.thumbnail((inp, inp1))
			img.save("img_thumbnail.jpg")
			print("The new image which kept the aspect ratio of the original image: ", img.size) # Output: (inp, inp1)
			img.show()
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")





#Function for cropping the image
def crop():
	try:
		img = Image.open("img1.jpg")
		print("Image original size is: ", img.size)
		#validate input
		try:
	#Getting Input
			left = int(input("Enter left dimension: \n")) 
			upper = int(input("Enter upper dimension: \n")) 
			right = int(input("Enter right dimension: \n")) 
			lower = int(input("Enter lower dimension: \n")) 
	#(left, upper, right, lower).
			box = (left, upper, right, lower)
			cropped_img = img.crop(box)
			cropped_img.save('cropped_img.jpg')
			print("Image cropped successfully as a new file: ", cropped_img.size)
			cropped_img.show()
		except ValueError:
			print("Input is not valid, enter int only!")
			#Getting Input
			left = int(input("Enter left dimension: \n")) 
			upper = int(input("Enter upper dimension: \n")) 
			right = int(input("Enter right dimension: \n")) 
			lower = int(input("Enter lower dimension: \n")) 
	#(left, upper, right, lower).
			box = (left, upper, right, lower)
			cropped_img = img.crop(box)
			cropped_img.save('cropped_img.jpg')
			print("Image cropped successfully as a new file: ", cropped_img.size)
			cropped_img.show()
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")





#Function to rotate the image in different angles
def rotate():
	try:
		img = Image.open("img1.jpg")
		#validate input
		try:
	#Getting input from user
			inp = int(input("Please enter an angle 45, 90, 180, 270, 360 or your own choice no for an image rotation: "))
			img_angle = img.rotate(inp)
			img_angle.save("img_rot_angle.jpg")
			print("Image rotated successfully!")
			img_angle.show()
		except ValueError:
			print("Invalid input,enter only int!")
			inp = int(input("Please enter an angle 45, 90, 180, 270, 360 or your own choice no for an image rotation: "))
			img_angle = img.rotate(inp)
			img_angle.save("img_rot_angle.jpg")
			print("Image rotated successfully!")
			img_angle.show()

	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")


#Function to transform the image in greyscale and CMYK
def transform():
	try:
		img = Image.open("img1.jpg")
		inp = input("Enter L (greyscale), CMYK: ")
		if inp == 'L' or inp == 'l': 
			greyscale_img = img.convert('L')
			greyscale_img.save("greyscale_img.jpg")
			print("Image created successfully!, check your folder")
			greyscale_img.show()
		if inp == 'CMYK' or inp == 'cmyk': 
			cmyk_img = img.convert('CMYK')
			cmyk_img.save("cmyk_img.jpg")
			print("Image created successfully!, check you folder.")
		else:
			print("Error, Invalid Choice!")
		
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")





#Function for intro about me
def About():	
	print("Hi, My name is Muhammad Umar Khalid major in compter science.\nI love to do coding and fix things. My favourite sport is cricket.\n ")





#Function to flip the image in to the mirror version
def flip():
	try:
		img = Image.open("img1.jpg")
		img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
		img_flip.save('img_flip.jpg')
		print("Image created successfully!")
		img_flip.show()
	except IOError:
		print("Unable to load image!\nPlease make sure image directory path is correct.")


#main funtion
if __name__ == '__main__':
	print(menu())