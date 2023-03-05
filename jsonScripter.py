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
        self.imageIndex = 0
        self.mainView = main
        self.drawMain()
        self.folderPath = StringVar()
        
    def drawMain(self, *args):
        title = "Annotation Scripter!"
        textLabel = Label(self.mainView, text=title, font=('Calibri', 20))
        testButton = Button(self.mainView, text='confirm', command=self.confrim)
        # button placement, x=0 y=0-> top left, x=1,y=1 -> bottom right
        testButton.place(relx=0.90, rely=0.95, anchor='center')
        textLabel.place(relx=0.1, rely=0.95, anchor='center')
        textLabel.pack()
        # this button calls the browseFolder plugin
        browseButton = Button(self.mainView, text='Browse Files', command=self.browseFolder)
        browseButton.place(relx=0.12, rely=0.95, anchor='center')
        prevButton = Button(self.mainView, text='prev', command=self.prev)
        prevButton.place(relx=0.45, rely=0.95, anchor='center')
        nextButton = Button(self.mainView, text='next', command=self.next)
        nextButton.place(relx=0.55, rely=0.95, anchor='center')
    

    def prev(self, *args):
        if self.imageIndex > 0:
            self.imageIndex -= 1
        elif self.imageIndex == 0:
            self.imageIndex = self.imageMaxCount
        else:
            self.imageIndex = 0
        self.imageLabel.config(image=self.image[self.imageIndex])
        self.imageLabel.image = self.image[self.imageIndex]


    def next(self, *args):
        if self.imageIndex < self.imageMaxCount-1:
            self.imageIndex += 1
        elif self.imageIndex == self.imageMaxCount-1:
            self.imageIndex = 0
        else:
            self.imageIndex = 0
        self.imageLabel.config(image=self.image[self.imageIndex])
        self.imageLabel.image = self.image[self.imageIndex]


    def imageWindow(self, *args):
        # create the frame for the image to sit in
        self.imageFrame = Frame(self.mainView, width=300, height=300)
        self.imageFrame.place(relx=0.5, rely=0.5, anchor='center')
        # load the image
        self.image = []
        for i in range(len(self.imagePath)):
            imageOpen = Image.open(self.imagePath[i])
            self.image.append(ImageTk.PhotoImage(imageOpen.resize((500,500))))
        self.drawImage()

    
    def drawImage(self, *args):
        self.imageLabel = Label(self.imageFrame, image=self.image[0])#, background='blue')
        self.imageLabel.image = self.image[0]
        self.imageLabel.place(relx=0.5, rely=0.5, anchor='center')
        self.imageLabel.pack()
        

    def browseFolder(self, *args):
        # Ask user for file path, then grab all ".png"/".jpg" extensions and place into an array
        fileName = filedialog.askdirectory()
        self.folderPath.set(fileName)
        self.imageName = []
        self.imagePath = []
        print(f'\nUser Selected Folder: {fileName}')
        for root, dirs, files in os.walk(fileName, topdown=False):
            for name in files:
                if name.__contains__('.png') or name.__contains__('.jpg'):
                    self.imagePath.append(f'{root}/{name}')
                    self.imageName.append(name)
        self.imageMaxCount = len(self.imagePath)
        self.imageIndex = 0
        self.imageWindow()

    
    def confrim(self, *args):
        print('confirmed!')

            
# call the class to draw an empty window on execution of script
main = Tk()
createWindow(main)
main.mainloop()
