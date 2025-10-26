# completed
import os 
from pypdf import PdfReader

def readpdf():
    try:
        pdf=input("Enter the path of the pdf file :- ")
        if not os.path.exists(pdf):
            print("File path not found! Please check the path ")
        pdf=pdf.replace("\\","/")
        reader=PdfReader(pdf)
    
    
        for page in reader.pages:
            if not page.extract_text():
                print("Sorry!\nWe are unable to read the pdf file.")
                return
            else:
                print(page.extract_text())
    except Exception as e:
        print(e)

if __name__=="__main__":
    readpdf()
