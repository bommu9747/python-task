u=open("story.txt","r")
print(u.readline())
x=u.read()

import win32com.client as wincom
import time
speak = wincom.Dispatch("SAPI.SpVoice")
text = "Python text-to-speech test. using win32com.client"
time.sleep(.5)
speak.Speak(x)

