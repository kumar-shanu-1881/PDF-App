import os 
from pypdf import PdfReader, PdfWriter

def remove_page():
    try:
        pdf=input("Enter the path of the pdf file :- ")
        if not os.path.exists(pdf):
            print("File path not found! Please check the path ")
            
        pdf=pdf.replace("\\","/")
        reader = PdfReader(pdf)
        writer = PdfWriter()

        print("total page count in this pdf is ",len(reader.pages))
        print("Enter the no of pages you want to remove from pdf :\n")

        start=int(input("From page:- "))
        end=int(input("To page:- "))
        remove_pages = range(start, end+1)  

        for i, page in enumerate(reader.pages):
            if i not in remove_pages:
                writer.add_page(page)

                
        name=input("Enter the name you want to save the PDF file as. ")
        if not name:
            name="Rotated.pdf"
        if not name.endswith('.pdf'):
            name+=".pdf"

        
        with open(name, "wb") as f:
            writer.write(f)


    except Exception as e:
        print(e)

if __name__=="__main__":
    remove_page()

