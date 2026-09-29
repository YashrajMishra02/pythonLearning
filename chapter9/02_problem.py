'''
Implement a game of Snake, Water and Gun in Python. The rules of the game are:
1 for snake
-1 for water
0 for gun

'''

import random
def game():
    dict = {"snake": 1,"water":-1,"gun":0}
    revdict = {1: "snake",-1: "water",0:"gun"}
    comp = random.choice([-1,0,1])
    yourchoicestr = input("Enter your character: ")
    yrChoice = dict[yourchoicestr]
    highscore = 0
    print("your current high score is "+highscore)
    print(f"you choose {yourchoicestr}\ncomputer choose {revdict[comp]}")
    if(comp == yrChoice):
        print("Draw match")
    else:
        if(comp == 1 and yrChoice == -1):
            print("You Loose")
            highscore -= 1
        elif(comp == 1 and yrChoice == 0):
            print("You Loose")
            highscore -= 1
        elif(comp == 0 and yrChoice == 1):
            print("You Win")
            highscore += 2
        elif(comp == 0 and yrChoice == -1):
            print("You Win")
            highscore += 2
        elif(comp == -1 and yrChoice == 1):
            print("You Win")
            highscore += 2
        elif(comp == -1 and yrChoice == 0):
            print("You Loose")
            highscore -= 1
        else:
            print("Something went wrong")
    return highscore

with open("hi_score.txt",'+a') as f:
    scrStr = f.read()
    scrStr = scrStr.replace(" ","")
    score = int(scrStr)
    highscore = game()
    if(highscore > score):
        f.write(highscore)
        print("You beat the highscore")
    else:
        print("You didn't beat the highscore")
    
