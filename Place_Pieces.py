#pieces on board
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
class pieces():
    def __init__(self):
        root.mainloop()
    def black_pawn(self):
        bpawn = Image.open('black_pawn.png')
        bpawn1 = bpawn.resize((70,90))
        self.bpawn = ImageTk.PhotoImage(bpawn1)
        for i in range(64):
            if self.coords[i][1]==1:
                self.coords[i][0].configure(image=self.bpawn,height=70,width=70)
                print(self.coords[i][0]['image'])
pieces()
