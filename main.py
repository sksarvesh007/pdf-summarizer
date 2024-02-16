# importing required modules
import PyPDF2
from transformers import pipeline
summarizer = pipeline("summarization")

pdfFileObj = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
print("enter the page which you want the summary of :")
pagenum = int(input())
pageObj = pdfReader.pages[pagenum]
summary = summarizer(pageObj.extract_text())
print(summary)
pdfFileObj.close()
