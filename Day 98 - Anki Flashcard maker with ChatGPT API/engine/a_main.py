'''
main.py

Handles overall setup, runs the main logic, and coordinates other modules to perform the required tasks.
'''

import sys
import io
from utils import user_input_covert_to_dict
from b_pdf_reader import read_pdf


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    for line in sys.stdin:
        try:
            raw_user_input = line.strip()
            dict_user_input = user_input_covert_to_dict(raw_user_input)
            pdf_pages = read_pdf(dict_user_input['source_file_path'])
            print(pdf_pages)

        except Exception as e:
            print(e)
            continue

        sys.stdout.flush()


#TODO
    # new prompt


# test
# [{"name":"main-topic","value":"AWS Cloud Practitioner"},{"name":"source-file-path","value":"C:\\Users\\kubas\\Desktop\\test.pdf"},{"name":"cloze-count","value":"2"},{"name":"flashcard-word-length","value":"40"},{"name":"outside-scope","value":"True"},{"name":"flashcard-density-per-1000","value":"20"}]

# full
# [{"name":"main-topic","value":"AWS Cloud Practitioner"},{"name":"source-file-path","value":"C:\\Users\\kubas\\Desktop\\AWS Certified Cloud Practitioner Slides v2.11.0.pdf"},{"name":"cloze-count","value":"2"},{"name":"flashcard-word-length","value":"40"},{"name":"outside-scope","value":"True"},{"name":"flashcard-density-per-1000","value":"20"}]
