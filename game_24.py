# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:24:55 2018

@author: Paul
"""

try:
    from tkinter import *
except ImportError:
    pass

try:
    from Tkinter import *
except ImportError:
    pass

from random import randint
import res_24 as res

class Mbut(Button):
    def __init__(self,master,frame,text,command):
        Button.__init__(self,frame,text=text,command=command,bg='gray30',fg='white',activeforeground='white',activebackground='gray30')
        self.master=master

    def clic(self,event):
        if self.state==ACTIVE:
            self.command

class Fen(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('700x700')
        self.bind('<F5>',self.reset)
        self.bind('<F6>',self.cancel)
        self.bind('<Escape>',self.leave)
        self.input=[]
        self.numbers=[0,0,0,0]
        self.imax=4
        self.nop=0

        #Frame 0
        self.frame0= Frame(self)
        Mbut(self,self.frame0,text='New (F5)',command= lambda: self.reset(None)).place(x=400,y=10,width=80,height=40)
        Mbut(self,self.frame0,text='Cancel (F6)',command=lambda: self.cancel(None)).place(x=500,y=10,width=100,height=40)
        Mbut(self,self.frame0,text='Cheat',command=lambda: self.cheat(None)).place(x=620,y=10,width=80,height=40)
        self.frame0.place(x=0,y=0,width=700,height=100)

        #Frame 1
        self.frame1= Frame(self)
        self.buttons=[]
        self.can = Canvas(self.frame1,height=400,width=600)
        self.frame1.place(x=0,y=100,width=600,height=400)

        #Input Label
        self.ilab = Label(self,text=' ')
        self.ilab.place(x=100,y=510,width=500,height=30)

        #Frame 2
        self.frame2= Frame(self)
        self.obuttons=[Mbut(self,self.frame2,text='+',command= lambda: self.process('+','o',0)),Mbut(self,self.frame2,text='-',command= lambda: self.process('-','o',0)),Mbut(self,self.frame2,text='x',command= lambda: self.process('x','o',0)),Mbut(self,self.frame2,text='/',command= lambda: self.process('/','o',0))]
        self.obuttons[0].place(x=50,y=0,width=100,height=100)
        self.bind('<w>',lambda event : self.process('+','o',0))
        self.obuttons[1].place(x=200,y=0,width=100,height=100)
        self.bind('<x>',lambda event : self.process('-','o',0))
        self.obuttons[2].place(x=350,y=0,width=100,height=100)
        self.bind('<c>',lambda event : self.process('x','o',0))
        self.obuttons[3].place(x=500,y=0,width=100,height=100)
        self.bind('<v>',lambda event : self.process('/','o',0))
        self.frame2.place(x=0,y=550,width=600,height=100)

    def reset(self,event):
        nok=True
        while nok:
            n1,n2,n3,n4=randint(1,13),randint(1,13),randint(1,13),randint(1,13)
            if res.test([n1,n2,n3,n4]):
                self.numbers=[n1,n2,n3,n4]
                nok=False
                self.can.delete(ALL)
        self.cancel(None)


    def cancel(self,event):
        for i in range(4,self.imax):
            self.buttons[i].destroy()
        self.buttons=[ Mbut(self,self.frame1,text=str(self.numbers[0]),command= lambda: self.process(self.numbers[0],'n',0)),Mbut(self,self.frame1,text=str(self.numbers[1]),command= lambda: self.process(self.numbers[1],'n',1)),Mbut(self,self.frame1,text=str(self.numbers[2]),command= lambda: self.process(self.numbers[2],'n',2)),Mbut(self,self.frame1,text=str(self.numbers[3]),command= lambda: self.process(self.numbers[3],'n',3))]
        self.bind('<a>',lambda event : self.process(self.numbers[0],'n',0))
        self.bind('<z>',lambda event : self.process(self.numbers[1],'n',1))
        self.bind('<e>',lambda event : self.process(self.numbers[2],'n',2))
        self.bind('<r>',lambda event : self.process(self.numbers[3],'n',3))
        for i in range(4):
            self.buttons[i].place(x=50+150*i,y=0,width=100,height=100)
        self.bind('<q>',lambda event : None)
        self.bind('<s>',lambda event : None)
        self.bind('<d>',lambda event : None)
        self.ilab.config(text=' ')
        self.numbers=self.numbers[:4]
        self.imax,self.nop,self.input=4,0,[]

    def process(self,y,t,i):
        if len(self.input)==0 and t=='n':
            self.input.append([y,i])
            self.ilab.config(text=str(self.input[0][0]))
        elif len(self.input)==1 and t=='o':
            self.input.append(y)
            self.ilab.config(text=str(self.input[0][0])+self.input[1])
        elif len(self.input)==2 and t=='n':
            [x,ix],op,iy=self.input[0],self.input[1],i
            if ix==iy or (y==0 and op=='/'):
                self.input=[]
                self.ilab.config(text=' ')
            else:
                self.nop+=1
                # Buttons disablance
                self.buttons[ix].config(state=DISABLED)
                self.buttons[iy].config(state=DISABLED)
                if ix==0 or iy==0:
                    self.bind('<a>',lambda event : None)
                if ix==1 or iy==1:
                    self.bind('<z>',lambda event : None)
                if ix==2 or iy==2:
                    self.bind('<e>',lambda event : None)
                if ix==3 or iy==3:
                    self.bind('<r>',lambda event : None)
                if ix==4 or iy==4:
                    self.bind('<q>',lambda event : None)
                if ix==5 or iy==5:
                    self.bind('<s>',lambda event : None)
                if ix==6 or iy==6:
                    self.bind('<d>',lambda event : None)
                #Creation of new button
                if op=='+':
                    res=x+y
                elif op=='-':
                    res=x-y
                elif op=='x':
                    res=x*y
                elif op=='/':
                    res=x/y
                if res==24 and self.nop==3:
                    self.victory()
                else:
                    self.numbers.append(res)
                    if self.imax==4:
                        self.buttons.append(Mbut(self,self.frame1,text=str(self.numbers[4])[:5],command= lambda: self.process(self.numbers[4],'n',4)))
                        self.bind('<q>',lambda event : self.process(self.numbers[4],'n',4))
                        self.buttons[-1].place(x=50,y=100,width=100,height=100)
                    elif self.imax==5:
                        self.buttons.append(Mbut(self,self.frame1,text=str(self.numbers[5])[:5],command= lambda: self.process(self.numbers[5],'n',5)))
                        self.bind('<s>',lambda event : self.process(self.numbers[5],'n',5))
                        self.buttons[-1].place(x=200,y=100,width=100,height=100)
                    elif self.imax==6:
                        self.buttons.append(Mbut(self,self.frame1,text=str(self.numbers[6])[:5],command= lambda: self.process(self.numbers[6],'n',6)))
                        self.bind('<d>',lambda event : self.process(self.numbers[6],'n',6))
                        self.buttons[-1].place(x=350,y=100,width=100,height=100)
                    self.imax+=1
                self.input=[]
                self.ilab.config(text=' ')
        else:
            self.input=[]
            self.ilab.config(text=' ')

    def cheat(self,event):
        self.ilab.config(text=res.test2(self.numbers)[1])

    def victory(self):
        for i in range(self.imax):
            self.buttons[i].destroy()
        photo = PhotoImage(file='Bravo.GIF')
        self.can.create_image(0,0,image=photo,anchor=NW)
        self.can.image=photo
        self.can.place(x=50,y=0,width=600,height=400)
        #Label(self.frame1,text='24. Bravo.',font=('Courier',44)).place(x=100,y=50,width=550,height=200)
        self.after(1000,lambda: self.reset(None))

    def leave(self,event):
        self.destroy()

F=Fen()
F.focus_force()
F.mainloop()
