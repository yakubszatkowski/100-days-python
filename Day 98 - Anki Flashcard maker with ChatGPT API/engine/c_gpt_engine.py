'''
gpt_engine.py
This module imports testing input that is forwarded to gpt engine
'''
import math


class ChatGptApi:
    
    def __init__(self):
        '''This class handles ChatGPT API engine'''
        pass

    def create_instruction(self, main_topic, **kwargs):
        '''
            This function returns appropriate prompt based on variables provided
        '''

        cloze_number = kwargs.get("cloze_number", 2)
        word_count = kwargs.get("word_count", 40)
        outside_scope = kwargs.get("outside_scope", True)
        # output_density = int(kwargs.get("output_density", 20))/1000
        # flashcard_count = math.ceil(len(source_text.split()) * output_density)

        instructions = f'''Task: 
- Create concise and direct statements about my input that I will be providing you based on {main_topic}
- Add cloze deletions to these statements using Anki cloze deletion mark-up. Ensure that each statement is clearly written, easily understandable, and adheres to the specified formatting and reference criteria.

Formatting Criteria:
- Construct sentences that will contain "Statement" and "Note" that will be separated by semicolon (;)
- Each “Statement" should contain a single statement written in Anki cloze deletion mark-up. Prioritize information about {main_topic}.
- Each "Note" should provide additional information for the corresponding "Statement". Do not restate or summarize information already present in the "Statment". 
- {'Information in the notes section can be outsourced outside the text' if outside_scope else 'Information in the notes section must be sourced only from the text'} 
- End of each sentence should end with breakpoint
- Output only the “Statement ; Note” pairs, each on its own line.
- Do not add section headers, numbering, or extra formatting outside of the required structure.
- Do not add any follow-up questions, suggestions, or extra commentary outside of the required Statement ; Note pairs.

Reference Criteria for each "Statement":
- Restrict each statement to {cloze_number} cloze deletions. If necessary, add 1-2 more cloze deletions, but they can only be either a cloze1 or cloze2 deletion.
- Limit the word count of each statement mentioned to less than {word_count} words.
- Keep the text within the cloze deletions limited to one or two key words.
- Each statement must be able to stand alone. Include the subject of the statement somewhere in the text.
- Keep ONLY simple, direct, cloze deletion statements in the "Statements". Keep any additional explanatory information in the "Notes".
- {'Expand with valuable insights beyond the given text, incorporating relevant knowledge for a richer response.' if outside_scope else 'Limit the response strictly to the information provided in the source text'} 
- Example Chatbot Response:
''' + r'{{c1::Necrosis}} in pancreatitis is identified by lack of contrast enhancement after bolus contrast administration. ; Necrotizing pancreatitis is associated with increased severity of disease and increased risk of death.'

        return instructions

    def request(self):
        '''Sends message prompt to ChatGPT'''


PROMPT_MESSAGE = ChatGptApi().create_instruction('AWS Cloud Practitioner')
print(PROMPT_MESSAGE)

# - Try to cover every aspect of the reviewed text in the flashcards, make at least {flashcard_count} of them
