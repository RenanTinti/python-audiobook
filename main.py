import pyttsx3
import PyPDF2

book = open('python-audiobook/Book.pdf', 'rb')
reader = PyPDF2.PdfFileReader(book)

pages = reader.numPages
print(pages)

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# Used to read a specific page
page = reader.getPage(0)
text = page.extractText()

engine.setProperty('rate', 200)
engine.say(text)

engine.runAndWait()
