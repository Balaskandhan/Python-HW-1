'''
Created on Apr 14, 2015

@author: balas
'''
number_of_tries = 0
def guessgame(low,up):
    global number_of_tries
    number_of_tries = number_of_tries + 1
    guess=(low+up)//2
    print("----------------------------------------------")
    isNumber=input("Is the number "+str(guess)+"?"+"\nPress(y-yes and N-no):")
    if isNumber=='y' or isNumber=='Y':
        return guess
    elif isNumber=='n' or isNumber=='N':
        isIt=input("Is the number larger than "+str(guess)+"?"+"\nPress(y-yes and N-no):")
        if isIt=='y' or isIt=='Y':
            return guessgame(guess+1,up)
        elif isIt=='n' or isIt=='N':
            return guessgame(low,guess-1)
    else:
        print("Wrong option!!!\nTry again with correct option")
        
        
        
low=1
up=100
play_Again = True
name=input("Hi,What is your name? ")
option=input("Hello, "+name+"\nDo you want to play a game?"+"\nPress(y-yes and N-no): ")
while play_Again:
    if option=='n' or option== 'N':
        print("Bye Bye")
    elif option=='y' or option=='Y':
        print("Ok,Now Guess any number between 1 and 100."+"\nI will try to find it.")
        guessgame(low,up)
        play_Again=False
        print("It took me "+str(number_of_tries)+" times for me to guess the number")
        play_Again = input("Do you want to play again?\nPress(y-yes and N-no):")
        if(play_Again=='y' or play_Again=='Y'):
            play_Again=True
        else:
            play_Again=False
    else:
        print("Wrong option!!!\nTry again with correct option")