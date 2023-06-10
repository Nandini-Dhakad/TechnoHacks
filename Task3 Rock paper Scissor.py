"Nandini Dhakad"
"Technohacks"
"Task 3: Rock,Paper,Scissor Game"

from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root=Tk()
root.title("ROCK PAPER SCISSOR")
root.configure(background="lightblue")

#pictures
rock_img=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor.jpg"))

rock_img_comp=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissor.jpg"))

#picture insertion in window
user_label=Label(root,image=scissor_img,bg="lightblue")
comp_label=Label(root,image=scissor_img_comp,bg="lightblue")
user_label.grid(row=1, column=4)
comp_label.grid(row=1, column=0)

#score
playerscore=Label(root,text=0,font=100, bg="lightblue",fg="black")
computerscore=Label(root,text=0,font=100, bg="lightblue",fg="black")
computerscore.grid(row=1, column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="USER",bg="lightblue",fg="black").grid(row=0,column=3)
comp_indicator=Label(root,font=50,text="COMPUTER",bg="lightblue",fg="black").grid(row=0,column=1)

#messages
msg=Label(root,font=50,bg="lightblue",fg="black")
msg.grid(row=3,column=2)

#update message
def updatemessage(x):
    msg['text'] = x

#update user score
def updateuserscore():
    score=int(playerscore["text"])
    score+=1
    playerscore["text"]=str(score)

#update computer score
def updatecomputerscore():
    score=int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)

#who's the winner?
def checkwin(player,computer):
    if player==computer:
        updatemessage("It's a tie")
    elif player=="rock":
        if computer=="paper":
            updatemessage("You LOOSE")
            updatecomputerscore()
        else:
            updatemessage("You WIN")
            updateuserscore()
    elif player=="paper":
        if computer=="scissor":
            updatemessage("You LOOSE")
            updatecomputerscore()
        else:
            updatemessage("You WIN")
            updateuserscore()
    elif player=="scissor":
        if computer=="rock":
            updatemessage("You LOOSE")
            updatecomputerscore()
        else:
            updatemessage("You WIN")
            updateuserscore()
    else:
        pass


#choice
choice=["rock","paper","scissor"]
def updatechoice(x):
     
     #computer
    compchoice= choice[randint(0,2)]
    if compchoice=="rock":
        comp_label.configure(image=rock_img)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img)
    elif compchoice=="scissor":
        comp_label.configure(image=scissor_img)

    #user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkwin(x,compchoice)

#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="grey",fg="white",command=lambda: updatechoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="grey",fg="white",command=lambda: updatechoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="grey",fg="white",command=lambda: updatechoice("scissor")).grid(row=2,column=3)


root.mainloop()