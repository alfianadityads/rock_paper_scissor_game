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

root.mainloop()