import pyttsx3
a=open("task3.txt","r")
e=a.read()
engine = pyttsx3.init()
engine.say(e)
engine.runAndWait()


