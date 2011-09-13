#!/usr/bin/python
# -*- coding: utf_8 -*-
import os
import random
from Tkinter import *

dictionary = dict(map(lambda s:s.split(), open("dictionary").readlines()))

count = 0
score = 0

f1content = dictionary.keys()
f2content = dictionary.values()


## 
Class Answer ():
	while count < 20:
		os.system('clear')
		wordnum = random.randrange(len(f1content))
		print 'Слово:', f1content[wordnum], ''
		options = [random.randrange(len(f2content)), random.randrange(len(f2content)), random.randrange(len(f2content))]
		options[random.randrange(3)] = wordnum
		print '1 -', f2content[options[0]],
		print '2 -', f2content[options[1]],
		print '3 -', f2content[options[2]],

		answer = input('\n Ваш выбор:')
###
        
###
		if options[answer-1] == wordnum:
			raw_input('\n Верно! Нажмите enter...')
			score += 1
		else:
			raw_input('\n Неверно! Нажмите enter...')
			count += 1
		
		print '\n Набрано очков:', score

obj=Answer
def b1_click ():
    global answer
    answer=1
  #  return answer
def b2_click ():
    global answer
    answer=2
 #   return answer
def b3_click ():
    #global answer
    answer=3
    
#    return answer
window=Tk()
window.title("Viet nam trainer")
button1=Button(window,text='1',width=25,height=5,command=b1_click)
button2=Button(window,text='2',width=25,height=5,command=b2_click)
button3=Button(window,text='3',width=25,height=5,command=b3_click)
label = Label(font='sans 20',text=answer)
label.pack()
button1.pack()
button2.pack()
button3.pack()
window.mainloop()

