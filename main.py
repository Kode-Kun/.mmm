# welcome to .mmm
# puzzle game
# this game is supposed to be run in a command prompt, not a python shell
# pls dont modify or look at anything here before finishing the game
# if you want to have the full /.mmm/ experience, that is
# made by aV01D aka u/_Flying_Octopus_ 

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
    time.sleep(3)
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
    #print("this doesn't have anything to do with the puzzles, but listening to")
    #print("aphex twin's 'rhubarb' really helped me get through the creation of this game.")
    #print("it fits /.mmm/ very well")
    time.sleep(15)
    print("")
    print("good luck, have fun")
    time.sleep(10)
    clear()
# level one
def chooseCommandLvlOne():
    command = ""
    #while ".text:" not in command:
        #print("choose a command")
        #time.sleep(1)
        #command = input("/.mmm/")
    #return command
    while command != "helloworld":
        command = input("/.mmm/")
    return command
# level two
def chooseCommandLvlTwo():
    command = ""
    while command != "iamgreetedbytheredtraveller":
        command = input("/.mmm/")
    return command
# level three
def chooseCommandLvlThree():
    command = ""
    while command != "ifeelsolightwithoutthehumansoul":
        command = input("/.mmm/")
    return command
# level four
def chooseCommandLvlFour():
    command = ""
    while command != "acoldwindrattlesthroughourbones":
        command = input("/.mmm/")
    return command
# level five
def chooseCommandLvlFive():
  while command != "didyouenjoyyourlife?":
    command = input("/.mmm/")
  return command
clear()
displayIntro()
print("Level 1")
time.sleep(2)
print("print('hello world')")
chooseCommandLvlOne()
clear()
time.sleep(2)
print("that was easy")
time.sleep(3)
clear()
time.sleep(2)
print("now shit gets real")
time.sleep(3)
clear()
time.sleep(2)
print("Level 2")
time.sleep(2)
#print("-..-/-/..../.-././.-/-../..---/....-/..---/...--/--.../.----/..---/--...")
print("-..- -··-· - .... .-. . .- -.. -··-· ..--- ....- ..--- ...-- --... .---- ..--- --...")
chooseCommandLvlTwo()
clear()
time.sleep(1)
print("Level 3")
time.sleep(2)
print("user-672045104")
print("discord")
print("/416002061042450432/673650586977042461/mmm29299291167.jpg")
chooseCommandLvlThree()
clear()
print("Level 4")
time.sleep(2)
print("il vero modo di screvere in cifra")
print("1505")
print("D qblo zjrq xtllzrz ttzznuu rie bzqfw")
print("1916")
print("watch?v=n9TJ9xApw0E")
chooseCommandLvlFour()
clear()
time.sleep(2)
print("Level 5")
time.sleep(2)
print("")
chooseCommandLvlFive()
