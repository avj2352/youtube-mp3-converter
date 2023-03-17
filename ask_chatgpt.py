'''
Simple ChatGPT interface
getting familiar with openai
https://github.com/openai/openai-quickstart-python/blob/master/app.py
'''

import openai
from util.config import OPEN_AI_API_KEY, typing_print

openai.api_key = OPEN_AI_API_KEY
model_engine = 'text-davinci-003'

def chat_gpt(text: str):
    print('generating response...')
    response = openai.Completion.create(
            engine=model_engine,
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
            )
    typing_print(response.choices[0].text)


# print(OPEN_AI_API_KEY)
text:str = input('🤖 Ask chatgpt: ')
chat_gpt(text) if text != '' else print('Invalid input, ask a valid question')
