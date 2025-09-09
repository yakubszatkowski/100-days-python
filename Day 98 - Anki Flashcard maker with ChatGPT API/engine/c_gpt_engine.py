'''
gpt_engine.py
This module imports testing input that is forwarded to gpt engine
'''
import re
import os

from openai import OpenAI
from dotenv import load_dotenv

class ChatGptApi:
    
    def __init__(self):
        '''Initialize ChatGPT API engine'''
        self.cloze_number = None
        self.word_count = None
        self.outside_scope = None
        self.output_density = None

        load_dotenv()
        chat_gpt_api_key = os.getenv("OPENAI_API_KEY")
        self.client  = OpenAI(api_key=chat_gpt_api_key)
        

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
        
        self.cloze_number = kwargs.get("cloze_number", 2)
        self.word_count = kwargs.get("word_count", 60)
        self.outside_scope = kwargs.get("outside_scope", True)
        self.output_density = int(kwargs.get("output_density", 10))

        instructions = f'''Task:
            - You are a proffesional teacher specialized in getting people ready for {main_topic} exam
            - Generate concise Anki cloze statements from {main_topic}, each with at least {self.cloze_number} (max {self.cloze_number+1}) clozes and <{self.word_count} words
            - Format: Statement ; Note (no labels/headers, one per line, end with breakpoint). Statement: simple, standalone, key info. Note: extra info, {'may include outside sources' if self.outside_scope else 'only from source text'}
            - Output at least {self.output_density} cards
            - Example: {{{{c1::Semi-supervised learning}}}} trains a model with both labeled and unlabeled data; Semi-supervised learning is a machine learning approach combining labeled and unlabeled data for classification or  {{{{c1::regression}}}}'''

        return re.sub('  ', '', instructions)

    def request(self, instruction, prompt):
        '''Sends call prompt to ChatGPT'''



# gpt_api = ChatGptApi()
# gpt_api_instructions = gpt_api.save_instruction(
#     main_topic='AWS Cloud Practitioner',
#     cloze_number=2,
#     word_count=60,
#     outside_scope=True,
#     output_density=10,
# )

# print(gpt_api_instructions)