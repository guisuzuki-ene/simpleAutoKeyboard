from pynput.keyboard import Key, Controller 
from RandomWordGenerator import RandomWord
import time
import random
import _thread

keyboard = Controller()

time.sleep(2)
working = 0

vecAdv = ['rpg cd', 'rpg rd', 'rpg adv', 'rpg heal', 'rpg buy life potion']
vecHunt = ['rpg cd', 'rpg rd', 'rpg hunt']
vecWork = ['rpg cd', 'rpg rd', 'rpg chop']

def autoWork(sleep, vec):
	while(1):
		for word in vec:
			for char in word:
				keyboard.type(char)
				time.sleep(0.12)

			keyboard.press(Key.enter)
		time.sleep(sleep)

def notIdle(sleep):
	while(1):
		r = RandomWord().generate()
		for char in r:
			keyboard.type(char)
			time.sleep(0.12)

		keyboard.press(Key.enter)
		time.sleep(sleep)

start = 1

while(1):	
	if start == 1:
		print('entrou')
		_thread.start_new_thread(autoWork, (random.uniform(75,100), vecHunt))
		time.sleep(5)
		_thread.start_new_thread(autoWork, (random.uniform(630,690), vecAdv))
		time.sleep(8)
		_thread.start_new_thread(autoWork, (random.uniform(330,390), vecWork))
		time.sleep(5)
		_thread.start_new_thread(notIdle, (random.uniform(15,60),))
		start = 0
