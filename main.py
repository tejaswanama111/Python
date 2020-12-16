import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

for num in range(0, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()

    """ RATE"""
rate = player.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
player.setProperty('rate', 200)     # setting up new voice rate


"""VOLUME"""
volume = player.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
player.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = player.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
player.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

player.say(text)
player.runAndWait()