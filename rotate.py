import os
from pypdf import PdfReader, PdfWriter

def  rotate():
    try:
        pdf=input("Enter the path of the pdf file :- ")
        if not os.path.exists(pdf):
            print("File path not found! Please check the path ")
        pdf=pdf.replace("\\","/")
        reader=PdfReader(pdf)
        writer = PdfWriter()
        i=0
        print("total page count in this pdf is ",len(reader.pages))
        nop=int(input("Enter the number of pages you want to rotate (should not to be exceed to the count of pages) : "))
        deg=int(input("\nEnter number of rotation you want to rotate (1 rotation=90 deg) :"))
        for page in reader.pages:
            writer.add_page(page)
            if i<=nop:
                writer.pages[i].rotate(deg*90)
            i+=1
        
        
        name=input("Enter the name you want to save the PDF file as. ")
        if not name.endswith('.pdf'):
            name+=".pdf"


        writer.write(name)
        print("Pdf Rotated Successfully")
    except Exception as e:
        print(e)

if __name__=="__main__":
    rotate()




# reader = PdfReader("example.pdf")
# writer = PdfWriter()

# writer.add_page(reader.pages[0])
# writer.pages[0].rotate(90)

# writer.write("out-page-rotation.pdf")