# completed
from pypdf import PdfReader, PdfWriter

def Encryptpdf():
    try:
        file=input("Enter the path of the pdf file:-")
        file=file.replace("\\","/")
        password=input("Enter the password of the file :- ")
        reader = PdfReader(file)
        writer = PdfWriter(clone_from=reader)

        # Add a password to the new PDF
        writer.encrypt(password, algorithm="AES-256")

        name=input("Enter the name of pdf file you want to save :- ")
        if name is None:
            name="encrypted-pdf.pdf"
        # Save the new PDF to a file
        with open(name, "wb") as f:
            writer.write(f)
    except Exception as e:
        print(e)
        
if __name__=="__main__":
    Encryptpdf()