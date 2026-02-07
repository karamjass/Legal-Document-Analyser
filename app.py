import os
print(os.listdir())

from ocr_utilits import extract_text
from summarize import generate_summary

image_path = "test_image.jpg"

print("Extracting text from image...")
text = extract_text(image_path)

print("\nOriginal Text:\n")
print(text)

print("\nGenerating Summary...\n")
summary = generate_summary(text)

print("Summary:\n")
print(summary)
