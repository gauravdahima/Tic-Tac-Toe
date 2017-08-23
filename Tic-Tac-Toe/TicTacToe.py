from graphics import *
import sys


def get_box(px,py):
    if(px > 0 and px <= 100 and py > 0 and py <= 100 ):
        return 0

    if(px > 100 and px <= 200 and py > 0 and py <= 100 ):
        return 1

    if(px > 200 and px <= 300 and py > 0 and py <= 100 ):
        return 2

    if(px > 0 and px <= 100 and py > 100 and py <= 200 ):
        return 3

    if(px > 100 and px <= 200 and py > 100 and py <= 200 ):
        return 4

    if(px > 200 and px <= 300 and py > 100 and py <= 200 ):
        return 5

    if(px > 0 and px <= 100 and py > 200 and py <= 300 ):
        return 6

    if(px > 100 and px <= 200 and py > 200 and py <= 300 ):
        return 7

    if(px > 200 and px <= 300 and py > 200 and py <= 300 ):
        return 8

def tic_tac_toe_O(entries,win, p2x, p2y):
    box = get_box(p2x,p2y)
    if(box == 0):
        center = Point(50,50)
        entries[0][0] = 2
    elif(box == 1):
        center = Point(150,50)
        entries[1][0] = 2
    elif(box == 2):
        center = Point(250,50)
        entries[2][0] = 2
    elif(box == 3):
        center = Point(50,150)
        entries[0][1] = 2
    elif(box == 4):
        center = Point(150,150)
        entries[1][1] = 2
    elif(box == 5):
        center = Point(250,150)
        entries[2][1] = 2
    elif(box == 6):
        center = Point(50,250)
        entries[0][2] = 2
    elif(box == 7):
        center = Point(150,250)
        entries[1][2] = 2
    elif(box == 8):
        center = Point(250,250)
        entries[2][2] = 2
    
    circle = Circle(center,50)
    circle.setOutline('green')
    circle.setWidth(5)
    circle.draw(win)


def tic_tac_toe_X(entries,win, p1x, p1y):
    
    box = get_box(p1x,p1y)
    if(box == 0):
        line1 = Line(Point(0,0),Point(100,100))
        line2 = Line(Point(0,100),Point(100,0))
        entries[0][0] = 1

    elif(box == 1):
        line1 = Line(Point(100,0),Point(200,100))
        line2 = Line(Point(100,100),Point(200,0))
        entries[1][0] = 1

    elif(box == 2):
        line1 = Line(Point(200,0),Point(300,100))
        line2 = Line(Point(200,100),Point(300,0))
        entries[2][0] = 1

    elif(box == 3):
        line1 = Line(Point(0,100),Point(100,200))
        line2 = Line(Point(0,200),Point(100,100))
        entries[0][1] = 1

    elif(box == 4):
        line1 = Line(Point(100,100),Point(200,200))
        line2 = Line(Point(100,200),Point(200,100))
        entries[1][1] = 1

    elif(box == 5):
        line1 = Line(Point(200,100),Point(300,200))
        line2 = Line(Point(200,200),Point(300,100))
        entries[2][1] = 1

    elif(box == 6):
        line1 = Line(Point(0,200),Point(100,300))
        line2 = Line(Point(0,300),Point(100,200))
        entries[0][2] = 1

    elif(box == 7):
        line1 = Line(Point(100,200),Point(200,300))
        line2 = Line(Point(100,300),Point(200,200))
        entries[1][2] = 1

    elif(box == 8):
        line1 = Line(Point(200,200),Point(300,300))
        line2 = Line(Point(200,300),Point(300,200))
        entries[2][2] = 1

    line1.setFill('red')
    line2.setFill('red')
    line1.setWidth(5)
    line2.setWidth(5)
    line1.draw(win)
    line2.draw(win)

def check(entries):
    if(entries[0][0] == 1 and entries[0][1] == 1 and entries[0][2] == 1):
        line = Line(Point(50,0),Point(50,300))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[1][0] == 1 and entries[1][1] == 1 and entries[1][2] == 1):
        line = Line(Point(150,0),Point(150,300))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[2][0] == 1 and entries[2][1] == 1 and entries[2][2] == 1):
        line = Line(Point(250,0),Point(250,300))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][0] == 1 and entries[1][0] == 1 and entries[2][0] == 1):
        line = Line(Point(0,50),Point(300,50))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][1] == 1 and entries[1][1] == 1 and entries[2][1] == 1):
        line = Line(Point(0,150),Point(300,150))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][2] == 1 and entries[1][2] == 1 and entries[2][2] == 1):
        line = Line(Point(0,250),Point(300,250))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][0] == 1 and entries[1][1] == 1 and entries[2][2] == 1):
        line = Line(Point(0,0),Point(300,300))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][2] == 1 and entries[1][1] == 1 and entries[2][0] == 1):
        line = Line(Point(0,300),Point(300,0))
        line.setFill('red')
        line.setWidth(5)
        line.draw(win)
        return True

    elif(entries[0][0] == 2 and entries[0][1] == 2 and entries[0][2] == 2):
        line = Line(Point(50,0),Point(50,300))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[1][0] == 2 and entries[1][1] == 2 and entries[1][2] == 2):
        line = Line(Point(150,0),Point(150,300))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[2][0] == 2 and entries[2][1] == 2 and entries[2][2] == 2):
        line = Line(Point(250,0),Point(250,300))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][0] == 2 and entries[1][0] == 2 and entries[2][0] == 2):
        line = Line(Point(0,50),Point(300,50))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][1] == 2 and entries[1][1] == 2 and entries[2][1] == 2):
        line = Line(Point(0,150),Point(300,150))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][2] == 2 and entries[1][2] == 2 and entries[2][2] == 2):
        line = Line(Point(0,250),Point(300,250))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][0] == 2 and entries[1][1] == 2 and entries[2][2] == 2):
        line = Line(Point(0,0),Point(300,300))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True
    elif(entries[0][2] == 2 and entries[1][1] == 2 and entries[2][0] == 2):
        line = Line(Point(0,300),Point(300,0))
        line.setFill('green')
        line.setWidth(5)
        line.draw(win)
        return True

def main():

    global win
    global boxsize
    entries = [[-1 for x in range(3)] for y in range(3)]

    windowsize = 300
    squares = 3
    boxsize = 100

    win = GraphWin("Tic Tac Toe", windowsize, windowsize)

    for i in range(squares - 1):
        hline = Line(Point(0, (windowsize/squares) * (i + 1)), Point(windowsize,  (windowsize/squares) * (i + 1)))
        hline.draw(win)
        vline = Line(Point((windowsize/squares) * (i + 1), 0), Point((windowsize/squares) * (i + 1), windowsize))
        vline.draw(win)

    for i in range(1,10):
        print("Player 1: click a square.")
        p1mouse = win.getMouse()
        p1x = p1mouse.getX()
        p1y = p1mouse.getY()
        tic_tac_toe_X(entries,win, p1x, p1y)
        if(check(entries) == True):
            print("Player 1 is the winner.")
            break
        
        print("Player 2: click a circle.")
        p2mouse = win.getMouse()
        p2x = p2mouse.getX()
        p2y = p2mouse.getY()
        tic_tac_toe_O(entries,win, p2x, p2y)
        if(check(entries) == True):
            print("Player 2 is the winner.")
            break

    print("Enter 1 to play again, 0 to Exit : ")
    x = int(input())
    if(x==1):
        win.close()
        main()
    else:
        sys.exit()

main()