from tkinter import *


y=""
x=2
player_1=[]
player_2=[]

def define_sign(number):

      global x,y
      global player_1,player_2

      if number==1:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b1.config(text=y)
            x=x+1


      if number==2:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b2.config(text=y)
            x=x+1


      if number==3:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b3.config(text=y)
            x=x+1


      if number==4:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b4.config(text=y)
            x=x+1


      if number==5:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b5.config(text=y)
            x=x+1


      if number==6:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b6.config(text=y)
            x=x+1


      if number==7:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b7.config(text=y)
            x=x+1


      if number==8:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b8.config(text=y)
            x=x+1


      if number==9:
            if x%2==0:
                  y='x'
                  player_1.append(number)
                  print(player_1)

            elif x%2!=0:
                  y='0'
                  player_2.append(number)
                  print(player_2)

            b9.config(text=y)
            x=x+1


            


root=Tk()


l1=Label(root,text="player 1 : x ",font="times 15")
l1.grid(row=0,column=1)

l2=Label(root,text="player 2 : O ",font="times 15")
l2.grid(row=0,column=2)

b1=Button(root,width=20,height=10,command=lambda: define_sign(1))
b1.grid(row=1,column=1)

b2=Button(root,width=20,height=10,command=lambda: define_sign(2))
b2.grid(row=1,column=2)

b3=Button(root,width=20,height=10,command=lambda: define_sign(3))
b3.grid(row=1,column=3)

b4=Button(root,width=20,height=10,command=lambda: define_sign(4))
b4.grid(row=4,column=1)

b5=Button(root,width=20,height=10,command=lambda: define_sign(5))
b5.grid(row=4,column=2)

b6=Button(root,width=20,height=10,command=lambda: define_sign(6))
b6.grid(row=4,column=3)

b7=Button(root,width=20,height=10,command=lambda: define_sign(7))
b7.grid(row=8,column=1)

b8=Button(root,width=20,height=10,command=lambda: define_sign(8))
b8.grid(row=8,column=2)

b9=Button(root,width=20,height=10,command=lambda: define_sign(9))
b9.grid(row=8,column=3)



root.mainloop()










