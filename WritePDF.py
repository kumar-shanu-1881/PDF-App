# not tested or not completed 
import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def writepdf():
    # 1. Ask for text file 
    file = input("Enter the text file name or path (with extension): ").strip()
    if not file:
        print("❌ File name or path not given!")
        return
    
    if not file.endswith('.txt'):
        file += '.txt'
    
    if not os.path.exists(file):
        print(f"❌ File '{file}' does not exist.")
        return
    
    with open(file, "r") as f:
        data = f.read()
    
    if not data.strip():
        print("❌ The text file is empty.")
        return

    # 2. Ask for PDF file path
    pdf_path = input("Enter the PDF file path (existing or new): ").strip()
    if not pdf_path.endswith(".pdf"):
        pdf_path += ".pdf"
    
    # 3. Ask if append or overwrite
    if os.path.exists(file):
        mode = input("Do you want to append to the PDF? (y/n): ").strip().lower()
    append = (mode == "y")

    # 4. Ask for font size
    try:
        fontsize = int(input("Enter font size (default 12): "))
    except ValueError:
        fontsize = 12

    # 5. Create a temporary PDF with the text content
    temp_file = "temp_text.pdf"
    c = canvas.Canvas(temp_file, pagesize=A4)
    width, height = A4

    y = height - 50
    textobj = c.beginText(50, y)
    textobj.setFont("Helvetica", fontsize)

    for line in data.splitlines():
        if y <= 50:  # bottom margin reached → new page
            c.drawText(textobj)
            c.showPage()
            textobj = c.beginText(50, height - 50)
            textobj.setFont("Helvetica", fontsize)
            y = height - 50
        textobj.textLine(line)
        y -= fontsize + 2

    c.drawText(textobj)
    c.save()

    writer = PdfWriter()

    if append and os.path.exists(pdf_path):
        # Copy existing PDF pages first
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    # Add the new text page(s)
    reader_temp = PdfReader(temp_file)
    for page in reader_temp.pages:
        writer.add_page(page)

    # Save final output
    with open(pdf_path, "wb") as f:
        writer.write(f)

    # Cleanup temp file
    os.remove(temp_file)

    print(f"✅ PDF saved successfully as '{pdf_path}'")

if __name__ == "__main__":
    writepdf()
