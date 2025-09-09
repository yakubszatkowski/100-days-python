'''
main.py

Handles overall setup, runs the main logic, and coordinates other modules to perform the required tasks.
'''

import sys
import io
import os
from utils import user_input_covert_to_dict
from b_pdf_reader import PDFConverter
from c_gpt_engine import ChatGptApi


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    for line in sys.stdin:
        try:
            raw_user_input = line.strip()
            dict_user_input = user_input_covert_to_dict(raw_user_input)
            
            file_path_input = dict_user_input['source_file_path']

            if not os.path.isfile(file_path_input):
                print(False)
                sys.stdout.flush()

            pdf_file_converter = PDFConverter(file_path_input)
            token_len, token_list  = pdf_file_converter.tokenize_text()
            
            gpt_api = ChatGptApi()
            gpt_api_instructions = gpt_api.save_instruction(
                main_topic =     dict_user_input['main_topic'],
                cloze_number =   dict_user_input['cloze_count'],
                word_count =     dict_user_input['flashcard_word_length'],
                outside_scope =  dict_user_input['outside_scope'],
                output_density = dict_user_input['flashcard_density_per_1000'],
            )

            print(gpt_api_instructions)

            'gpt-4o-mini'

        except Exception as e:
            print(e)
            continue

        sys.stdout.flush()


# test
# [{"name":"main-topic","value":"AWS Cloud Practitioner"},{"name":"source-file-path","value":"C:\\Users\\kubas\\Desktop\\test_split.pdf"},{"name":"cloze-count","value":"2"},{"name":"flashcard-word-length","value":"40"},{"name":"outside-scope","value":"True"},{"name":"flashcard-density-per-1000","value":"20"}]

# full
# [{"name":"main-topic","value":"AWS Cloud Practitioner"},{"name":"source-file-path","value":"C:\\Users\\kubas\\Desktop\\AWS Certified Cloud Practitioner Slides v2.11.0.pdf"},{"name":"cloze-count","value":"2"},{"name":"flashcard-word-length","value":"40"},{"name":"outside-scope","value":"True"},{"name":"flashcard-density-per-1000","value":"20"}]
