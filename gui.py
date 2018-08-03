# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:05:54 2018

@author: sol-relay-2
"""
from tkinter import Tk, Label, Button

class aGUI:
    def __init__(self, master):
        self.master = master
        master.title("A GUI")
        
        self.label = Label(master, text="First GUI")
        self.label.pack()
        
        self.greet_button = Button(master, text="Greet", command = self.greet)
        self.greet_button.pack()
        
        self.close_button = Button(master, text = "Close", command = master.quit)
        self.close_button.pack()
        
    def greet(self):
        print("Suh bro")

root = Tk()
my_gui = aGUI(root)
root.mainloop()