# completed
from pypdf import PdfWriter
def MergePdf():
    try:
        num=int(input("Enter the number of pdf files you want to merge: "))

        pdfs=[]

            
        for i in range(num):
            file=input(f"Enter the path of the pdf file {i+1}: ")
            file= file.replace("\\", "/")  # makes it safe for Python
            pdfs.append(file)



        filename=input("Enter the new pdf file name : ")
        if filename is None:
            filename="newPdf.pdf"
        elif not filename.lower().endswith(".pdf"):
            filename += ".pdf"

        try:
            merger = PdfWriter()
            for pdf in pdfs:
                merger.append(pdf)
            merger.write(filename)
            merger.close()
            print("Pdf files merged successfully")
        except Exception:
            print("Error merging pdf files")
            return

    except Exception as e:
        print(e)

if __name__=="__main__":
    MergePdf()