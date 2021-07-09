import pyttsx3
import PyPDF2

pageNum = int(input("Enter a page num: "))
book = open('book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)  

friend = pyttsx3.init()
page = pdfReader.getPage(pageNum)
text = page.extractText() 

friend.say(text)
friend.runAndWait()