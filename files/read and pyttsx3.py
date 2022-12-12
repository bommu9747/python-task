u=open("user.txt","r")
print(u.read())
x=u.read()
import pyttsx3
engine = pyttsx3.init()
engine.say(x)
engine.runAndWait()