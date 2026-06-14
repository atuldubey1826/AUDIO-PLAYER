import tkinter as tk
import os,sys
import pygame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

pygame.mixer.init()
songs = []
a = os.listdir(r"D:\SONG FOR MUSIC PLAYER")
for i in a:
    songs.append(i)
print(songs)

class AudioPlayer:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title('Audio Player')
        self.root.geometry('500x300')

        self.label = tk.Label(self.root,text= "WECOME TO AKD AUDIO PLAYER: ",font=('Linotype',17))
        self.label.pack(padx= 10,pady= 10)

        self.songlist = tk.Listbox(height=4,width= 82)
        for i in a:
            self.songlist.insert(tk.END, i)
        self.songlist.bind('<Double-Button-1>',self.playsong)
        self.songlist.bind('<Return>',self.playsong)
        self.songlist.pack(anchor= 'nw')

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0,weight= 1)
        self.buttonframe.columnconfigure(1,weight= 1)
        self.buttonframe.columnconfigure(2,weight= 1)

        self.button1 = tk.Button(self.buttonframe,text='RESUME',font=('Arial',16),command= self.unpause)
        self.button1.grid(row=0,column=0,sticky= tk.W + tk.E)
        self.root.bind('<space>',self.unpause)

        self.button2 = tk.Button(self.buttonframe,text='PAUSE',font=('Arial',16),command= self.pausesong)
        self.button2.grid(row=0,column=1,sticky= tk.W + tk.E)
        self.root.bind('p',self.pausesong)

        self.button3 = tk.Button(self.buttonframe,text='REWIND',font=('Arial',16),command= self.rewindsong)
        self.button3.grid(row=0,column=2,sticky= tk.W + tk.E)
        self.root.bind('r',self.rewindsong)

        self.button4 = tk.Button(self.buttonframe,text='Half Vol',font=('Arial',16),command= self.halfvolume)
        self.button4.grid(row=1,column=0,sticky= tk.W + tk.E)
        self.root.bind('h',self.halfvolume)

        self.button5 = tk.Button(self.buttonframe,text='Full Vol',font=('Arial',16),command= self.fullvolume)
        self.button5.grid(row=1,column=1,sticky= tk.W + tk.E)
        self.root.bind('f',self.fullvolume)

        self.button6 = tk.Button(self.buttonframe,text='CLOSE',font=('Arial',16),command= self.shutit)
        self.button6.grid(row=1,column=2,sticky= tk.W + tk.E)
        self.root.bind('<Escape>',self.shutit)

        self.buttonframe.pack(fill='x',side= tk.BOTTOM)

        
        self.root.mainloop()

    def playsong(self , event = None):
        selection = self.songlist.curselection()
        
        
        if not selection:
            return
        
            
        selected_song = self.songlist.get(selection[0])
        full_path = os.path.join(r"D:\SONG FOR MUSIC PLAYER" , selected_song)    
        pygame.mixer.music.load(full_path)
        pygame.mixer.music.play()

    def unpause(self,event = None):
        pygame.mixer.music.unpause()

    def pausesong(self,event = None):
        pygame.mixer.music.pause()

    def rewindsong(self,event = None):
        pygame.mixer.music.rewind()

    def halfvolume(self,event = None):
        pygame.mixer.music.set_volume(0.5)

    def fullvolume(self,event = None):
        pygame.mixer.music.set_volume(1)

    def shutit(self,event = None):
        sys.exit()
        


AudioPlayer()