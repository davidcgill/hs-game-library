#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gilld
#
# Created:     19-12-2016
# Copyright:   (c) gilld 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
from random import *
from Button import *
import hangman
import Tictactoe

def exitbutton(win):
    #creates the button which closes the program (to be placed on every page)
    centre=Point(387,393)
    exitbut=Button(win,centre,15,25,"x")
    exitbut.activate("red")
    #places the button in top right and returns the button to user
    return exitbut

def homepage():
    win=GraphWin("Chess",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("systemhighlight")
    ext=exitbutton(win)

    game=Button(win,Point(325,75),100,50,"TBD")
    game1=Button(win,Point(325,135),100,50,"Checkers")
    game2=Button(win,Point(325,195),100,50,"Chess")
    game3=Button(win,Point(325,255),100,50,"Tictactoe")
    game4=Button(win,Point(325,315),100,50,"Hangman")
    game4.activate("red")
    game3.activate("orange")
    game2.deactivate()
    game1.deactivate()
    game.deactivate()
    buttonlist=[game,game1,game2,game3,game4,ext]
    while 1==1:
        p=win.getMouse()
        if buttonlist[5].clicked(p)==True:
            win.close()
            quit()
        elif buttonlist[4].clicked(p)==True:
            win.close()
            hangman.main()
        elif buttonlist[3].clicked(p)==True:
            win.close()
            Tictactoe.ticmain()
        elif buttonlist[2].clicked(p)==True:
            win.close()
        elif buttonlist[1].clicked(p)==True:
            win.close()
        elif buttonlist[0].clicked(p)==True:
            win.close()

    #else move title movement word games bouncing back and forth






