'''
main.py

Handles overall setup, runs the main logic, and coordinates other modules to perform the required tasks.
'''
import sys
from utils import user_input_covert_to_dict
from b_pdf_reader import read_pdf


if __name__ == '__main__':
    for line in sys.stdin:
        raw_user_input = line.strip()
        dict_user_input = user_input_covert_to_dict(raw_user_input)
        print(dict_user_input['source_file_path'])

        pdf_text = read_pdf(dict_user_input['source_file_path'])

        
        print(pdf_text)
        sys.stdout.flush()
