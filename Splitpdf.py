import os
from pypdf import PdfReader, PdfWriter

def splitpdf():
    try:
        input_path=input("Enter the path of the pdf file ")
        if not os.path.isfile(input_path):
            print("File not found! check the path again")
        input_path=input_path.replace("/","\\")
        
        # Read the pdf 
        reader=PdfReader(input_path)

        # Loop through all pages and save each as a seaprate PDF 
        for i in range(len(reader.pages)):
            page=reader.pages[i]
            writer=PdfWriter()
            writer.add_page(page)

            output_pdf="page_"+str(i+1)+".pdf"

            # write to new pdf
            with open(output_pdf,"wb") as f:
                writer.write(f)

            print("Saved: ",output_pdf)
        print("PDF Splitted successfullly")
    except Exception as e:
        print(e)


if __name__=="__main__":
    splitpdf()
