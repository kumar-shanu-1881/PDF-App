import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def Extractandmerge():
    # 1. Ask for text file
    text_file = input("Enter the text file name or path (with extension): ").strip()
    if not text_file.endswith(".txt"):
        text_file += ".txt"
    if not os.path.exists(text_file):
        print(f"❌ Text file '{text_file}' not found.")
        return

    with open(text_file, "r", encoding="utf-8") as f:
        text_data = f.read().strip()
    if not text_data:
        print("❌ The text file is empty.")
        return

    # 2. Ask for existing PDF file
    pdf_path = input("Enter the existing PDF file name or path: ").strip()
    if not pdf_path.endswith(".pdf"):
        pdf_path += ".pdf"
    if not os.path.exists(pdf_path):
        print(f"❌ PDF file '{pdf_path}' not found.")
        return

    # 3. Ask for output PDF name
    new_pdf_name = input("Enter a name for the new merged PDF: ").strip()
    if not new_pdf_name:
        print("❌ New PDF name not provided.")
        return
    if not new_pdf_name.endswith(".pdf"):
        new_pdf_name += ".pdf"
    if os.path.exists(new_pdf_name):
        overwrite = input(f"⚠️ '{new_pdf_name}' already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            print("❌ Operation cancelled.")
            return

    # 4. Ask for font size
    try:
        fontsize = int(input("Enter font size (default 12): "))
    except ValueError:
        fontsize = 12

    # 5. Create temporary PDF from text file
    temp_pdf = "temp_text.pdf"
    c = canvas.Canvas(temp_pdf, pagesize=A4)
    width, height = A4
    y = height - 50
    textobj = c.beginText(50, y)
    textobj.setFont("Helvetica", fontsize)

    for line in text_data.splitlines():
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

    # 6. Merge PDFs
    writer = PdfWriter()

    # Add existing PDF pages
    existing_reader = PdfReader(pdf_path)
    for page in existing_reader.pages:
        writer.add_page(page)

    # Add new text pages
    new_reader = PdfReader(temp_pdf)
    for page in new_reader.pages:
        writer.add_page(page)

    # Save merged PDF under the new name
    with open(new_pdf_name, "wb") as f:
        writer.write(f)

    os.remove(temp_pdf)
    print(f"✅ Merged PDF saved successfully as '{new_pdf_name}'")

if __name__ == "__main__":
    Extractandmerge()
