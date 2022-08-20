#Coordinate game for chess
from tkinter import *
import random
root = Tk()

class game():
    def __init__(self):
        self.chessboard()
        self.colorboxes()
        self.generate()
        self.scores()
        root.mainloop()

    def chessboard(self):
        self.rows = ["a","b","c","d","e","f","g","h"]
        self.col = [8,7,6,5,4,3,2,1]
        self.coords = []
        for r in range(8):
            for c in range(8):
                but = Button(root,text="",height=4,width=9,command=lambda x=r,y=c: self.click(x,y))
                but.grid(row=r,column=c)
                self.coords.append((but,r,c))

        for i in range(64):
            if self.coords[i][1]==7:
                self.coords[i][0].configure(text=self.rows[self.coords[i][2]],anchor='sw')
            
        for i in range(64):
            if self.coords[i][2]==0:
                self.coords[i][0].configure(text=self.col[self.coords[i][1]],anchor='nw')
                if self.coords[i][1]==0:
                    self.coords[i][0].configure(text=8,anchor='nw')

    def colorboxes(self):
        for i in range(64):
            if  (int(self.coords[i][1]) + int(self.coords[i][2])) % 2 !=0 :
                self.coords[i][0].configure(bg='lime green')

    def click(self,r,c):      
        self.response = str(self.rows[c]) + str(self.col[r])
        self.check()
    
    def generate(self):
        x1 = random.randint(0,7)
        x2 = random.randint(0,7)
        self.ans = str(self.rows[x1]) + str(self.col[x2])
        lab1 = Label(root,text=self.ans)
        lab1.grid(row=10,column=1)

    def check(self):
        if self.response==self.ans:
            self.score["text"] = int(self.score["text"]) + 1
            self.generate()

    def scores(self):
        lab = Label(root,text="Scores: ")
        lab.grid(row=11,column=0)
        self.score=Label(root,text='0')
        self.score.grid(row=11,column=1)

        
game()