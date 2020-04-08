#Author: Muhammad Umar Khalid
#Major: Computer Science
#Professor: Robert Domanski
#Date:  04//04/2020


# import necessary modules 
import pandas as pd
import matplotlib.pyplot as plt
import sys

#Creating menu so user can make a choice: 
def menu():
	print("\n")
	print("		    	********** Welcome to Project2 Matplotib library **********")
	print()

	choice = input("""
					A: BarGraph of McDonald's items-calories by items-categary or by each-item
					B: Pie chart of Mcdonald's items-calories & TotalFat by each-items
					C: About me	
					D: Quit

					Please enter your choice: """)
	print("\n")
	if choice == "A" or choice == "a":
		bar()
		menu()
	elif choice == "B" or choice == "b":
		pie()
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


#Function for bar graph
def bar():
	
	print("Enter 'cat' to see Calories-graph of calories by item-category:\nEnter 'nct' for number of category:\n")
	#Getting Input
	inp = input("")
	if inp == 'cat' or inp == 'CAT':
		#Reading CSV file from a given path or the file should be in the samefolder 
		data = pd.read_csv("menu.csv")
		#read data in dataframe
		df = pd.DataFrame(data)
		#Title name
		plt.title("Total Calories by item-Category")
		x = df["Category"]
		#X-axis label
		plt.xlabel("Category")
		#Y-axis label
		plt.ylabel("Calories")
		data = df["Calories"]
		plt.bar(x, data, color="grey")
		#Text rotation
		plt.xticks(rotation=45)
		plt.subplots_adjust(bottom = 0.3)
		plt.show()

	elif inp == 'nct' or inp == 'NCT':
		inp = int(input("Enter no of items to see calories-graph by each item: "))
		data = pd.read_csv("menu.csv")
		df = pd.DataFrame(data)

		plt.title("Total Calories by each Item")
		#Getting user input for no of items
		x = df["Item"].head(inp)
		plt.xlabel("Item")
		plt.ylabel("Calories")
		data = df["Calories"].head(inp)
		plt.bar(x, data, color="aqua")
		#Item name at 30 degree angle
		plt.xticks(rotation=45)
		plt.subplots_adjust(bottom = 0.3)
		plt.show()
	else:
		print("Error! Invalid Input.")



#Function for pie chart 
def pie():
	inp = input("Enter 'cal' to see calories and 'tfat' to see total fat for each-item: \n")
	if inp == 'cal' or inp == 'CAL':

		data =  pd.read_csv("menu.csv")
		df = pd.DataFrame(data)
		inp = int(input("Enter How many items-calories graph you wanna see: "))
		mcdonald = df["Item"].head(inp)
		calories_Data = df["Calories"].head(inp)
		#colors for pie chart for each item
		colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#E13F29", "#D69A80", "#D63B59", "#AE5552"]
		plt.pie(calories_Data, labels=mcdonald, colors=colors,
		autopct='%1.1f%%', shadow=True, startangle=90)
		#Title
		plt.title("McDonald's Item Calories Pie chart data by each item\n")
		plt.show()

	elif inp == 'tfat' or inp == 'TFAT':
		data =  pd.read_csv("menu.csv")
		df = pd.DataFrame(data)
		inp = int(input("Enter How many items-Totalfat graph you wanna see: "))
		mcdonald = df["Item"].head(inp)
		fat_Data = df["Total Fat"].head(inp)
		colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b", "#E13F29", "#D69A80", "#D63B59", "#AE5552"]
		plt.pie(fat_Data, labels=mcdonald, colors=colors,
		autopct='%1.1f%%', shadow=True, startangle=90)
		plt.title("McDonald's Items TotalFat Pie chart data by each item\n")
		plt.show()
	else:
		print("Error! Invalid Input.")


#Function for intro about me
def About():	
	print("Hi, My name is Muhammad Umar Khalid major in compter science.\nI love to do coding and fix things. My favourite sport is cricket.\n ")




#main funtion
if __name__ == '__main__':
	print(menu())