from pypdf import PdfReader
import os 

def extracttextandmerge():
    try:
        pdf=input("Enter the path of the pdf file :- ")
        if not os.path.exists(pdf):
            print("File path not found! Please check the path ")
        pdf=pdf.replace("/","\\")

        reader=PdfReader(pdf)
        file=input("Enter the name of the file you want to save the extracted text:- ")
        if not file.endswith(".txt"):
            file+=".txt"

        for i in range(len(reader.pages)):
            page=reader.pages[i]

    except Exception as e:
        print(e)

if __name__=="__main__":
    extracttextandmerge()