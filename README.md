OCR Text Extractor
==================

This Python script performs Optical Character Recognition (OCR) on an image file to extract text. It uses `pandas`, `PIL` (Python Imaging Library), and `pytesseract`, a Python wrapper for Tesseract-OCR.

Description
-----------

The script loads an image file, uses Tesseract OCR to extract text from the image, and then processes the text to split it into clean, readable lines. This can be useful for reading text from screenshots, scanned documents, or any images containing textual information.

Installation
------------

Before running the script, ensure that Python 3 and the necessary packages are installed on your system. Follow these steps to set up the environment:

### Prerequisites

*   Python 3
*   pip (or pip3 for Python 3)

### Step 1: Install Required Python Packages

1.  **Install Pandas:**
    
        pip3 install pandas
        # or, if using Python 2 (not recommended)
        pip install pandas
    
2.  **Install Pillow:**
    
        pip3 install Pillow
        # or, if using Python 2
        pip install Pillow
    
3.  **Install pytesseract:**
    
        pip3 install pytesseract
        # or, if using Python 2
        pip install pytesseract
    

### Step 2: Install Tesseract-OCR

*   **macOS:**
    
    If you are on macOS, you can install Tesseract using Homebrew:
    
        brew install tesseract
    
*   **Other Operating Systems:**
    
    For other operating systems, please visit the [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract) for installation instructions.
    

Usage
-----

1.  Place the image file you want to process in an accessible directory.
2.  Update the `img_path` in the script to point to your image file.
3.  Run the script using Python:
    
        python3 ocr_text_extractor.py
        # or, if using Python 2
        python ocr_text_extractor.py
    
4.  The script will display the extracted text in the console.

Code
----

    import pandas as pd
    from PIL import Image
    import pytesseract
    
    # Load the image from file
    img_path = '/path/to/your/image.png'
    img = Image.open(img_path)
    
    # Use tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    # Clean the text and split into lines
    lines = text.split('\n')
    lines_clean = [line.strip() for line in lines if line.strip() != '']
    
    # Display the extracted text to verify the OCR output
    print(lines_clean)

Replace `/path/to/your/image.png` with the actual path to your image file.