"""This module imports testing input that is forwarded to gpt engine"""
from test import test_input
import math


class ChatGPTAPI:
    """This class handles ChatGPT engine"""
    def __init__(self):
        pass

    def prompt_input(self, main_topic, source_text, **kwargs):
        """
            This function returns appropriate prompt based on variables provided
        """

        cloze_number = kwargs.get("cloze_number", 2)
        word_count = kwargs.get("word_count", 40)
        outside_scope = kwargs.get("outside_scope", True)
        output_density = int(kwargs.get("output_density", 20))/1000
        flashcard_count = math.ceil(len(source_text.split()) * output_density)

        prompt = f'Review Text: "{source_text} " \n Task: \n- Create concise and direct statements from '+\
            f'the provided text that focus on {main_topic}. \n- Add cloze deletions to these statements using Anki '+\
            'cloze deletion mark-up. Ensure that each statement is clearly written, easily understandable, and '+\
            'adheres to the specified formatting and reference criteria.\n\nFormatting Criteria: \n- Construct a '+\
            'table with three columns: "Statements", "Notes", and "Number".\n- Each row of the "Statements" column '+\
            'should contain a single statement written in Anki cloze deletion mark-up. Prioritize information about '+\
            f'{main_topic}.\n- Each row of the "Notes" column should provide additional information for the '+\
            'corresponding "Statement". Do not restate or summarize information already present in the "Statment". '+\
            'Information in the notes section should be sourced from the text.\n- The "Number" column should serve '+\
            'to number each row, facilitating feedback.\n\nReference Criteria for each "Statement":\n- Restrict '+\
            f'each statement to {cloze_number} cloze deletions. If necessary, add 1-2 more cloze deletions, but they '+\
            'can only be either a cloze1 or cloze2 deletion.\n- Limit the word count of each statement mentioned to '+\
            f'less than {word_count} words.\n- Keep the text within the cloze deletions limited to one or two key '+\
            'words.\n- Each statement must be able to stand alone. Include the subject of the statement somewhere in '+\
            'the text.\n- Keep ONLY simple, direct, cloze deletion statements in the "Statements" column. Keep any '+\
            'additional explanatory information in the "Notes" column.\n- Try to cover every aspect of the reviewed '+\
            f'text in the flashcards, make at least {flashcard_count} of them\n' +\
            f'- Expand with valuable {main_topic} insights beyond the given text, incorporating relevant knowledge '+\
            'for a richer response.' if outside_scope else '- Limit the response strictly to the information '+\
            'provided in the source text'+\
            'Example Chatbot Response: \n| Statements | Notes | Number |\n| --- | --- | --- |\n| {{c1::Necrosis}} ' +\
            'in pancreatitis is identified by lack of contrast enhancement after bolus contrast administration. | ' +\
            'Necrotizing pancreatitis is associated with increased severity of disease and increased risk of ' +\
            'death. | 1 |\n| Acute {{c1::peripancreatic fluid collections}} are non-encapsulated aggregations of ' +\
            'fluid in the pancreatic bed and retroperitoneum.  |  | 2 |\n'

        return prompt

    def request(self):
        """Sends message prompt to ChatGPT"""


PROMPT_MESSAGE = ChatGPTAPI().prompt_input("AWS, Amazon Web Services", test_input)
print(PROMPT_MESSAGE)
