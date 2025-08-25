'''
gpt_engine.py
This module imports testing input that is forwarded to gpt engine
'''
import re

class ChatGptApi:
    
    def __init__(self):
        '''Initialize ChatGPT API engine'''
        pass

    def save_instruction(self, main_topic, **kwargs):
        '''Generate instructions for creating Anki cloze cards based on a given topic.
        Args:
            main_topic (str): The main topic for the Anki cards.
            **kwargs:
                cloze_number (int, optional): Number of cloze deletions per statement (default 2).
                word_count (int, optional): Maximum word count for statements and notes (default 60).
                outside_scope (bool, optional): Whether notes can include external sources (default True).
                output_density (int, optional): Number of cards generated per ~1000 tokens (default 10).

        Returns:
            str: A formatted instruction string for GPT prompting'''
        

        cloze_number = kwargs.get("cloze_number", 2)
        word_count = kwargs.get("word_count", 60)
        outside_scope = kwargs.get("outside_scope", True)
        output_density = int(kwargs.get("output_density", 10))

        instructions = f'''Task:
            - You are a proffesional teacher specialized in getting people ready for {main_topic} exam
            - Generate concise Anki cloze statements from {main_topic}, each with at least {cloze_number} (max {cloze_number+1}) clozes and <{word_count} words.
            - Format: Statement ; Note (no labels/headers, one per line, end with breakpoint). Statement: simple, standalone, key info. Note: extra info, {'may include outside sources' if outside_scope else 'only from source text'}.
            - Output at least {output_density} cards.
            - Example: {{{{c1::Semi-supervised learning}}}} trains a model with both labeled and {{{{c1::unlabeled data}}}}; Semi-supervised learning is a machine learning approach combining labeled and unlabeled data for classification or regression.'''

        return re.sub('  ', '', instructions)

    def request(self, instruction, prompt):
        '''Sends call prompt to ChatGPT'''

PROMPT_MESSAGE = ChatGptApi().save_instruction('AWS Cloud Practitioner')
print(PROMPT_MESSAGE)
