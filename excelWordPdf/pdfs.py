# pdfs are binary files

#! A LOT OF METHODS USED IN VIDEO ARE DEPRECATED, FOLLOW PYTHON ERRORS TO FIND NEW METHODS
# cant extract media from pdfs, some pdfs may not be readable with this import but its the best we have
import PyPDF2 #using the excelenv environment
import os

os.chdir('/home/reece/PracticeFiles')

pdfFile = open('meetingminutes1.pdf', 'rb') #rb = read binary
reader = PyPDF2.PdfReader(pdfFile)
len(reader.pages) #number of pages in pdf
page = reader.pages[0] #returns page object
print(page.extract_text()) #extracts text from page object

#! this is deprecated, find a new way to do this
# for pageNum in range(reader.pages):
#     print(reader.pages(pageNum).extractText()) #extracts text from all pages

# combine pdfs
pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

# create 2 readers
reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)

# create writer
writer = PyPDF2.PdfFileWriter() #empty pdf file
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)  # add page to writer

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)  # add page to writer

outputFile = open('combinedminutes.pdf', 'wb') #wb = write binary
writer.write(outputFile)
outputFile.close() #good practice to close files
