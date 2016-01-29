#!/usr/bin/env python3
import random
import copy

try:
    import tkinter
    tkinter_available = True
except ImportError:
    tkinter_available = False
    
class Life:
    def __init__(self,size):
        self.size = size
        self.generation = 0
        self.world = [[0 for x in range(size)] for x in range(size)]
        random.seed()
        self.initialize()

    def initialize(self):
        
        for _ in range(random.randint(1,self.size*self.size)):
            x = random.randint(1,self.size-1)
            y = random.randint(1,self.size-1)
            self.world[x][y] = 1
        
        '''
        self.world[9][9] = 1
        self.world[10][10] = 1
        self.world[11][10] = 1
        self.world[11][9] = 1
        self.world[11][8] = 1
        '''
        '''
        self.world[10][10] = 1
        self.world[9][10] = 1
        self.world[8][10] = 1
        '''

    def nextGeneration(self):
        w = copy.deepcopy(self.world)
        change = False
        for y in range(self.size):
            for x in range(self.size):
                n = self.neighbours(x,y)
                if self.world[x][y] == 1 and (n < 2 or n > 3):
                    w[x][y] = 0
                    change = True
                if self.world[x][y] == 0 and n == 3:
                    w[x][y] = 1
                    change = True
        self.world = w
        self.generation += 1
        return change
                    
    def neighbours(self,x,y):
        n = 0
        for j in range(-1,2):
            for i in range(-1,2):
                if (i != 0 or j != 0) and self.world[(x+i)%self.size][(y+j)%self.size] == 1:
                    n += 1
        return n

    def getWorld(self):
        return self.world

def draw(t):
    print(chr(27) + "[2J")
    for i in range(size*2):
        print("-",end="")
    print()

    for y in range(size):
        for x in range(size):
            if t[x][y] == 0:
                print(" ",end=" ")
            elif t[x][y] == 1:
                print("*",end=" ")
        print()
            
    for i in range(size*2):
        print("-", end="")
    print()

def drawCanvas(t, size, canvas):
    cellsize = min(canvas.winfo_width(),canvas.winfo_height())/size
    
    canvas.delete("cells")
    y0 = (canvas.winfo_height() - cellsize*size)/2
    for y in range(size):
        x0 = (canvas.winfo_width() - cellsize*size)/2
        for x in range(size):
            if t[x][y] == 0:
                canvas.create_rectangle(x0, y0, x0+cellsize, y0+cellsize, fill="black",tags="cells")
            elif t[x][y] == 1:
                canvas.create_rectangle(x0, y0, x0+cellsize, y0+cellsize, fill="white",tags="cells")
            x0 += cellsize        
        y0 += cellsize
    


def play(l, size, window, canvas):
    drawCanvas(l.getWorld(), size, canvas)
    l.nextGeneration()
    window.after(500, play, l, size, window, canvas)


size = 30
l = Life(size)

if tkinter_available:
    try:
        window = tkinter.Tk()
    except tkinter.TclError:
        tkinter_available = False

if tkinter_available:
    canvas = tkinter.Canvas(window, width=500, height=500)
    canvas.pack(fill="both", expand="yes")
    #window.resizable(width="false", height="false")
    window.after(500, play, l, size, window, canvas)
    window.mainloop()
else:
    import time
    change = True
    while change:
        draw(l.getWorld())
        change = l.nextGeneration()
        time.sleep(1)
        




