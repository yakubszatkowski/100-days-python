'''
pdf_reader.py

Module that contains function used to process .pdf files
'''
import os
import pymupdf

def read_pdf(file_path):
    ''' Read .pdf file by file path and return formatted string of it'''
    document = []
    if os.path.isfile(file_path):
        with pymupdf.open(file_path) as doc:
            for page in doc:
                document.append(page.get_text())
    else:
        document = False
    return document
