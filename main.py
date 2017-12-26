import open as opn
from time import ctime
import time
from tkinter import *
from tkinter import ttk
import speech_recognition as sr
from pygame import mixer
import pyperclip
import threading
import translation as trans
import operation as pm
import dictionary_tref as dct
import win32com.client as wincl
import webbrowser
'''
sapi initialisation
'''

speak = wincl.Dispatch("SAPI.SpVoice")
'''
code start here 
'''

'''
speech 
reconginizer
is 
here'''

r = sr.Recognizer()
r.pause_threshold = 0.5
r.energy_threshold = 4500
with sr.Microphone() as source:#use of microphone
    print('speak')# print speak
    print('listening')#print listening
    audio = r.listen(source, timeout=3)#audio listining
try:
    print('recognizing')
    print("You said " + r.recognize_google(audio))#conversion
    input = r.recognize_google(audio)
    #input=input('Enter your command')
    input = input.lower()
    if input.find('open') != -1:
        opn.fil_search(input)
    if input.find('play') != -1 or input.find('play') != -1:
        pm.op_music(input)
    if input.find('translate') != -1:
        trans.translate(input)
    if input.find('define') != -1:
        dct.dict(input)
    if input.find('time') != -1:
        print(ctime())
        speak.Speak(ctime())


except sr.UnknownValueError:
    print("Could not understand")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
