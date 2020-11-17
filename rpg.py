# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:47:13 2020

@author: marcelo
"""

from pynput.keyboard import Controller, Key
import time
import random
import string

keyboard = Controller()

comando = 0
flag_hunt = 0
flag_potion = 0
flag_adv = 0
flag_str = 0
flag_chop = 0
flag_fish = 0
vec_ale = ["rpg p", "rpg i", "rpg cd", "rpg rd", "rpg recipes", "rpg p @Suzuki", "rpg p @mouran1", "rpg i @Suzuki", "rpg i @mouran1"]

while(1):
    comando = 0
    
    def comandos(string):
        for character in string:
            keyboard.type(character)
            delay = 0.01
            time.sleep(delay)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
    def random_string(length1, length2):
        letters = string.ascii_letters
        final_length = random.choice(range(length1, length2))
        result_str = ''.join(random.sample(letters, final_length))
        comandos(result_str)

    """Hunt"""
    if (comando == 0):
        time.sleep(random.uniform(65, 90))
        comandos("rpg hunt")
        flag_hunt += 1
        flag_chop += 1
        flag_adv += 1
        
        """Heal, Buy Potion"""
        if (flag_hunt >= 3):
            time.sleep(5)
            comandos("rpg heal")
            flag_potion = 1
            if(flag_potion == 1):
                time.sleep(random.uniform(6, 20))
                comandos("rpg buy life potion 1")
                flag_potion = 0
        
        """Chop, Fish"""
        if(flag_chop >= 5):
            if(flag_fish >= 2):
                time.sleep(5)
                comandos("rpg fish")
                flag_fish = 0
            else:
                time.sleep(5)
                comandos("rpg chop")
                flag_fish += 1
            flag_chop = 0
                
        """Adventure"""
        if (flag_adv >= 60):
            time.sleep(5)
            comandos("rpg heal")
            time.sleep(random.uniform(6, 10))
            comandos("rpg buy life potion 1")
            time.sleep(random.uniform(6,10))
            comandos("rpg adv")
            flag_adv += 0
    
    """String aleatorias"""
    while(flag_str <= 5):
        time.sleep(random.uniform(6, 20))
        random_string(5, 20)
        time.sleep(5)
        for vec in random.sample(vec_ale, 1):
            comandos(vec)
        flag_str += 1
    flag_str = 0


"""
flag = 0
flag2 = 0

while(1):
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
        def chop(string):
            for character in string:
                keyboard.type(character)
                delay = 0.01
                time.sleep(delay)
            keyboard.press(Key.enter)         
        chop("rpg chop")
        flag2 = 0
"""