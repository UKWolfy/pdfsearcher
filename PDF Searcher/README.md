markdown
# PDF Keyword Search and Move Script

This Python script searches all PDF files in the current directory for specified keywords, logs the results to `results.txt`, and moves the processed PDFs to a `complete` folder. Ideal for automating keyword searches across multiple PDFs and organizing files.

## Features
- Processes all `.pdf` files in the current directory.
- Reads keywords from `keywords.txt` (one per line).
- Outputs results to `results.txt` with PDF names, keywords, and page numbers.
- Moves processed PDFs to a `complete` folder.
- Optional: Highlights keywords in new PDFs (disabled by default).

## Prerequisites
- **Python 3.x**: [Download here](https://www.python.org/).
- **Required Libraries**:
  - `pdfplumber`: For text extraction.
  - `PyMuPDF` (aka `fitz`): For PDF manipulation (e.g., highlighting).
  - Install them with:
    ```bash
    pip install pdfplumber PyMuPDF
    ```

## Setup
1. **Clone or Download**: Place `pdf_search.py` in a folder with your PDFs.
2. **Install Dependencies**:
   ```bash
   pip install pdfplumber PyMuPDF
Create keywords.txt:
Add one keyword per line, e.g.:
complete
approved
accepted
Save as keywords.txt in the same folder.
Usage
Add PDFs: Place .pdf files in the script’s folder.
Run the Script:
bash
python pdf_search.py
View Results:
Console: Shows progress.
results.txt: Detailed results.
complete folder: Processed PDFs.
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
To enable highlighting:
Uncomment these lines in pdf_search.py:
python
# highlighted_pdf = os.path.join(output_folder, f"highlighted_{pdf_file}")
# highlight_keywords(pdf_path, keywords, highlighted_pdf)
Rerun the script. Highlighted PDFs (e.g., highlighted_doc1.pdf) will appear in complete.
Notes
Case Insensitive: Matches "Approved" and "approved".
Warnings: CropBox missing warnings are suppressed but harmless.
Overwrites: results.txt is overwritten each run. Use "a" instead of "w" in the script to append.
Errors: Missing keywords.txt or other issues are logged to results.txt.
Troubleshooting
"Module not found": Verify pdfplumber and PyMuPDF are installed.
No PDFs processed: Ensure PDFs are in the script’s folder.
Highlighting issues: Update with pip install --upgrade PyMuPDF.
Contributing
Feel free to fork, modify, or submit pull requests!
License
This project is unlicensed (public domain). Use and adapt it freely!
