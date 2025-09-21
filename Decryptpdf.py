# completed
# import find_path_with_name as find
import os
from pypdf import PdfReader, PdfWriter

def Decryptpdf():
    try:
        file=input("Enter the path of the pdf file :- ")

        # file=find.find_file(file)

        file=file.replace("\\","/")
        file = os.path.abspath(file) 
        reader = PdfReader(file)

        password=input("Enter the password you want to save :- ")
        if reader.is_encrypted:
            reader.decrypt(password)

        writer = PdfWriter(clone_from=reader)

        # Save the new PDF to a file
        filename=input("Enter the file name you want to save :- ")
        if filename is None:
            filename="decrypted-pdf.pdf"
        print("Hello")
        with open(file, "wb") as f:
            writer.write(f)
    except Exception as e:
        print(e)

if __name__=="__main__":
    Decryptpdf()