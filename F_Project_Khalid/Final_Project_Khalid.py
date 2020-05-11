#Import necessary modules
import os
import sys


#menu function so user can make a choice
def menu():
    print("\n")
    print("             ********** Welcome to the Personal Budget program **********")
    print()

    choice = input("""
                    A: Start the Program!
                    B: What is meant by deficit and surplus!
                    C: Purpose of the program!
                    D: About author! 
                    E: Quit!

                    Please enter your choice: """)
    print("\n")
    if choice == "A" or choice == "a":
        Application()
    elif choice == "B" or choice == "b":
        meaning()
        menu()
    elif choice == "C" or choice == "c":
        purpose()
        menu()
    elif choice == "D" or choice == "d":
        Aboutme()
        menu()
    elif choice == "E" or choice == "e":
        print("Exiting the program.")
        print("Babye!!!")
        sys.exit
    else:
        print("You must only select either A, B, C, D, or E.")
        print("Please try again")
        menu()




#Function for understanding surplus and deficit
def meaning():
    print('Deficit: A deficit is an amount by which a resource, especially money, falls short of what is required. \nA deficit occurs when expenses exceed revenues, imports exceed exports, or liabilities exceed assets. \nA deficit is synonymous with shortfall or loss and is the opposite of a surplus.')
    print('\nSurplus: A surplus describes the amount of an asset or resource that exceeds the portion that is actively utilized. \nA surplus can refer to a host of different items, including income, profits, capital, and goods. \nIn the context of inventories, a surplus describes products that remain sitting on store shelves, unpurchased. \nIn budgetary contexts, a surplus occurs when income earned exceeds expenses paid. A budget surplus can \nalso occur within governments when there is leftover tax revenue after all governmental programs are fully financed.')




#Function for intro about me
def Aboutme():
    print("Hi, My name is Muhammad Umar Khalid majoring in compter science.\nI love to do coding and fix things. My favourite sport is cricket\n ")




#Purpose functuon of the program
def purpose():
    print('The purpose of this program to take income and expenses from the user \nand tells the user whether they have a surplus, a deficit, or if they are breaking even. ')




#Declaring class
class Application:
    #init to assign values to object properties or other operations
    #declaring and initializing 
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.expense_l = []
        self.expense_name = []
        self.income_name = []
        self.income_l = []
        self.prompt_income()



    #income ask from user function
    def income_ask(self):
        add_income = input('\nLets Add your Income? [Enter y for YES, or n for No]: ')
        return add_income




    #income sum function
    def income_sum(self):
        self.income = sum(self.income_l)




    #expense ask from user function
    def expense_ask(self):
        add_expense = input('\nNow Lets Add your Expenses? [Enter y for YES, or n for NO]: ')
        return add_expense




    #expense sum function
    def expense_sum(self):
        self.expenses = sum(self.expense_l)





    #check income function
    def income_check(self):
        if not self.income_l:
            print('Please enter atleast one source of Income: ')
            self.prompt_income()




    #check expense function
    def expense_check(self):
        if not self.expense_l:
            print('Please enter atleast one Expense: ')
            self.prompt_expense()





    #prompt income function to get income inputs from the user
    def prompt_income(self):
        while True:
            result = self.income_ask()
            if result == 'y':
                try:
                    income_input = int(input('Enter source of Income. [Numbers Only]: '))
                    #adding in income_l
                    self.income_l.append(income_input)
                    income_name = input('Enter Income name. [Name Only]: ')
                    #adding in income_name
                    self.income_name.append(income_name)
                    inp = input('\nDo you have another source of Income. [Enter y for YES, or n for NO]: ')
                    if inp == 'y':
                        self.prompt_income()
                    else:
                        self.income_check()
                        break

                except ValueError:
                    print("Input is not valid enter valid input!")
                    income_input = int(input('Enter source of Income. [Numbers Only]: '))
                    #adding in income_l
                    self.income_l.append(income_input)
                    income_name = input('Enter Income name. [Name Only]: ')
                    self.income_name.append(income_name)
                    inp = input('\nDo you have another source of Income. [Enter y for YES, or n for NO]: ')
                    if inp == 'y':
                        self.prompt_income()
                    else:
                        self.income_check()
                        break
            else:
                #checkif user didnot put any income
                self.income_check()
                break
        #updating income by adding all together which user enter        
        self.income_sum()
        incomedict = dict(zip(self.income_name, self.income_l))
        for detail in incomedict:
            print(detail + ': ', '$' + str(incomedict[detail]))
        print('Total user Income: ', '$' + str(self.income))
        self.prompt_expense()





    #prompt expense function to get expenses inputs from the user
    def prompt_expense(self):
        while True:
            result = self.expense_ask()
            if result == 'y':
                try:
                    expense_input = int(input('Enter Expense amount. [Numbers Only]: '))
                    #adding in expense_l
                    self.expense_l.append(expense_input)
                    expense_name = input('Enter Expense name. [Name Only]: ')
                    #adding in expense_name 
                    self.expense_name.append(expense_name)
                    inp = input('\nDo you have another Expenses. [Enter y for YES, or n for NO]: ')
                    if inp == 'y':
                        self.prompt_expense()
                    else:
                        self.expense_check()
                        break

                except ValueError:
                    print("Input is not valid! Try again...")
                    expense_input = int(input('Enter Expense amount. [Numbers Only]: '))
                    #adding in expense_l
                    self.expense_l.append(expense_input)
                    expense_name = input('Enter Expense name. [Name Only]: ')   
                    #adding in expense_name 
                    self.expense_name.append(expense_name)
                    inp = input('\nDo you have another Expenses. [Enter y for YES, or n for NO]: ')
                    if inp == 'y':
                        self.prompt_expense()
                    else:
                        self.expense_check()
                        break
                        
            else:
                #check if user didnot put any expense
                self.expense_check()
                break
        #updating income by adding all together which user enter
        self.expense_sum()
        expensedict = dict(zip(self.expense_name, self.expense_l))
        for detail in expensedict:
            print(detail + ': ', '$' + str(expensedict[detail]))
        print('Total user Expenses: ', '$' + str(self.expenses))
        self.uservalue()





    #check user value and compare it after substracting income minus expenses 
    def uservalue(self):
        result = self.income - self.expenses
        if result < 0:
            print('\nYour total Income is: ' +  '$' + str(self.income))
            print('Your total Expenses are: ' + '$' + str(self.expenses))
            print('Result = Caution! Budget exceeded, You are in negative, you have a deficit of: ${amount}'.format(amount=result))
            
        if result == 0:
            print('\nYour total Income is: ' +  '$' + str(self.income))
            print('Your total Expenses are: ' + '$' + str(self.expenses))
            print('Result = You have broken even, you are spending exactly as much as you make.')

        if result > 0:
            print('\nYour total Income is: ' +  '$' + str(self.income))
            print('Your total Expenses are: ' + '$' + str(self.expenses))
            print('Result = Congratulations! You are in positive, you have a surplus of: ${amount}'.format(amount=result))

        #asking user if he wants to run another analysis
        another = input('Would you like to run another analysis? [Enter y for YES, or n for NO]: ')
        if another == 'y':
            self.reset_program()
        else:
            self.close_program()




    #reset function and emptying list
    def reset_program(self):
        self.income = 0
        self.expenses = 0
        del self.expense_l[0:]
        del self.expense_name[0:]
        del self.income_name[0:]
        del self.income_l[0:]
        self.prompt_income()




    #exiting the program function using sys.exit
    def close_program(self):
        print('\nExiting Program.')
        print('Babye!!!')
        sys.exit(0)




#Main function
if __name__ == '__main__':
    name = input("\nEnter your name: " )
    print("Welcome " + name + "!")
    #calling menu function
    menu()
    