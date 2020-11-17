from pynput.keyboard import Key, Controller 
import time
import random

keyboard = Controller()

time.sleep(5)

vec = ['rpg cd', 'rpg rd', 'rpg hunt', 'rpg adv', 'rpg heal', 'rpg buy life potion', 'rpg chop']

vecIdle = ['nem fodendo', 'mó vacilo', 'vai me taxar n', 'epic guard corno', 'ta trollando ctz',
'bot eficiente', 'estamos vendo', 'hauehauehauea', 'mano', 'qual foi mano', 'configura isso direito']

while(1):
	for word in vec:
		print(word)
		for char in word:
			keyboard.press(char)
			keyboard.release(char)
			time.sleep(0.15)

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
	for idleWord in random.sample(vecIdle, 2):
		for char in idleWord:
			keyboard.press(char)
			keyboard.release(char)
			time.sleep(0.15)

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)
	
	time.sleep(random.uniform(60,90))