from tkinter import *
from PIL import Image,ImageTk

# main 

root = Tk()
root.title("Paper Rock Scissors Game")
root.configure(background="#918f8e")


# Picture assets

# User
rock_user_img = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_user_img = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissors_user_img = ImageTk.PhotoImage(Image.open("scissors_user.png"))

# Computer
rock_comp_img = ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_comp_img = ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissors_comp_img = ImageTk.PhotoImage(Image.open("scissors_comp.png"))


# Insert picture
user_label = Label(root,image=scissors_user_img, bg="#918f8e")
comp_label = Label(root,image=scissors_comp_img, bg="#918f8e")

user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)

# Player Indicators
userIndicator = Label(root, font=50, text="USER", bg="#918f8e", fg="white")
compIndicator = Label(root, font=50, text="COMPUTER", bg="#918f8e", fg="white")

userIndicator.grid(row=0, column=1)
compIndicator.grid(row=0, column=3)

# Scores
userScores = Label(root, text=0, font=100, bg="#918f8e", fg="white")
compScores = Label(root, text=0, font=100, bg="#918f8e", fg="white")

userScores.grid(row=1, column=1)
compScores.grid(row=1, column=3)

# Buttons
rock = Button(root, width=20, height=3, text="ROCK", bg="#daf2f2", fg="black").grid(row=2, column=1)
paper = Button(root, width=20, height=3, text="PAPER", bg="#f7e702", fg="black").grid(row=2, column=2)
scissor = Button(root, width=20, height=3, text="SCISSOR", bg="#ff8f8f", fg="black").grid(row=2, column=3)

# Messages
msg = Label(root, font=50, bg="#918f8e", fg="white")
msg.grid(row=3, column=2)

root.mainloop()