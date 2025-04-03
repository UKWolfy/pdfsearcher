import os
import shutil
import pdfplumber
import fitz  # PyMuPDF for highlighting

# Define the keyword file, output folder, and results file
keyword_file = "keywords.txt"  # Text file with keywords, one per line
output_folder = "complete"      # Folder to move processed PDFs
results_file = "results.txt"    # File to store search results

# Function to read keywords from a text file
def load_keywords(file_path):
    with open(file_path, "r") as f:
        # Read lines, strip whitespace, and filter out empty lines
        keywords = [line.strip() for line in f if line.strip()]
    if not keywords:
        raise ValueError(f"No keywords found in '{file_path}'")
    return keywords

# Function to search for keywords in a PDF and return results
def search_pdf(pdf_path, keywords):
    results = {keyword: [] for keyword in keywords}
    
    # Open the PDF with pdfplumber for text extraction
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text().lower()  # Case-insensitive search
            for keyword in keywords:
                if keyword.lower() in text:
                    results[keyword].append(page_num)
    
    return results

# Function to highlight keywords (optional)
def highlight_keywords(pdf_path, keywords, output_path):
    doc = fitz.open(pdf_path)
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text").lower()
        for keyword in keywords:
            if keyword.lower() in text:
                # Search for all instances of the keyword on the page
                text_instances = page.search_for(keyword)  # Removed hit_max
                for inst in text_instances:
                    highlight = page.add_highlight_annot(inst)
                    highlight.update()
    
    doc.save(output_path)
    return output_path

# Main execution
try:
    # Load keywords
    keywords = load_keywords(keyword_file)
    
    # Create the 'complete' folder if it doesn’t exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all PDF files in the current directory
    current_dir = os.getcwd()
    pdf_files = [f for f in os.listdir(current_dir) if f.lower().endswith(".pdf")]
    
    if not pdf_files:
        with open(results_file, "w") as f:
            f.write("No PDF files found in the current directory.\n")
        print("No PDF files found. Results written to 'results.txt'.")
    else:
        print(f"Found {len(pdf_files)} PDF file(s) to process. Processing...")
        with open(results_file, "w") as f:
            f.write(f"Search Results - {len(pdf_files)} PDF(s) Processed\n")
            f.write("=" * 50 + "\n\n")
            
            for pdf_file in pdf_files:
                pdf_path = os.path.join(current_dir, pdf_file)
                f.write(f"PDF: {pdf_file}\n")
                
                # Search the PDF
                results = search_pdf(pdf_path, keywords)
                
                # Write results to file
                for keyword, pages in results.items():
                    if pages:
                        f.write(f"'{keyword}' found on page(s): {', '.join(map(str, pages))}\n")
                    else:
                        f.write(f"'{keyword}' not found in the PDF\n")
                
                f.write("-" * 50 + "\n")
                
                # Optionally highlight (uncomment to use)
                # highlighted_pdf = os.path.join(output_folder, f"highlighted_{pdf_file}")
                # highlight_keywords(pdf_path, keywords, highlighted_pdf)
                
                # Move the original PDF to the 'complete' folder
                dest_path = os.path.join(output_folder, pdf_file)
                shutil.move(pdf_path, dest_path)
        
        print(f"Processing complete. Results written to '{results_file}'.")

except FileNotFoundError:
    with open(results_file, "w") as f:
        f.write(f"Error: '{keyword_file}' not found. Please create it with one keyword per line.\n")
    print(f"Error occurred. Details written to '{results_file}'.")
except ValueError as e:
    with open(results_file, "w") as f:
        f.write(f"Error: {e}\n")
    print(f"Error occurred. Details written to '{results_file}'.")
except Exception as e:
    with open(results_file, "w") as f:
        f.write(f"An error occurred: {e}\n")
    print(f"Error occurred. Details written to '{results_file}'.")