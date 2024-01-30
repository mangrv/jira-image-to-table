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
