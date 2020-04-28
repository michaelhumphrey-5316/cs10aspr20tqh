#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:09:21 2020

@author: michaelhumphrey
"""

import tkinter
from tkinter import Label


top = tkinter.Tk()
top.geometry('400x600')

top.title("MTg card Finder")
w = Label(top, text="")
#w.grid(row=0, column=0, columnspan=9,)

color_l=[]
#things that can be togeled within the buttons

global color
global green_mana
global black_mana
global blue_mana
global white_mana
global red_mana

green = False
black= False
blue = False
white= False
red = False



color=" "
def show_entry_fields():
    print("power: %s\nToughnesse: %s\nrarity%s\nType" % (power.get(), toughnes.get(), rarity.get(), Type.get()))
    power.delete(0, tkinter.END)
    toughnes.delete(0, tkinter.END)


def oneCallBack():
    if green_mana == False:
        green_mana=True
    print("green")
    color_l.append(color)

def twoCallBack():#black
   color="black"
   color_l.append(color)
def threeCallback():#blue
   color="blue"
   color_l.append(color)
def fourCallback():#white
   color="white"
   color_l.append(color)
def fiveCallback():#red
   color="red"
   color_l.append(color)
def filtersCallback():#red
   color="red"
   color_l.append(color)


def Apply_powerCallback():
   w.config(text="")
def dotcallback():
   w.config(text=w.cget("text")+".")

Green = tkinter.Button(top, text ="green", command = oneCallBack, height=4, width=4, activebackground= "red")
Black = tkinter.Button(top, text ="black", command = twoCallBack, height=4, width=4)
Blue = tkinter.Button(top, text ="blue", command = threeCallback, height=4, width=4)
White = tkinter.Button(top, text ="white", command = fourCallback, height=4, width=4)
Red = tkinter.Button(top, text ="Red", command = fiveCallback, height=4, width=4)
Apply_filters = tkinter.Button(top, text ="Apply_filters", command = filtersCallback, height=5, width=12)

#B8 = tkinter.Entry(top, text ="8", command = eightCallback, height=4, width=4)
tkinter.Label(top, text="power").place(y=80, x=2)#e1
Power_button = tkinter.Button(top, text ="apply", command = filtersCallback, height=5, width=12)

tkinter.Label(top, text="toughness").place(y=100, x=2)#e2
#mabey have this text box be buttons instead
tkinter.Label(top, text="rarity").place(y=120, x=2)#e3
tkinter.Label(top, text="type").place(y=140, x=2)#e4
tkinter.Label(top, text="CmC").place(y=160, x=2)#e4
tkinter.Label(top, text="X").place(y=300, x=2)#e

power = tkinter.Entry(top)
Power_button = tkinter.Button(top, text ="apply", command = Apply_powerCallback, height=2, width=2)
toughnes = tkinter.Entry(top)
rarity = tkinter.Entry(top)
Type = tkinter.Entry(top)
CMC = tkinter.Entry(top)
List_filters = tkinter.Label(top)

tkinter.Button(top, 
          text='Show', command= show_entry_fields).place(y=400, 
                                                       x=100,)
#           y         x
power.place(y=80, x=60)#power
Power_button.place(y=80, x=250)#power

toughnes.place(y=100, x=60)#toughnes
rarity.place(y=120, x= 60)#rarity
Type.place(y=140, x= 60)#type
CMC.place(y=160, x=60)#power

Green.place(y=10, x=0)#green
Black.place(y=10, x=40)#black
Blue.place(y=10, x=80)#blue
White.place(y=10, x=120)#white
Red.place(y=10, x=160)#red

Apply_filters.place(y=200, x=0)#Apply_filters
List_filters.place(y=300, x=0)#List_filters

w.place(x=100, y=70)

top.mainloop()
