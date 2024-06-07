import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key = api_key)

system_context="""
You are adept at generating very accurate code in response to user's
queries. You are to be used within an application developed solely for 
generating code. if the user's request doesn't provide enough context to
facilitate the generation of very accurate code, request more infromation 
from the user that will provide all context required for generating the code.
Politely decline to answer any question that isn't code or algorithm related.

Example: if the user does not specify the programming language in the query, 
ask for the programming language before generating any code.
"""

def code_response(message: str, model= 'gpt-4',
                  system_context: str= system_context, max_tokens= 4096):
    response = client.chat.completions.create(
        model= model,
        messages=[
            {"role": "system", "content": system_context},
            {"role": "user", "content": message},
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":

    message = input("Enter a question for the : ")
    response_str = code_response(message)

    print(response_str[:])


