import pyttsx3

engine = pyttsx3.init()

# rate = engine.getProperty('rate')
engine.setProperty('rate', 90)
engine.say("right? write?")

engine.runAndWait()