from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

import numpy as np
import json as js
import os


class createWindow:
    # initialize the window with a set frame, create some variables
    def __init__(self, main):
        main.title('Test')
        main.geometry("600x600")
        main.resizable(False, False)
        self.mainView = main
        self.drawText()
        self.folderPath = StringVar()
        self.imageSet = []
        # this button calls the browseFolder plugin
        browseButton = Button(self.mainView, text='Browse Files', command=self.browseFolder)
        browseButton.place(relx=0.1, rely=0.95, anchor='center')
        
    def drawText(self, *args):
        title = "Annotation Scripter!"
        textLabel = Label(self.mainView, text=title, font=('Calibri', 20))
        testButton = Button(self.mainView, text='confirm', command=self.confrim)
        # button placement, x=0 y=0-> top left, x=1,y=1 -> bottom right
        testButton.place(relx=0.90, rely=0.95, anchor='center')
        textLabel.place(relx=0.1, rely=0.95, anchor='center')
        textLabel.pack()
    
    def drawImage(self, *args):
        test = ImageTk.PhotoImage(Image.open(self.imageSet[0]))
        imageLabel = Label(self.mainView, image=test, background='blue')
        imageLabel.place(relx=0.5, rely=0.5, width=100, height=100, anchor='center')
        

    def browseFolder(self, *args):
        fileName = filedialog.askdirectory()
        self.folderPath.set(fileName)
        print(f'\nUser Selected Folder: {fileName}')
        for root, dirs, files in os.walk(fileName, topdown=False):
            for name in files:
                if name.__contains__('.png'):
                    self.imageSet.append(f'{root}/{name}')
        print(self.imageSet)
        self.drawImage()

    
    def confrim(self, *args):
        print('confirmed!')

            
# call the class to draw an empty window on execution of script
main = Tk()
createWindow(main)
main.mainloop()
