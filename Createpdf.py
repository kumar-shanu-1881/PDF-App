# module completed
import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
def generate_pdf():
    """
#     A simple script to generate a PDF file with custom text input.

#     Features:
#     - User chooses a filename (adds .pdf if missing).
#     - Warns if the file already exists.
#     - Accepts multi-line text input (press Enter twice to end).
#     - Allows custom font size (defaults to 12 if invalid).
#     - Handles page breaking when content reaches the bottom margin.
#     - Saves the final PDF file.
#     """

#     # Ask user for the file name
    name=input("Enter the name of pdf file you want to save :- ").strip()

    #     # If no name is entered, use default
    if not name:
        name = "new.pdf"

#     # Ensure the file name ends with ".pdf"
    if not name.endswith(".pdf"):
        name+=".pdf"

    # Checks if file already exists or not
    if os.path.exists(name):
        print(f"Warning: '{name}' already exists and will be replaced.")

        #     # Ask for text input (multi-line support)
    print("\nEnter a text you want on write on the pdf file :- ")
    print("You can enter multiple lines (Press Enter twice to end input)")
    lines=[]
    while True:
        line=input()
        if line:# If line is not empty, add to list
            lines.append(line)
        else:
            break

#     # If no text entered, exit
    if not lines:
        print("No text entered. PDF not created.")
        return
    
    #     # Ask for font size (with error handling)
    try:
        fontsize = int(input("Enter font size (default 12): ") or 12)
    except ValueError:
        print("Invalid font size. Defaulting to 12.")
        fontsize = 12


    # Create a PDF file
    c=canvas.Canvas(name)# Create a brand-new PDF file
    c.setTitle("Generated PDF")
    c.setAuthor("Python script by kumar")

    y = 780  # Current vertical position
    textobj=c.beginText(65,y)
    
    textobj.setFont("Helvetica", fontsize)


    for line in lines:
        wrapped_lines=simpleSplit(line, "Helvetica", fontsize, 435)
        for w in wrapped_lines:
            if y <= 50:  # Bottom margin reached → new page
                c.drawText(textobj)
                c.showPage()
                textobj = c.beginText(65, 780)
                textobj.setFont("Helvetica", 12)
                y = 780
            clean_line = w.replace("■", "").replace("o", "")
            textobj.textLine(clean_line.strip("\n"))
            y -= fontsize+2  # Move down for next line

    c.drawText(textobj)
    try:
        c.save()  # Finish and save
        print("PDF file created successfully with the name :- ",name)
    except Exception as e:
        print(f"Error saving PDF: {e}")

if __name__=="__main__":
    generate_pdf()








#     if not name:
#         name = "new.pdf"


#     if not name.endswith(".pdf"):
#         name += ".pdf"

#     # Check if file already exists
#     if os.path.exists(name):
#         print(f"Warning: '{name}' already exists and will be replaced.")


#     print("\nEnter a text you want on write on the pdf file :- ")
#     print("You can enter multiple lines (Press Enter twice to end input)")
#     lines = []
#     while True:
#         line = input()
#         if line:   
#             lines.append(line)
#         else:      # Empty line means end of input
#             break


#     if not lines:
#         print("No text entered. PDF not created.")
#         return


#     try:
#         fontsize = int(input("Enter font size (default 12): ") or 12)
#     except ValueError:
#         print("Invalid font size. Defaulting to 12.")
#         fontsize = 12


#     c = canvas.Canvas(name)   # Creates a new PDF file
#     y = 780                   # Starting vertical position (top of page)
#     textobj = c.beginText(65, y)  # Start text at (x=65, y=780)
#     textobj.setFont("Helvetica", fontsize)

#     # Write each line into the PDF
#     for line in lines:
#         if y <= 50:  # If bottom margin is reached → create a new page
#             c.drawText(textobj)           # Write current text to page
#             c.showPage()                  # Start a new page
#             textobj = c.beginText(65, 780)  # Reset text object to top of page
#             textobj.setFont("Helvetica", 12)
#             y = 780

#         textobj.textLine(line)     # Write one line of text
#         y -= fontsize + 2          # Move down for the next line

#     # Draw the final text and save the PDF
#     c.drawText(textobj)
#     c.save()
#     print("PDF file created successfully with the name :- ", name)


# # Run the script if executed directly
# if __name__ == "__main__":
#     generate_pdf()
