from tkinter import * 
from PIL import Image,ImageTk
from random import randint

main_root = Tk()
main_root.title("Snake,Water & Gun Game")
main_root.configure(bg="white")


user_indicator = Label(main_root,font=100,text="Snake, Water & Gun Game ",fg="darkblue").grid(row=0,column=2)
user_indicator = Label(main_root,font=50,text="USER").grid(row=0,column=0)
comp_indicator = Label(main_root,font=50,text="COMPUTER").grid(row=0,column=4)
msg = Label(main_root,font=50,fg="black")
msg.grid(row=1,column=2)


water_img = ImageTk.PhotoImage(Image.open("water.png"))
snake_img = ImageTk.PhotoImage(Image.open("snake.png"))
gun_img = ImageTk.PhotoImage(Image.open("gun.png"))
water_comp_img = ImageTk.PhotoImage(Image.open("water.png"))
snake_comp_img = ImageTk.PhotoImage(Image.open("water.png"))
gun_comp_img = ImageTk.PhotoImage(Image.open("water.png"))

user_label = Label(main_root,image=snake_img,bg="white")
comp_label = Label(main_root,image=snake_img,bg="white")
user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)


player_score=Label(main_root,text=0,font=('arial',40,"bold",),fg="red")
computer_score=Label(main_root,text=0,font=('arial',40,"bold"),fg="red")
computer_score.grid(row=1,column=3)
player_score.grid(row=1,column=1)


a=Label(main_root,font=('arial',15,"bold"),text="player",bg="orange",fg="blue")
computer_indicator=Label(main_root,font=("arial",15,"bold"),text="computer",bg="orange",fg="blue")
computer_indicator.grid(row=0,column=3)
a.grid(row=0,column=1)





compChoices = ["water","snake","gun"]
def choice(x):
              compstack = compChoices[randint(0,2)]
              if compstack == "water":
                            comp_label.configure(image = water_img)
              elif compstack == "snake":
                            comp_label.configure(image = snake_img)
              elif compstack == "gun":
                            comp_label.configure(image = gun_img)


              if(x == "water"):
                              user_label.configure(image = water_img)
              elif(x == "snake"):
                              user_label.configure(image = snake_img)
              elif(x == "gun"):
                              user_label.configure(image = gun_img)

              check_win(x,compstack)

snake = Button(main_root,width=20,height=2,text="SNAKE",bg="yellow",fg="black",command=lambda:choice("snake")).grid(row=2,column=2)
water = Button(main_root,width=20,height=2,text="WATER",bg="blue",fg="black",command=lambda:choice("water")).grid(row=2,column=1)
gun = Button(main_root,width=20,height=2,text="GUN",bg="green",fg="black",command=lambda:choice("gun")).grid(row=2,column=3)
exit ==Button(main_root,width=20,height=2,text="EXIT ",bg="darkred",fg="black",command=exit).grid(row=3,column=4)



def updateM(x):
              msg['text'] = x

def player_update():
    final=int(player_score['text'])
    final+=1
    player_score["text"]=str(final)

def computer_update():
    final=int(computer_score['text'])
    final+=1
    computer_score["text"]=str(final)
          

def check_win(player,computer):
                              if player == computer:
                                  updateM("It's Tie !")
        
                              elif player == "water":
                                  if computer == "snake":
                                     
                                      updateM("Oops !! You Lose !")
                                      computer_update()
                                      
                                                        
                                  else:
                                      updateM(" Congratulation !! You Won !")
                                      player_update()
                                      
                                      
                                      
                                      
                                      
                              elif player == "gun":
                                  if computer == "water":
                                      updateM("Oops !! You Lose !")
                                      computer_update()
                                      
                                       
                                  else:
                                      updateM("Congratulation !! You Won !")
                                      player_update()
                                      
                                      
                              elif player == "snake":
                                  if computer == "gun":
                                      updateM("Oops !! You Lose !")
                                      computer_update()
                                      
                                      
                                  else:
                                      updateM("Congratulation !! You Won !")
                                      player_update()
                                      
                                       


main_root.mainloop()

