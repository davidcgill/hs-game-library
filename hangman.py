#-------------------------------------------------------------------------------
# Name:        Hangman.py
# Purpose:     To demonstrate coding abilities and skills learned this year
#
# Author:      gilld5528
#
# Created:     19/05/2015
# Copyright:   (c) gilld5528 2015
#-------------------------------------------------------------------------------
#graphics window with small animation in the background(leaves blowing) #and users options
#here (on the main screen) there will be buttons to #choose catagories high page or to #exit
#choose catagorty which will bring you a #word bank and the left (letters= psoitions)
#a drawing window in the middle, #animate the drawing of the elements (gallow and man,hill)
#at the bottom have the #spaces for the words(dashs r large txt) when guessed chaged printed statement #(random word)
#top right have a #score
#after #each round propt for quit or continue (also after each death)
#make a# high scores page (write to document if number is greater than things in high doc
#replace correct number based of if statements if greater than one repleace and bump down (keep top 3 )
# animater death #swing and x on eyes

#eroor handeling same letter twice
#hint sysytem(-points per hint)
#word documents which each have 250 words...split cata into difficulty (based on the length and less clicks to lose)
#make and exit button on each page to kill the program
from graphics import *
from random import *
from Button import *
from tictac import *
from time import *
import homepage

def random(L):
#takes the length of the given list and finds a random letter in that legth
    ran=randint(0,L-1)
    return ran

def exitbutton(win):
    #creates the button which closes the program (to be placed on every page)
    centre=Point(387,393)
    exitbut=Button(win,centre,15,25,"x")
    exitbut.activate("red")
    #places the button in top right and returns the button to user
    return exitbut

def deadman(win,dead,buttonlist,score):
#This program draws a deadman and makes him swing while intrupreting clicks from the user
#it takes in win to draw, dead is used to determine if it is being called on homecreen or after a loss
#button list is a list of the catagorys exit button and difficultly buttons(only used if on homescreen)
#score is used to update highscores and display to user

#set difficulty to "easy" (default) and make it lasedclick (so it will activate when another diff is clicked)
    diff="easy"
    lastclicked=buttonlist[6]
#code bellow draws various components of the man
    ground=Polygon(Point(30,60),Point(55,130),Point(215,130),Point(190,60))
    ground.draw(win)
    ground.setFill("sienna")
#draw ground,nuse, rope and the knot (thickpart)
    ropemain=Oval(Point(155,250),Point(145,320))
    ropemain.draw(win)
    ropemain.setWidth("3")
    ropenot=Line(Point(150,320),Point(150,340))
    ropenot.draw(win)
    ropenot.setWidth("6")
    rope=Line(Point(150,340),Point(150,370))
    rope.draw(win)
    rope.setWidth("2")

    head=Circle(Point(150,275),20)
    head.draw(win)
    head.setFill("white")
#draw head and connecting body stick
    body=Line(Point(150,255),Point(150,190))
    body.draw(win)

    leg1=Line(Point(170,140),Point(150,190))
    leg2=Line(Point(130,140),Point(150,190))
    leg1.draw(win)
    leg2.draw(win)
#draw legs and arms
    arm1=Line(Point(150,240),Point(180,185))
    arm2=Line(Point(150,240),Point(120,185))
    arm1.draw(win)
    arm2.draw(win)

    gallow=Line(Point(150,370),Point(50,370))
    gallow.draw(win)
    gallow.setWidth("3")

    gallowmain=Line(Point(50,370),Point(50,100))
    gallowmain.draw(win)
    gallowmain.setWidth("3")

    eye1=Text(Point(140,275),"X")
    eye2=Text(Point(160,275),"X")
    eye1.setSize(8)
    eye2.setSize(8)
    eye1.draw(win)
    eye2.draw(win)
#draw the gallow structure and draw  the deadeyes with "x" characters
    x=150
    click=False
#initialize x counter and click variable (checks if a catagory has been clicked/when to break)
    if dead==True:
        losepage(win)
        exitbut=exitbutton(win)
    #only if you have just lost print loser statments and add an exit button(because otherwise its brought in by main)
    while 1==1:
    #a forever loop which will just loop until break is called
        n=1
        #reset n, n is a varible used to determine all the characters motion
        while x<=160:
        #a loop which repeats 10 times (could be replaced by for x in range 11)
            body.undraw()
            arm1.undraw()
            arm2.undraw()
            leg1.undraw()
            leg2.undraw()
            #undraw all parts that are to be moved
            body=Line(Point(150,255),Point(150+n,190+n))
            arm1=Line(Point(150+n/3,240),Point(180+n*2,185+n*2))
            arm2=Line(Point(150+n/3,240),Point(120+n*2,185+n*2))
            leg1=Line(Point(170+n*2,140+n*2),Point(150+n,190+n))
            leg2=Line(Point(130+n*2,140+n*2),Point(150+n,190+n))
            #move each part by a number based on the increasing n value (multipliers are for swing top moves less than the bottom)
            #must be like this for the man swings all the way
            arm1.draw(win)
            arm2.draw(win)
            body.draw(win)
            leg1.draw(win)
            leg2.draw(win)
            #redraw moved parts and increase loop counter and move counter(n)
            x=x+1
            n=n+1
            #checks for a mouse click and sleep .1 seconds for a smooth animation
            p=win.checkMouse()
            sleep(.1)
            #if a click has occured
            if p!=None:
                #these first two conditions only will happen if after a loss
                if dead==True and exitbut.clicked(p)==True:
                    win.close()
                    highscore(score)
                    #if dead and x is hit,close window, save highscore and quit program
                    quit()
                elif dead==True:
                    win.close()
                    #on general click when dead close window save highscore
                    #and show them their score compared others on scorepage (which ultimatly leads back to homescreen)
                    highscore(score)
                    scorepage(score)

                else:
                    #otherwise we are on homepage, so pass to see what is clicked
                    diff,lastclicked=clickchecker(p,buttonlist,win,lastclicked,diff)
                    #recieve current difficulty and clicked difficulty (button)



        n=1
        #reset n value for movement of the same speed on the way back
        while x>=150:
            #repeats process described above only movement is returning to base position
            body.undraw()
            arm1.undraw()
            arm2.undraw()
            leg1.undraw()
            leg2.undraw()
            body=Line(Point(150,255),Point(162-n,202-n))
            body.draw(win)
            leg1=Line(Point(194-n*2,164-n*2),Point(162-n,202-n))
            leg2=Line(Point(154-n*2,164-n*2),Point(162-n,202-n))
            arm1=Line(Point(154-n/3,240),Point(204-n*2,209-n*2))
            arm2=Line(Point(154-n/3,240),Point(144-n*2,209-n*2))
            arm1.draw(win)
            arm2.draw(win)
            leg1.draw(win)
            leg2.draw(win)
            x=x-1
            p=win.checkMouse()
            sleep(.1)
            n=n+1
            if p!=None:
                 if dead==True and exitbut.clicked(p)==True:
                    win.close()
                    highscore(score)
                    quit()
                 elif dead==True:
                    win.close()
                    highscore(score)
                    scorepage(score)


                 else:
                    diff,lastclicked=clickchecker(p,buttonlist,win,lastclicked,diff)
        n=1
        while x<=160:
            #repeat process but move up and to the left
            body.undraw()
            arm1.undraw()
            arm2.undraw()
            leg1.undraw()
            leg2.undraw()
            body=Line(Point(150,255),Point(150-n,190+n))
            body.draw(win)
            leg1=Line(Point(170-n*2,140+n*2),Point(150-n,190+n))
            leg2=Line(Point(130-n*2,140+n*2),Point(150-n,190+n))
            arm1=Line(Point(150-n/3,240),Point(180-n*2,185+n*2))
            arm2=Line(Point(150-n/3,240),Point(120-n*2,185+n*2))
            arm1.draw(win)
            arm2.draw(win)
            leg1.draw(win)
            leg2.draw(win)
            x=x+1
            p=win.checkMouse()
            sleep(.1)
            n=n+1
            if p!=None:
               if dead==True and exitbut.clicked(p)==True:
                    win.close()
                    highscore(score)
                    quit()
               elif dead==True:
                    win.close()
                    highscore(score)
                    scorepage(score)


               else:
                    diff,lastclicked=clickchecker(p,buttonlist,win,lastclicked,diff)


        n=1
        while x>=150:
            #repeat procees described above and finish cycle(move man back to starting position)
            body.undraw()
            arm1.undraw()
            arm2.undraw()
            leg1.undraw()
            leg2.undraw()
            body=Line(Point(150,255),Point(138+n,202-n))
            body.draw(win)
            leg1=Line(Point(146+n*2,164-n*2),Point(138+n,202-n))
            leg2=Line(Point(106+n*2,164-n*2),Point(138+n,202-n))
            arm1=Line(Point(146+n/3,240),Point(156+n*2,209-n*2))
            arm2=Line(Point(146+n/3,240),Point(96+n*2,209-n*2))
            arm1.draw(win)
            arm2.draw(win)
            leg1.draw(win)
            leg2.draw(win)
            x=x-1
            p=win.checkMouse()
            sleep(.1)
            n=n+1
            if p!=None:
               if dead==True and exitbut.clicked(p)==True:
                    win.close()
                    highscore(score)
                    quit()
               elif dead==True:
                    win.close()
                    highscore(score)
                    scorepage(score)


               else:
                    diff,lastclicked=clickchecker(p,buttonlist,win,lastclicked,diff)



#This program is called in deadman to check and handle the clicks
def clickchecker(p,buttonlist,win,lastclicked,diff):
#take in the click, list of buttons on homepage,win,lasted diff clicked(button),difficult (txt)
    if buttonlist[5].clicked(p)==True:
        #if index 5 (exitbutton) is clicked close window and quit
        #dont have to save score because the user has not played yet
        win.close()
        quit()
#if button index 0 through 4 is clicked close the window
#and call hangpage with its corresponding catagory,  current difficulty and 0
#0 is the score becasue at start (before game started) score=0
    elif buttonlist[0].clicked(p)==True:
        win.close()
        hangpage("Countries",diff,0)
    elif buttonlist[1].clicked(p)==True:
        win.close()
        hangpage("Animals",diff,0)
    elif buttonlist[2].clicked(p)==True:
        win.close()
        hangpage("Food",diff,0)
    elif buttonlist[3].clicked(p)==True:
        win.close()
        hangpage("Movies",diff,0)
    elif buttonlist[4].clicked(p)==True:
        win.close()
        hangpage("TV Shows",diff,0)

#if none of the catagories aren't clicked check for the user changing the difficulty
    elif buttonlist[6].clicked(p)==True:
        diff="easy"
        #set the txt diff to the aporpiate words
        lastclicked.activate("brown")
        #activate the lasted clicked button
        lastclicked=buttonlist[6]
        buttonlist[6].deactivate()
        #deactivate this button and set it as lastclicked(to be activated next time a diff is clicked)
        return diff,lastclicked
        #return the new difficultly, and the new lastclicked (used button)
    elif buttonlist[7].clicked(p)==True:
        #same process as above for medium button
        diff="medium"
        lastclicked.activate("brown")
        lastclicked=buttonlist[7]
        buttonlist[7].deactivate()
        return diff,lastclicked
    elif buttonlist[8].clicked(p)==True:
        #same process as above for hard button
        diff="hard"
        lastclicked.activate("brown")
        lastclicked=buttonlist[8]
        buttonlist[8].deactivate()
        return diff,lastclicked

#check if the button for highscore page was clicked
    elif buttonlist[9].clicked(p)==True:
        win.close()
        #if so close page and call score page with score as false for it knows a game was just not completed
        scorepage(False)
    else:
        return diff,lastclicked
        #if none above is true blank screen was clicked so return same values as passed and continue animation


def scorepage(score):
    #recieve the current score or false if from homepage
    win=GraphWin("highscores",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("systemhighlight")
    exitbut=exitbutton(win)
    #create window,setcords,exitbutton and colour backgroud
    infile=open("highscore.txt","r")
    #open(for reading) the highscores and initalize spot variable
    spot=300
    #display on page, page's purpose and give directions
    Text(Point(200,350),"Top 5 Highscores!!!").draw(win)
    tx=Text(Point(200,385),"Click anywhere to go to home page or the x to quit")
    tx.setSize(8)
    tx.draw(win)
    #set directions to small for you can differentiate them for highscore txt
    for x in infile:
        #loop through the file and print off the line of txt found in each line of the file
        Text(Point(200,spot),"{0}".format(x)).draw(win)
        #change spot variable to place next score 50 pixels lower
        spot=spot-50
    infile.close()
    #close file,   since file is always only 5 lines long will always loop 5 times
    if score!=False:
        #if not on homepage place the current score on screen (50 lower than last score)
        Text(Point(200,spot),"current score: {}".format(score)).draw(win)
    p=win.getMouse()
    #wait for user click
    if exitbut.clicked(p)==True:
        win.close()
        quit()
        #on x close win and quit program
    else:
        #for a general click close win and open main
        win.close()
        main()

def main():
#this creates and oversees all opperations on the homepage
    win=GraphWin("Hangman!",400,400)
    win.setCoords(0,0,400,400)
    win.setBackground("systemhighlight")

#after seting coords and sizing the screen create buttons
    catagory=Button(win,Point(325,75),100,50,"Countries")
    catagory1=Button(win,Point(325,135),100,50,"Animals")
    catagory2=Button(win,Point(325,195),100,50,"Food")
    catagory3=Button(win,Point(325,255),100,50,"Movies")
    catagory4=Button(win,Point(325,315),100,50,"TV Shows")

    easy=Button(win,Point(50,30),60,25,"Easy")
    medium=Button(win,Point(135,30),60,25,"Medium")
    hard=Button(win,Point(220,30),60,25,"Hard")
    high=Button(win,Point(200,385),100,20,"Highscores")
#makes difficulty buttons and highscore button
    exitbut=exitbutton(win)
    catagory.activate("red")
    catagory1.activate("orange")
    catagory2.activate("green")
    catagory3.activate("yellow")
    catagory4.activate("pink")
    easy.deactivate()
    medium.activate("brown")
    hard.activate("brown")
    high.activate("brown")
#activate all buttons except easy (it is the default difficulty)
    buttonlist=[catagory,catagory1,catagory2,catagory3,catagory4,exitbut,easy,medium,hard,high]
#put all buttons in a list set dead to flase and false as score because no score is needed on the homescreen
    deadman(win,False,buttonlist,False)
#deadman will loop until a button which leads away from the page is clicked , when that happens it will call, the new page directly


def read(cat):
    #this program reads the file for desired catagory by recieving cat via parameters
    filelist=[]
    outfile=open("{}.txt".format(cat),"r")
    #loop through the file and append each line into a list
    for file in outfile:
        filelist.append(file)
    outfile.close()
    #close file and return the list
    return filelist



def hangpage(listtype,diff,score):
#page where the game takes place
   win=GraphWin("Let's play hangman!",400,400)
   win.setCoords(0,0,400,400)
    #draw window, set coords and draw section dividers
   boarder=Line(Point(275,0),Point(275,400))
   boarder1=Line(Point(0,60),Point(275,60))
   boarder.draw(win)
   boarder1.draw(win)
   #Tell the user what difficulty  and catagory they are playing on
   Text(Point(75,385),"{0}: {1}".format(listtype,diff)).draw(win)
   txscore=Text(Point(200,385),"{}.pts".format(score))
   txscore.draw(win)
   #show them their current score (this one only affects at the begining of each game)
   exitbut=exitbutton(win)
   #set a variable to check if the user has won called "Win" also make x button
   Win= False
   part=0
   #start the parts drawn counter to 0
   #call function which draws keyboard
   letters,buttonlist=keyboard(win)
   #recieve list of keyboard keys and the alphabet( also put exitbuuton in the list)
   buttonlist.append(exitbut)
   while 1==1:
        #forever loop which will catch any words that do not work properly (though all words under 44 charcters should)
        blanklist,solution,L=letset(listtype,letters)
        #pass the catagory and the alaphbet| get list of "blanks" and our solution
        tx,tx1,work=Writetxt(blanklist,L,win)
        #pass the blanks to be drawn. Get the line (or two) of txt and if it suceeded
        if work==True:
            #if it worked break and contiue with program and if not a new word will be choosen
            break

   while Win==False:
        #loop until the user has "won" the game
       p=win.getMouse()
       #get a click and  handle it ,recieving the letter clicked
       let=letcheck(p,buttonlist,letters,win,score)
       if let!=False:
        #if the click was not on a letter or the x igonre this and waits for another click
            tx.undraw()
            tx1.undraw()
            #otherwise undraw current txt/blanks( solution in the making)
            blanklist,Win,part,points_earned=letfind(let,solution,blanklist,part,win,L,diff,score)
            #call letfind and get updated blanklist,if u have won,# of parts drawn, and if uve earned points
            tx,tx1,notneed=Writetxt(blanklist,L,win)
            #draw updated blanklist(which will now have letters in if a correct letter is clicked
            if points_earned==True:
                #if the user has gained points give them the coresponding amount to their diff
                if diff=="easy":
                    score=score+1
                elif diff=="medium":
                    score=score+2
                else:
                    score=score+4
            else:
                #if points are not earned you got a wrong letter so subtract a point
                score=score-1
            #update the score
            txscore.undraw()
            txscore=Text(Point(200,385),"{}.pts".format(score))
            txscore.draw(win)
#call white sheet because its faster than undrawing each part and (can't undraw parts because deffined elsewhere)
   whitesheet(win)
   savedman(win,listtype,exitbut,diff,score)
   #call saved man animation which will handel the next decsion

def losepage(win):
    Text(Point(137.5,390),"You Lose!!").draw(win)
    #when user has lost print you lose and tell them how to proceed
    tx=Text(Point(137.5,380),"Click anywhere to restart or X to quit")
    tx.setSize(9)
    tx.draw(win)


def savedman(win,listype,exitbut,diff,score):
#this program will animate a "saved man" and interpret the next click

    Text(Point(200,385),"{}.pts".format(score)).draw(win)
    #print the score then add 10 (looks like its added at each sucesive game won)
    score=score+10
    #draw a man standing on the ground
    ground=Polygon(Point(30,60),Point(55,130),Point(215,130),Point(190,60))
    ground.draw(win)
    ground.setFill("sienna")

    head=Circle(Point(150,200),20)
    head.draw(win)
    head.setFill("white")

    body=Line(Point(150,115),Point(150,180))
    body.draw(win)

    leg1=Line(Point(170,65),Point(150,115))
    leg2=Line(Point(130,65),Point(150,115))
    leg1.draw(win)
    leg2.draw(win)

    arm1=Line(Point(150,150),Point(190,185))
    arm2=Line(Point(150,150),Point(110,185))
    arm1.draw(win)
    arm2.draw(win)
    #after he has been drawn print winning statment and instructions
    tx=Text(Point(150,260),"Thanks for saving me!!")
    tx1=Text(Point(150,245),"Click anywhere to save my friend")
    tx.draw(win)
    tx1.draw(win)

    while 1==1:
    #forever loop
        x=0
        n=1
        #set variables of move(distance) counter and number of motions counter
        while x<=10:
            #until x==10 (could have used a for loop in range 11)
            body.undraw()
            arm1.undraw()
            arm2.undraw()
            leg1.undraw()
            leg2.undraw()
            head.undraw()
            #undraw his whole body
            head=Circle(Point(150,200+n),20)
            body=Line(Point(150,115+n),Point(150,180+n))
            leg1=Line(Point(170,65+n),Point(150,115+n))
            leg2=Line(Point(130,65+n),Point(150,115+n))
            arm1=Line(Point(150,150+n),Point(190,185+n))
            arm2=Line(Point(150,150+n),Point(110,185+n))
            #move each part by n value from origanal position
            arm1.draw(win)
            arm2.draw(win)
            head.draw(win)
            leg1.draw(win)
            leg2.draw(win)
            body.draw(win)
            #draw the part again post movement and check for a click
            p=win.checkMouse()
            if p!=None:
                #if click happens check  and if its on the exit button
                if exitbut.clicked(p)==True:
                    # if on exit button close window, save score (if beats a previous) and quit the program
                    win.close()
                    highscore(score)
                    quit()
                win.close()
                #on general click close the window and call hangpage( which will now have all score earned till this point)
                #use same catagory and difficult for each time until loss
                hangpage(listype,diff,score)

            sleep(.1)
            n=n+1
            x=x+1
            #sleep for smooth animation and increse each variable
        n=1
        #reset n(move magnitude counter)
        while x>=0:
            #same as above but decrease position and x value
            body.undraw()
            arm1.undraw()
            arm2.undraw()
            leg1.undraw()
            leg2.undraw()
            head.undraw()
            head=Circle(Point(150,210-n),20)
            body=Line(Point(150,125-n),Point(150,190-n))
            leg1=Line(Point(170,75-n),Point(150,125-n))
            leg2=Line(Point(130,75-n),Point(150,125-n))
            arm1=Line(Point(150,160-n),Point(190,195-n))
            arm2=Line(Point(150,160-n),Point(110,195-n))
            arm1.draw(win)
            arm2.draw(win)
            head.draw(win)
            leg1.draw(win)
            leg2.draw(win)
            body.draw(win)
            p=win.checkMouse()
            if p!=None:
                if exitbut.clicked(p)==True:
                    win.close()
                    highscore(score)
                    quit()
                win.close()
                hangpage(listype,diff,score)

            sleep(.1)
            x=x-1
            n=n+1

def keyboard(win):
    x,y=300,363
    #initilize height and horizonal values
    index=0
    #set buttonlist to 0 and index counter to blank
    buttonlist=[]
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #list of letters in the alphabet
    for vert in range(6):
        #for my 6 rows of text
        for i in range(4):
            #loop 4 times (4 buttons are placed in each row)
            #make a button with a letter in the aphabet on it
            let=Button(win,Point(x,y),15,40,"{}".format(letters[index]))
            #next loop will index next position because counter (next letter in the alapha)
            let.activate("sky blue")
            #activate the button , colour it blue and add it to a list of buttons
            buttonlist.append(let)
            #increase index and move over next letter
            x=x+25
            index=index+1
    #after each row is done move down and reset x value
        y=y-57
        x=300

    for i in range(2):
        #draw the remaining 2 letters at more spaced out intervals
        let=Button(win,Point(x+10,y),15,40,"{}".format(letters[index]))
        let.activate("sky blue")
        buttonlist.append(let)
        x=x+55
        index=index+1
#return the alphabet and the list of letter buttons
    return letters,buttonlist


def Writetxt(blanklist,L,win):
    T=""
    T1=""
    work=True
    count=0
    index=21
#initilize variables(empty txt strings), if it draws possibly,a counter and an index counter
    if len(blanklist)<=2:
        return T,T1,work
        #say it doesnt work if word is less than two characters
    if L>22:
    #this condition is met if the string is too long to be draw on one line
        for y in range(L-1):
        #for the length of the word
            #check for a space(all our spaces have been tripled for astetic reasons)
            #index will count down from max that will fit on first line and count down
            if blanklist[index]== "   ":
                #once a space is found add the characters up to the space(index)
                for x in blanklist[0:index]:
                    T=T+x
                    #loop and add all terms up till the space (furthest from the start)
                tx=Text(Point(137.5,35),T)
                tx.setFace("arial")
                #set first line of text
                for y in blanklist[index+1:L-1]:
                    T1=T1+y
                    count=count+1
                    #loop second half of the soloution with a count

                tx1=Text(Point(137.5,15),T1)
                tx1.setFace("arial")
                tx.draw(win)
                tx1.draw(win)
                #set second line of text and if count(terms in second line) is greater than 22 its to big
                if count>22:
                    tx.undraw()
                    tx1.undraw()
                    #set work to false and undraw txt
                    work=False
                #reurn strings and if it worked or not
                return tx,tx1,work

            index=index-1
            #reduce index in search of space to split lines on
        return T,T1,False
        #this return statment happens if there is no space found bellow 22 characters (finds a new word)

    else:
        #if it fits on one line
         for x in blanklist:
            T=T+x
            #add each character in blanklist to a empty txt string
         tx=Text(Point(137.5,25),T)
         #plot, set size and draw the line of txt
         tx.setFace("arial")
         tx.draw(win)
         #say it worked, pass the string (and an dot just to meet requirement)
         return tx, Point(270,0),True

def letset(cat,letters):
#this program draws a random word and sets the apporpiate blanks
    filelist=read(cat)
    #read file and get list of words in that catagory and find legth of list
    l=len(filelist)
    num=random(l)
    #get a random number in the appriate range
    solution=filelist[num]
    solution= solution.upper()
    #index the list to the random number and make the "solution" all caps
    blanklist=[]
    ranlist=[]
    L=len(solution)
    #find the length of the solution and
    for i in range (L-1):
        #for the length of the word  append that position to ranlist(list of the actual chacters)
        ranlist.append(solution[i])
        for x in range(26):
            #then for 26 (length of alphabet)
            if solution[i]== letters[x]:
                #in that range check if the letter is equal to a letter in the aplhabet
                blanklist.append("_ ")
                #if it is a leter plot it as an underscore and break (will break to outer for loop, to try next character in answer)
                break
            elif solution[i]==" ":
                #if its a space  draw a triple space and break
                blanklist.append("   ")
                break
        #if the other two conditions arent met in the loop of 26, the character isnt a space or a letter
        else:
            blanklist.append(solution[i])
            #place the character as is into the list
    #return list to be seen by user , solutionlist and the Length
    return blanklist,ranlist,L


def letcheck(p,buttonlist,letters,win,score):
#this programs checks what letter has been been clicked
    count=-1
    #start count as -1 for when entring the loop it starts as 0
    for y in buttonlist:
        count=count+1
        #add one to the count
        if y.clicked(p)== True:
            if count==26:
                #this is true when none were true until the last button
                #the last button in the list is the x so it will save and quit
                win.close()
                highscore(score)
                quit()

            else:
                #if its not 26, index the aplphabet in a corresesponding position(count) as the button was found
                clickedlet=letters[count]
                y.deactivate()
                #this will give u the apporpiate letter which we then return while deactivating the button
                return clickedlet
    return False
    #return false if no button is clicked this will make it wait for another click

def letfind(letter,solution,blanklist,part,win,L,diff,score):
#this program find if the letter clicked is in the answer
    count=0
    check= False
    #initialize the variables check (has it found something)=false and a counter to 0
    for x in solution:
        #loop throught  each character in soloution (will catch
        if x==letter:
            #and if any of the characters in solution is the letter clicked
            blanklist[count]=letter
            #in the position where the match is found set it to the letter
            check=True
            #change check to true for you know youve found at least one match
            if blanklist.count("_ ")==0:
                #this condition is met when you have won so return the completed list and win as true
                return blanklist, True,part,True
        count=count+1
        #increase the count the index of blanklist to modify

    if check==False:
        #when nothing has been replaced  call draw part and return false as points earned (will subtract)
        part=drawpart(part,win,solution,L,diff,score)
        return blanklist, False,part,False

    return blanklist, False,part,True
    #when something has been found true but u havent won say uve earned point

def drawpart(part,win,solution,L,diff,score):
    #this function draws parts for mistakes (more parts on higher dificulty
    if diff=="easy":
        #on easy it will loop once through the draw section
        loop=1
    elif diff=="medium":
        loop=2
    #on medium and hard it will loop twice (the potential to draw 2 objects)
    else:
        loop=2
    for i in range(loop):
        #in this loop it will draw one part each time
        if part==0:
            ground=Polygon(Point(30,60),Point(55,130),Point(215,130),Point(190,60))
            ground.draw(win)
            ground.setFill("sienna")
        #anything less than or = 1
        elif part<=1:

            gallowmain=Line(Point(50,370),Point(50,100))
            gallowmain.draw(win)
            gallowmain.setWidth("3")
        #anything less than or =2
        elif part<=2:
            gallow=Line(Point(150,370),Point(50,370))
            gallow.draw(win)
            gallow.setWidth("3")

        elif part<=3:
            ropemain=Oval(Point(155,250),Point(145,320))
            ropemain.draw(win)
            ropemain.setWidth("3")
            ropenot=Line(Point(150,320),Point(150,340))
            ropenot.draw(win)
            ropenot.setWidth("6")
            rope=Line(Point(150,340),Point(150,370))
            rope.draw(win)
            rope.setWidth("2")
        elif part<=4:
            head=Circle(Point(150,275),20)
            head.draw(win)
            head.setFill("white")
        elif part<=5:
            body=Line(Point(150,255),Point(150,190))
            body.draw(win)
        elif part<=6:
            leg1=Line(Point(170,140),Point(150,190))
            leg1.draw(win)
        elif part<=7:
            leg2=Line(Point(130,140),Point(150,190))
            leg2.draw(win)
        elif part<=8:
            arm1=Line(Point(150,240),Point(180,185))
            arm1.draw(win)
            #so on for subsequent parts until a value greater than 9
        else:
           whitesheet(win)
           Writetxt(solution,L,win)
           Text(Point(200,300),"{}.pts".format(score)).draw(win)
           deadman(win,True,["n","o","t"," ","n","e","e","d","e","d"],score)


#this is nesicary because other wise it would skip statements and draw every other part

        if diff=="easy":
            part= part+1
            #increase part by 1 (corresponfding part is drawn next mistake) 10 trys
        elif diff=="medium":
            part=part+.6
            #two loops so at .6 a peice will draw 1.2 parts each time, this works out to 8 trys
            #ex after first loop it has drawn 0 and than at .6 the second part is drawn... second mistake 1.2 than 1.8 is hit so only one part is drawn that time
        else:
            #draws 2 parts (1 each iteration) so you get 5 trys
            part=part +1
    return part
    #return part value

def highscore(score):
#this function checks if your highscore needs to be updated and if so updates it
    initals=False
    scores=[]
    names=[]
    newscores=[]
    sc=[]
    count=0
    n=0
    check=False
    #initilize all variables lists to be filled, counts and a check
    infile=open("highscore.txt","r")
    for ln in infile:
    #will loop through all 5 entries of the file
        st = ""
        sc = ln.split("  ")
        #split each file on the triple space
        if sc[0] == "\n":
            x = 0
            #catchs newlines that r in the place of numbers
        else:
            x=int(sc[0])
            #if not a newline turn the first string (prev score) into an int


        if len(sc) > 1:
        #as long as there is a username
             lengh=len(sc[1])
             st=sc[1]
             st=st[0:lengh-1]
             #set st to username removing newline

        else:
            st= "Anonymous"
            #if no name label it anon

        scores.append(x)
        names.append(st)
        #append each score to scores and each user name to names
    infile.close()
    #close file and loop through the scores list
    for y in scores:
        if score>=y:
        #once your current score is = or greater than one in the list,they have beat a score
            initals=input("Type your initals (under 10 chatacters):")
            newscores.append(str(score) + "  " + initals[0:11])
            #ask for user name and append  it plus your score to the newscores list
            while count<4:
                #while count is less than 4 we need more values to = top 5
                newscores.append(str(scores[count]) + "  " + names[count])
                count=count+1
                #add next top values n once count =4 break because we have 5 values
            break

        newscores.append(str(y) + "  " + names[count])
        count=count+1
         #if doesnt beat first value append first value to list and add to count
        #will continue until scores list is done so if not greater than any will append origanal values to newscores

    outfile=open("highscore.txt","w")
    #open file to write put each new score  (which has a name and a number) in the file in descending order
    write=newscores[0]+"\n"+newscores[1]+"\n"+newscores[2]+"\n"+newscores[3]+"\n"+newscores[4]
    print(write,file=outfile)
    outfile.close()
    #close file


def whitesheet(win):
    #with win draw a sheet of white the size of the drawing area (blanking out the page)
    whitesheet=Rectangle(Point(0,60),Point(275,400))
    whitesheet.setFill("white")
    whitesheet.draw(win)
