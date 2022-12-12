import pyttsx3
q=open("story.txt","r")
z=q.read()
engine = pyttsx3.init()
engine.say(z)
engine.runAndWait()


