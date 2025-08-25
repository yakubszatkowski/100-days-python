'''
pdf_reader.py

Module that contains class used to process .pdf files
'''

import pymupdf
import re
from collections import Counter 
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFConverter():

    def __init__(self, file_path):
        '''Initialize PDF Converter with file path'''
        self.file_path = file_path
        self.token_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=1000,
            chunk_overlap=50
        )


    def read_pdf(self):
        '''Reads .pdf file by file path and return formatted string of it'''
        with pymupdf.open(self.file_path) as doc:
            page_list = [page.get_text() for page in doc]

            return page_list



    def clean_repetetives(self):
        '''Cleans .pdf file from footers, headers and other repetitive sentences, characters and returns clean text'''
        document_pages = self.read_pdf() 
        pages_count = len(document_pages)

        document_text = ' '.join(document_pages)
        document_sentences = document_text.split('\n')
        
        sentence_counts = dict(Counter(document_sentences))
        possible_headers = [sentence for sentence, count in sentence_counts.items() if count > pages_count*0.8]

        document_sentences_no_headers = [sentence for sentence in document_sentences if sentence not in possible_headers]
        clean_text = re.sub(' +', ' ', ' '.join(document_sentences_no_headers))

        return clean_text


    def tokenize_text(self):
        '''Splits clen text into tokens, returns length of cunks and token chunks'''
        clean_text = self.clean_repetetives()
        token_chunks = self.token_splitter.split_text(clean_text)
        len_token_chunks = len(token_chunks)
        
        return len_token_chunks, token_chunks


converter = PDFConverter(r'C:\Users\kubas\Desktop\test_split.pdf')
token_len, token_list  = converter.tokenize_text()
clean_text = converter.clean_repetetives()
postion = 19

print(token_list[postion])
print(len(token_list[postion]))
print(token_len)
print(clean_text)