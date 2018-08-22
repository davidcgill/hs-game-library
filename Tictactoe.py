#-------------------------------------------------------------------------------
# Name:        Tic Tac toe
# Purpose:
#
# Author:      gilld
#

#-------------------------------------------------------------------------------
from graphics import *
from random import *
from Button import *
from time import *
import homepage

def exitbutton(win):
    #creates the button which closes the program (to be placed on every page)
    centre=Point(387,393)
    exitbut=Button(win,centre,15,25,"x")
    exitbut.activate("red")
    #places the button in top right and returns the button to user
    return exitbut
#this program heads the tic tac toe minigame
def ticmain():
    import homepage
    win=GraphWin("Hangman!",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("systemhighlight")
    exitbut=exitbutton(win)
    #create the window make an exit button
    butlist=makebuttons(win)
    Line(Point(50,150),Point(350,150)).draw(win)
    Line(Point(50,250),Point(350,250)).draw(win)
    Line(Point(150,50),Point(150,350)).draw(win)
    Line(Point(250,50),Point(250,350)).draw(win)
    #draw the grind and recieve a list of the 9 buttons (one in each sector)
    won=False
    turn="x"
    count=0
    checklist=[]
    letlist=[]
    #initialize variables empty lists to handel clicks a counter and whos turn it is
    tx=Text(Point(200,375),"x's turn")
    tx.draw(win)
#draw changable text object (user feed back) and entre loop, finishs when u win or board is full
    while won!=True and count<9:
        p=win.getMouse()
        #get mouse click and quit if x is hit
        if exitbut.clicked(p)==True:
            win.close()
            quit()
#otherwise loop through to see  which button was clicked
        for i in range(9):
            if butlist[i].clicked(p)==True:
                #if one of the buttons deactivate it and append its repreentitive number
                #each button is numbered based on its position, also appen whos turn it is in a corresponding position in a second list
                butlist[i].tictacdeactivate(turn)
                #special deactivation which will place a label of who clicked on it
                checklist.append(str(i))
                letlist.append(turn)
                #call to check if u have won, if you have you will receive won as true and which player is a winner
                won,winner=checkwin(checklist,letlist,win)
        #if you havent won change to the other players turn (and show this change to the user)
        if turn=="x":
            tx.setText("O's turn")
            turn="o"

        else:
            tx.setText("x's turn")
            turn="x"
        #increase the count , once out is 9 quit loop (the game board has been filled with no winner)
        count=count+1
    if won==True:
        tx.setText("{} wins!!".format(winner))
        #if u win print winner, or if u have tied display that
    else:
        tx.setText("It's a {}".format(winner))

    homescreen=Button(win,Point(100,375),80,20,"homepage")
    playagain=Button(win,Point(300,375),80,20,"Play again")
    homescreen.activate("yellow")
    playagain.activate("yellow")
    #make and activate buttons of descion to make (home page or keep playing)
    while 1==1:
        p=win.getMouse()
        if playagain.clicked(p)==True:
            win.close()
            ticmain()

        elif homescreen.clicked(p)==True:
            win.close()
            homepage.homepage()
        elif exitbut.clicked(p)==True:
            win.close()
            quit()
        #loop forever until the user has clicked a valid button

def makebuttons(win):
    buttlist=[]
    y=300
    #list of buttons and starting height , loop bellow creates 3 rows
    for i in range (3):
        x=100
        #horizonal position to be reset each loop
        for q in range(3):
            but=Button(win,Point(x,y),100,100,"")
            but.tictactivate()
            #special activation for tictac where there are no boarders on the button
            buttlist.append(but)
            x=x+100
            #append buttons to a list and make each collumn (the buttons side by side)
        y=y-100
        #set to next vertical row and when finished all three return list of the buttons
    return buttlist


def checkwin(checklist,letlist,win):
        tx=""
        for i in checklist:
            tx=tx+i
            #change list of  numbered spots into a string for we can use the find command
#this following section checks each winning scenario indivualy
    #sets the variables x,y,z to find the numbers (buttons clicked) of the givin winning scenario
    #find comand returns a value over -1 if true
        x,y,z=tx.find("0"),tx.find("1"),tx.find("2")
        #check if each value is found (has been clicked) than if it has been
        #checl in the other list in correspoding loctions whos turn it was when clicked
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
            #if the same user clicked all the spots draw a line showing winning play and return the winner and the fact u have won
              Line(Point(50,300),Point(350,300)).draw(win)
              return True,letlist[x]
    #code does the same for all other combinations reseting x,y,z to find other winning combs
        x,y,z=tx.find("3"),tx.find("4"),tx.find("5")
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
            Line(Point(50,200),Point(350,200)).draw(win)
            return True,letlist[x]
        x,y,z=tx.find("6"),tx.find("7"),tx.find("8")
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
              Line(Point(50,100),Point(350,100)).draw(win)
              return True,letlist[x]
        x,y,z=tx.find("0"),tx.find("3"),tx.find("6")
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
            Line(Point(100,50),Point(100,350)).draw(win)
            return True,letlist[x]
        x,y,z=tx.find("1"),tx.find("4"),tx.find("7")
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
            Line(Point(200,50),Point(200,350)).draw(win)
            return True,letlist[x]
        x,y,z=tx.find("2"),tx.find("5"),tx.find("8")
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
            Line(Point(300,50),Point(300,350)).draw(win)
            return True,letlist[x]
        x,y,z=tx.find("0"),tx.find("4"),tx.find("8")
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
            Line(Point(100,300),Point(300,100)).draw(win)
            return True,letlist[x]
        x,y,z=tx.find("2"),tx.find("4"),tx.find("6")
        if x >-1 and y>-1 and z>-1 and letlist[x]==letlist[y]==letlist[z]:
              Line(Point(300,300),Point(100,100)).draw(win)
              return True,letlist[x]
        #sorry for code here probably a better way to do it, but this way works
        else:
            return False,"Draw"
        #if nothing is clicked pass that there is no winner yet
