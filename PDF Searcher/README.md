PDF Keyword Search and Move Script
This Python script searches all PDF files in the current directory for specified keywords, logs the results to a text file (results.txt), and moves the processed PDFs to a folder named complete. It’s designed to help automate keyword searches across multiple PDFs and organize the files afterward.
Features
Searches all .pdf files in the current directory.
Reads keywords from a keywords.txt file (one keyword per line).
Outputs results to results.txt, including the PDF name, keywords found, and page numbers.
Moves processed PDFs to a complete folder.
Optional: Highlights keywords in a new PDF (commented out by default).
Prerequisites
Python 3.x: Ensure Python is installed (download from python.org).
Required Libraries: Install these via pip:
bash
pip install pdfplumber PyMuPDF
pdfplumber: Extracts text from PDFs for searching.
PyMuPDF (imported as fitz): Handles PDF manipulation (e.g., highlighting).
Setup
Clone or Download: Place the script (pdf_search.py) in a folder where your PDFs are located.
Install Dependencies: Run the following command in your terminal/command prompt:
bash
pip install pdfplumber PyMuPDF
Create keywords.txt:
Open a text editor (e.g., Notepad, VS Code).
Add one keyword per line, e.g.:
complete
approved
accepted
Save as keywords.txt in the same folder as the script.
Usage
Prepare PDFs: Place all .pdf files you want to process in the same folder as the script.
Run the Script:
Open a terminal/command prompt in the folder.
Execute:
bash
python pdf_search.py
Check Output:
Console: Shows basic progress (e.g., "Processing complete").
results.txt: Contains detailed results (e.g., keywords found and page numbers).
complete folder: Processed PDFs are moved here.
Example results.txt
Search Results - 2 PDF(s) Processed
==================================================

PDF: doc1.pdf
'complete' not found in the PDF
'approved' found on page(s): 2
'accepted' found on page(s): 3
--------------------------------------------------
PDF: doc2.pdf
'complete' found on page(s): 1
'approved' not found in the PDF
'accepted' not found in the PDF
--------------------------------------------------
Optional Highlighting
To generate highlighted versions of the PDFs:
Uncomment the following lines in the script:
python
# highlighted_pdf = os.path.join(output_folder, f"highlighted_{pdf_file}")
# highlight_keywords(pdf_path, keywords, highlighted_pdf)
Rerun the script. Highlighted PDFs (e.g., highlighted_doc1.pdf) will appear in the complete folder.
Notes
Case Insensitivity: Searches are case-insensitive (e.g., "Approved" matches "approved").
Warnings: You might see a CropBox missing warning in the console. This is harmless and suppressed in the script.
Overwrites: results.txt is overwritten each run. To append instead, change "w" to "a" in the script’s open() calls.
Errors: If keywords.txt is missing or empty, or if an error occurs, details are written to results.txt.
Troubleshooting
Error: "Module not found": Ensure pdfplumber and PyMuPDF are installed.
No PDFs processed: Check that .pdf files are in the same folder as the script.
Highlighting fails: Update PyMuPDF with pip install --upgrade PyMuPDF if you encounter issues.
License
This script is provided as-is for personal use. Feel free to modify it to suit your needs!
How to Use It
Copy the text above into a file named README.md.
Place it in the same folder as pdf_search.py.
Open it in a Markdown viewer (e.g., VS Code, GitHub) or read it as plain text.
This README should cover everything a user (including future you!) needs to get started. Let me know if you’d like to add more details or adjust anything!