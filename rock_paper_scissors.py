from tkinter import *
from PIL import Image,ImageTk
from random import randint

# main 

root = Tk()
root.title("Paper Rock Scissors Game")
root.configure(background="#918f8e")

# =====================================================================

# Picture assets

# User
rock_user_img = ImageTk.PhotoImage(Image.open("images/rock_user.png"))
paper_user_img = ImageTk.PhotoImage(Image.open("images/paper_user.png"))
scissors_user_img = ImageTk.PhotoImage(Image.open("images/scissors_user.png"))

# Computer
rock_comp_img = ImageTk.PhotoImage(Image.open("images/rock_comp.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open("images/paper_comp.png"))
scissors_comp_img = ImageTk.PhotoImage(Image.open("images/scissors_comp.png"))

# =====================================================================

# Insert picture
user_label = Label(root,image=scissors_user_img, bg="#918f8e")
comp_label = Label(root,image=scissors_comp_img, bg="#918f8e")

user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)

# =====================================================================

# Player Indicators
userIndicator = Label(root, font=50, text="USER", bg="#918f8e", fg="white")
compIndicator = Label(root, font=50, text="COMPUTER", bg="#918f8e", fg="white")

userIndicator.grid(row=0, column=1)
compIndicator.grid(row=0, column=3)

# =====================================================================

# Scores
userScores = Label(root, text=0, font=100, bg="#918f8e", fg="white")
compScores = Label(root, text=0, font=100, bg="#918f8e", fg="white")

userScores.grid(row=1, column=1)
compScores.grid(row=1, column=3)

# =====================================================================

# Messages
msg = Label(root, font=50, bg="#918f8e", fg="white")
msg.grid(row=3, column=2)

# =====================================================================

# Update Choices
choices = ["rock", "paper", "scissor"]
# for user
def updateChoice(x):
# for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_comp_img)
    elif compChoice == "paper":
        comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissors_comp_img)

    if x == "rock":
        user_label.configure(image=rock_user_img)
    elif x == "paper":
        user_label.configure(image=paper_user_img)
    else:
        user_label.configure(image=scissors_user_img)
        
# =====================================================================

# Buttons
rock = Button(root, width=20, height=3, text="ROCK", bg="#daf2f2", fg="black", command= lambda:updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=3, text="PAPER", bg="#f7e702", fg="black", command= lambda:updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=3, text="SCISSOR", bg="#ff8f8f", fg="black", command= lambda:updateChoice("scissor")).grid(row=2, column=3)

# =====================================================================

root.mainloop()