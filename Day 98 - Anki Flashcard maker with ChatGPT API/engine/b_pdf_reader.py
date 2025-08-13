'''
pdf_reader.py

Module that contains function used to process .pdf files
'''
import os
import pymupdf

def read_pdf(file_path):
    ''' Read .pdf file by file path and return formatted string of it'''

    if os.path.isfile(file_path):
        with pymupdf.open(file_path) as doc:
            text = chr(12).join([page.get_text() for page in doc])
    else:
        text = False
    return text

