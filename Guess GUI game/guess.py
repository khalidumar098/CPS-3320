#Author: Muhammad Umar Khalid
#Major: Computer Science
#Professor: Robert Domanski
#Date:  04//05/2020


#Tkinter
import tkinter as tk
import random

#Generating random no from 1 to 10 
guessno = random.randint(1, 10)


#Check function
def check():
#get the value from text gets
    guess = int(txt_guess.get())

    #Play to check guess is equal, greater or lower
    if guess < guessno:
        msg = "Your guess is too low"
    elif guess > guessno:
        msg = "Your guess is too high"
    elif guess == guessno:
        msg = "Correct, Good job!"
    else:
        msg = "Error! Something went wrong"

        #show the results
    lbl_result["text"] = msg

        #clear text after input
    txt_guess.delete(0, 10)


#Reset function
def reset():
    #Declaration of global number 
    global guessno
    #random number generator
    guessno = random.randint(0, 10)
    lbl_result["text"] = "Game reset, Lets Play again!"



#create root window
root = tk.Tk()

#rootwindow background colortxt_clear
root.configure(bg = "#6d7a69")

#title
root.title("Guess No Game!")

#window size
root.geometry("430x100")




#creating widgets
lbl_title = tk.Label(root,text="Welcome to the Guessing Game! I am thinking of a number between 1 and 10.", bg="#696969")

lbl_title.pack()


#Showing results label
lbl_result = tk.Label(root, text="Good luck!", bg="lightgrey")

lbl_result.pack()


#Check Button 
btn_check = tk.Button(root, text="Check", foreground = "green", command = check)
btn_check.pack(side = "left")


#Reset Button
btn_reset = tk.Button(root, text="Reset", foreground = "red", command = reset)
btn_reset.pack(side = "right")


#Input entry box
txt_guess = tk.Entry(root, width = 6) 
txt_guess.pack()


#Main event
root.mainloop()
root.destroy()