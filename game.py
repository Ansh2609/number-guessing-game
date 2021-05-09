# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:48:50 2021

@author: anshs
"""
x="random number guess game"
print(x.center(100))
import random
x=random.randint(0,101)
while True:
    user_input=int(input("enter a number between 0 and 100 : "))
    if x != user_input:
        if x > user_input:
            print("try again, go higher")
        elif x < user_input:
            print("try again, go lower")
    elif x == user_input:
        print("game over")
        break