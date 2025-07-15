'''
utils.py

Helper functions for small conversions and other simple tasks 
to make the code easier to read and reuse.
'''

import json


def user_input_covert_to_dict(raw_user_input):
    ''' converts raw user imput to json, then to dictionary with correctly handled variables '''
    json_user_input = json.loads(raw_user_input)

    main_topic_val = json_user_input[0]['value']
    source_file_path = json_user_input[1]['value']
    cloze_count = int(json_user_input[2]['value']) if json_user_input[2]['value'] == int else 2
    flashcard_word_length = int(json_user_input[3]['value']) if json_user_input[3]['value'] == int else 40
    outside_scope = (True if json_user_input[4]['value'] == 'True' else False)
    flashcard_density_per_100 = int(json_user_input[5]['value']) if json_user_input[3]['value'] == int else 20

    user_input = {
        'main_topic': main_topic_val,
        'source_file_path': source_file_path,
        'cloze_count': cloze_count,
        'flashcard_word_length': flashcard_word_length,
        'outside_scope': outside_scope,
        'flashcard_density_per_100': flashcard_density_per_100,
    }

    return user_input
