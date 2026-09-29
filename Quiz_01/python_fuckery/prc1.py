import PyPDF2
import pyttsx3

print ("hello\n")
speaker = pyttsx3.init()
readpdf = PyPDF2.PdfReader(open('Research.pdf','rb'))

for pagenumber in range(len(readpdf.pages)):
    page = readpdf.pages[pagenumber]
    text = page.extract_text()
    speaker.save_to_file(text,'Research.mp3')
    speaker.runAndWait()

speaker.stop()