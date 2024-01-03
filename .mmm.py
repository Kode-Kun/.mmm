# welcome to .mmm
# puzzle game
# pls dont modify or look at anything here before finishing the game
# if you want to have the full /.mmm/ experience, that is
# made by Kode-Kun

import random
import time
from os import system, name
# clear command function
def clear():
    if name == 'nt':
        _ = system('cls') 

    else:
        _ = system('clear')
# game starts here
def displayIntro():
    print("/.mmm/")
    time.sleep(2)
    print("")
    print("write your answer after /.mmm/. if the answer is right, you will")
    print("move to the next level.")
    print("there are no spaces in the answers.")
    print("if you guess the answer is 'this is the answer', you should write")
    print("thisistheanswer")
    time.sleep(2)
    print("you are free to use any tool, website and software available on your")
    print("pc and on the internet.")
    print("")
    time.sleep(3)
    print("")
    print("good luck, have fun")
    time.sleep(5)
    clear()
def chooseCommand(answer):
   command = ""
   while command != answer:
       command = input("/.mmm/")
# # level five
# def chooseCommandLvlFive():
#   while command != "didyouenjoyyourlife?":
#     command = input("/.mmm/")
#   return command
clear()
displayIntro()
print("Level 1")
time.sleep(1)
print("print('hello world')")
chooseCommand("helloworld")
clear()
time.sleep(1)
print("Level 2")
time.sleep(1)
#print("-..-/-/..../.-././.-/-../..---/....-/..---/...--/--.../.----/..---/--...")
print("-..- -··-· - .... .-. . .- -.. -··-· ..--- ....- ..--- ...-- --... .---- ..--- --...")
chooseCommand("iamgreetedbytheredtraveller")
clear()
time.sleep(1)
print("Level 3")
time.sleep(2)
print("user-672045104")
print("discord")
print("/416002061042450432/673650586977042461/mmm29299291167.jpg")
chooseCommand("ifeelsolightwithoutthehumansoul")
clear()
print("Level 4")
time.sleep(2)
print("il vero modo di screvere in cifra")
print("1505")
print("D qblo zjrq xtllzrz ttzznuu rie bzqfw")
print("1916")
print("watch?v=n9TJ9xApw0E")
chooseCommand("acoldwindrattlesthroughourbones")
clear()
time.sleep(2)
#print("Level 5")
#time.sleep(2)
#print("")
#chooseCommandLvlFive()
