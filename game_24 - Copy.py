# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 21:24:55 2018

@author: Paul
"""

from tkinter import *
from random import randint
import res_24 as res

class Fen(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry('700x700')
        self.bind('<F5>',self.reset)
        self.input=[]
        self.numbers=[0,0,0,0]
        
        #Frame 1
        self.frame1= Frame(self)
        self.buttons=[]
        self.frame1.place(x=0,y=100,width=600,height=300)
        
        #Frame 2
        self.frame2= Frame(self)
        Button(self.frame2,text='+',command= lambda: self.process('+','o',0)).place(x=50,y=0,width=100,height=100)
        Button(self.frame2,text='-',command= lambda: self.process('-','o',0)).place(x=200,y=0,width=100,height=100)
        Button(self.frame2,text='x',command= lambda: self.process('x','o',0)).place(x=350,y=0,width=100,height=100)
        Button(self.frame2,text='/',command= lambda: self.process('/','o',0)).place(x=500,y=0,width=100,height=100)
        self.frame2.place(x=0,y=400,width=600,height=100)
        
    def reset(self,event):
        nok=True
        while nok:
            n1,n2,n3,n4=randint(1,13),randint(1,13),randint(1,13),randint(1,13)
            if res.test([n1,n2,n3,n4]):
                self.numbers=[n1,n2,n3,n4]
                nok=False
        self.buttons=[ Button(self.frame1,text=str(self.numbers[0]),command= lambda: self.process(self.numbers[0],'n',0)),Button(self.frame1,text=str(self.numbers[1]),command= lambda: self.process(self.numbers[1],'n',1)),Button(self.frame1,text=str(self.numbers[2]),command= lambda: self.process(self.numbers[2],'n',2)),Button(self.frame1,text=str(self.numbers[3]),command= lambda: self.process(self.numbers[3],'n',3))]
        for i in range(4):
            self.buttons[i].place(x=50+150*i,y=0,width=100,height=100)
        
    def process(self,y,t,i):
        if len(self.input)==0 and t=='n':
            self.input.append([y,i])
            print('hey 1')
        elif len(self.input)==1 and t=='o':
            self.input.append(y)
            print('hey 2')
        elif len(self.input)==2 and t=='n':
            [x,ix],op,iy=self.input[0],self.input[1],i
            if ix==iy or (y==0 and op=='/'):
                self.input=[]
                print('nique')
            else:
                print('hey 3')
                self.buttons[ix].config(state=DISABLED)
                self.buttons[iy].config(state=DISABLED)
                if op=='+':
                    res=x+y
                elif op=='-':
                    res=x-y
                elif op=='x':
                    res=x*y
                elif op=='/':
                    res=x/y
        else:
            self.input=[]
            
F=Fen()
F.focus_force()
F.mainloop()