'''
pdf_reader.py

Module that contains function used to process .pdf files
'''

import pymupdf
from collections import Counter 

class PDFConverter():

    def __init__(self, file_path):
        ''' Initialize PDF Converter with file path'''
        self.file_path = file_path


    def read_pdf(self):
        ''' Reads .pdf file by file path and return formatted string of it'''
        with pymupdf.open(self.file_path) as doc:
            return [page.get_text() for page in doc]


    def clean_repetetives(self):
        ''' Cleans .pdf file from footers, headers and other repetitive sentences'''
        document_pages = self.read_pdf() 
        pages_count = len(document_pages)

        document_text = '\n'.join(document_pages)
        document_sentences = document_text.split('\n')
        
        sentence_counts = dict(Counter(document_sentences))
        possible_headers = [sentence for sentence, count in sentence_counts.items() if count > pages_count*0.8]

        document_sentences_no_headers = [sentence for sentence in document_sentences if sentence not in possible_headers]
        clean_text = ' '.join(document_sentences_no_headers)

        return clean_text


# converter = PDFConverter(r'C:\Users\kubas\Desktop\test_split.pdf')
# x = converter.clean_repetetives()
# print(x)
