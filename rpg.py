# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

from pynput.keyboard import Controller, Key
import time
import random

keyboard = Controller()
flag = 0
flag2 = 0

while(1):
    time.sleep(random.uniform(0,2))
    def aleatorios(string):
        for character in string:
            keyboard.type(character)
            delay = 0.01
            time.sleep(delay)
        keyboard.press(Key.enter) 
            
    aleatorio = random.randrange(3)
    if(aleatorio == 0):
        time.sleep(5)
        aleatorios("rpg rd")
    elif(aleatorio == 1):
        time.sleep(5)
        aleatorios("rpg cd")
    else:
        time.sleep(5)
        aleatorios("rpg p")
    
    time.sleep(65)
    def hunt(string):
        for character in string:
            keyboard.type(character)
            delay = 0.01
            time.sleep(delay)
        keyboard.press(Key.enter)
    hunt("rpg hunt")
    flag += 1
    flag2 +=1
    
    if(flag == 3):
        time.sleep(5)
        def buy(string):
            for character in string:
                keyboard.type(character)
                delay = 0.01
                time.sleep(delay)
            keyboard.press(Key.enter)
        buy("rpg buy life potion 1")
        
        time.sleep(5)
        def heal(string):
            for character in string:
                keyboard.type(character)
                delay = 0.01
                time.sleep(delay)
            keyboard.press(Key.enter)         
        heal("rpg heal")
        flag = 0
    
    if(flag2 == 5):
        time.sleep(5)
        def fish(string):
            for character in string:
                keyboard.type(character)
                delay = 0.01
                time.sleep(delay)
            keyboard.press(Key.enter)         
        fish("rpg fish")
        flag2 = 0
        