# PDF-App

A simple terminal-based PDF utility application written in Python.  
It offers a set of functionalities to create, read, split, merge, encrypt, decrypt, and extract text from PDF files.

## 📄 Features  

- Create a new PDF file.  
- Read / view existing PDF files.  
- Split a PDF into multiple PDFs.  
- Merge multiple PDFs into a single PDF.  
- Extract text from PDF and save as a text file.  
- Encrypt PDF files.  
- Decrypt encrypted PDF files.  

## 🛠️ Prerequisites  

- Python 3.x installed on your system.  
- (Any additional dependencies you use — `PyPDF2`, `Reportlib`)  

## 🚀 Installation & Setup  

1. Clone the repository  
   ```bash
   git clone https://github.com/kumar-shanu-1881/PDF-App.git
   ```  
2. Navigate into the project directory  
   ```bash
   cd PDF-App
   ```  
3. (Optional) Create a virtual environment  
   ```bash
   python3 -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```  
4. Install dependencies (if any)  
   ```bash
   pip install -r requirements.txt
   ```  

## 🎯 Usage  

Each functionality is implemented in a separate Python script. For example:  
- To create a PDF: `python Createpdf.py`  
- To read a PDF: `python ReadPdf.py`  
- To split a PDF: `python Splitpdf.py`  
- To merge PDFs: `python MergePdf.py`  
- To extract text: `python ExtractTextandmerge.py` / `python Extracttext.py`  
- To encrypt a PDF: `python Encryptpdf.py`  
- To decrypt a PDF: `python Decryptpdf.py`  

> Adapt the commands above depending on your environment/OS.  

## ⚠️ Limitations / Known Issues  

- This is a terminal-based application — no GUI interface is provided.  
- For large PDFs or many files, performance might be limited.  
- (Add other limitations or known issues here if any.)  

## 📊 Project Structure  

```
/PDF-App  
|-- Createpdf.py  
|-- ReadPdf.py  
|-- Splitpdf.py  
|-- MergePdf.py  
|-- Extracttext.py  
|-- ExtractTextandmerge.py  
|-- Encryptpdf.py  
|-- Decryptpdf.py  
|-- README.md   <-- (this file)  
|-- … other scripts …  
```  

## 🤝 Contributing  

Contributions are welcome! To contribute:  
1. Fork the repository  
2. Create a branch for your feature or bugfix  
3. Make changes and test thoroughly  
4. Submit a pull request  

Please ensure new code is clean, commented (if needed), and doesn’t break existing functionality.  

## 📝 License  



## 🙋 Author / Maintainer  

- Repository owner: `kumar-shanu-1881` on GitHub  
