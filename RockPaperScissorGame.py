import random



while True:
    l=["ROCK", "PAPER", "SCISSOR"]
    ucount = 0
    ccount = 0
    
    c=int(input('''ENTER YOUR CHOICE(1 or 2):
                1 Play Now
                2 Exit'''))
    if c==1:
        for a in range(1,6):
            userinput=int(input('''Choose Any :
    1 ROCK
    2 PAPER
    3 SCISSOR
                    '''))
            if userinput==1:
                uchoice = "ROCK"
            elif userinput==2:
                uchoice = "PAPER"
            elif userinput==3:
                uchoice="SCISSOR"
            Cchoice = random.choice(l)    
            
            if Cchoice==uchoice:
                print("User choice is ", uchoice)
                print("Computer Choice is ", Cchoice)
                print("The game is Drw !")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="ROCK" and Cchoice=="SCISSOR") or (uchoice=="PAPER" and Cchoice=="ROCK") or (uchoice=="SCISSOR" and Cchoice=="PAPER"):
                print("User choice is ", uchoice)
                print("Computer Choice is ", Cchoice)
                print("User Win the Game !")
                ucount=ucount+1 
            else:
                print("User choice is ", uchoice)
                print("Computer Choice is ", Cchoice)
                print("Computer Win the Game !")
                ccount=ccount+1

        if ucount==ccount:
            print("Final Game Draw .........!")
            print("User Score : ", ucount)
            print("Computer Score : ", ccount)

        elif ucount>ccount:
            print("User win the game .........!")
            print("User Score : ", ucount)
            print("Computer Score : ", ccount)
        else:
            print("Computer Win the Game.........!")
            print("User Score : ", ucount)
            print("Computer Score : ", ccount)
    else:
        break
