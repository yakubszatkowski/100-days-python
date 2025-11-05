'''
gpt_engine.py
This module imports testing input that is forwarded to gpt engine
'''
import re
import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

class ChatGptApi:
    
    def __init__(self):
        '''Initialize ChatGPT API engine'''
        self.cloze_number = None
        self.word_count = None
        self.outside_scope = None
        self.output_density = None
        self.model = 'gpt-4o-mini'

        load_dotenv()
        chat_gpt_api_key = os.getenv('OPENAI_API_KEY')
        self.client = AsyncOpenAI(api_key=chat_gpt_api_key)


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
            - Format: Statement ; Note (no labels/headers, one per line, always ends with breakpoint). 
            - Statement: simple, standalone, key info, must contain cloze. 
            - Note: extra info, {'may include outside sources' if self.outside_scope else 'only from source text'}, never contains cloze.
            - Output at least {self.output_density} cards
            - Example: {{{{c1::Semi-supervised learning}}}} trains a model with both {{{{c2::labeled and unlabeled}}}} data; Semi-supervised learning is a machine learning approach combining labeled and unlabeled data for classification or regression'''

        return re.sub('  ', '', instructions)


    async def get_response(self, instruction, prompt):
        print('start task')
        response = await self.client.responses.create(
            model=self.model,
            instructions=instruction,
            input=prompt,
        )

        return response.output_text


    async def get_all_responses(self, instruction, prompt_list):
        tasks = []
        async with asyncio.TaskGroup() as tg:
            for i, prompt in enumerate(prompt_list):
                print('create task', i)
                task = tg.create_task(self.get_response(instruction, prompt))
                tasks.append(task)
        
        print('finalized results')
        results = [task.result() for task in tasks]

        print(len(results), ' - length')
        return results

