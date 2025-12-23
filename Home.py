#Completed✅
import MergePdf, ReadPdf, Decryptpdf ,Encryptpdf,Createpdf,WritePDF,Splitpdf,Extracttext,ExtractTextandmerge,rotate,Remove_page
print("Welcome !")
print("This is a simple pdf app")
print("Pick a option what do you want to do ?:-")
print("\t1. Create a pdf file")
print("\t2. Extract text from one or more pdf and save it in one")
print("\t3. Read a pdf file")
print("\t4. Write a pdf file ")
print("\t5. Merge pdf files")
print("\t6. Split pdf files")
print("\t7. Encrypt pdf file")
print("\t8. Decrypt pdf file")
print("\t9. Extract text from pdf and save it in text file ")
print("\t10. Rotate pdf file/or pages")
print("\t11. Remove pages from pdf file")
print("\t12. exit()")
print()
try:
    choice=input("Enter your choice:- ")
    match choice:
        case "1":
            print("You have chosen to create a pdf file ")
            Createpdf.generate_pdf()#Completed but some bugs need to fix 
        case "2":
            print("You have chosen to extract text from one or more pdf and save it in one")
            ExtractTextandmerge.Extractandmerge() #Completed ✅
        case "3":
            print("You have chosen to read a pdf file")
            ReadPdf.readpdf() #Completed✅
        case "4":
            print("You have chosen to write a pdf file form the text file and add it to existing pdf file")
            WritePDF.writepdf()#Completed but some bugs need to fix 
        case "5":
            print("You have chosen to merge pdf files")
            MergePdf.MergePdf()  #Completed✅
        case "6":
            print("You have chosen to split pdf files")
            Splitpdf.splitpdf()  #Completed✅
        case "7":
            print("You have chosen to encrypt pdf file")
            Encryptpdf.Encryptpdf()#Completed✅
        case "8":
            print("You have chosen to decrypt pdf file")
            Decryptpdf.Decryptpdf()#Completed✅
        case "9":
            print("Extract text from pdf and create a text file from that text")
            Extracttext.extracttext()#Completed✅
        case "10":
            print("Rotate Pdf / pages of pdf  ")
            rotate.rotatepdf()
        case "11":
            print("Remove pages of pdf  ")
            Remove_page.remove_page()
        case "12":
            print("Thankyou for using this app")
except Exception as e:
    print("Invalid choice")



