
### Steps to Use
1. **Create `keywords.txt`**:
   - Add your keywords, one per line (e.g., "complete," "approved," "accepted").
   - Save it in the same folder as the script.

2. **Place PDFs**:
   - Put all `.pdf` files in the same folder as the script.

3. **Run the Script**:
   - Save the script as `pdf_search.py`.
   - Run it:
     ```bash
     python pdf_search.py
     ```
   - Console output will be minimal (e.g., "Processing complete. Results written to 'results.txt'.").
   - Check `results.txt` for the detailed output.

4. **Highlighting (Optional)**:
   - Uncomment the `highlight_keywords` section if you want highlighted versions in the `complete` folder.

### Notes
- **Overwriting**: Each run overwrites `results.txt`. If you want to append instead, change `"w"` to `"a"` in the `open(results_file, "w")` lines.
- **Error Handling**: Errors (e.g., missing `keywords.txt`) are written to `results.txt` for easy reference.
- **File Movement**: PDFs are still moved to `complete` after processing.

This should give you a clean, file-based output as requested. Let me know if you’d like the format tweaked or any other adjustments! How’s this looking for you?