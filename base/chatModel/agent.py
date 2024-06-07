import os
import json

from openai import OpenAI
from .tools.crew.crew import course_content_crew

from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY_TWO")

client = OpenAI(api_key = openai_api_key)

functions = [
    {
        "name": "course_content_crew",
        "description": "Generates personalized course contents for a given course or skill, user current skills level and user desired level",
        "parameters": {
            "type": "object",
            "properties": {
                "course_query": {
                    "type": "string",
                    "description": "The course or skill user intends to learn, must include the language and the word 'course'. Eg. Machine learning with python course",
                },
                "current_level": {
                    "type": "string",
                    "description": "The current skill level of the user. Eg. Beginner, Intermetiate or a description, such as 'have completed DSA'",
                },
                "desired_level": {
                    "type": "string",
                    "description": "The desired or expected level of skill user intends to obtain upon completing this course. Eg. I want to master LLMs with python",
                },
                
            },
            "required": ["course_query", "current_level", "desired_level"],
        },
    }
]

system_context = """
You are an expert conversation agent in chatting with users about a course or skill they intend to learn. you will politely ask them more questions
until you have gotten all the informations you need.
###
THE INFORMATION YOU NEED BEFORE CALLING A FUNCTION:
1. Course or skill user intends to learn
2. Programming Language the user intends to learn the skill with if a language is required (this is not mandatory unless the skill to be learned requires a programming language. eg ML, DSA)
3. Background of the user: what skills the user currently has, can also be intermediate, beginner etc. It is best to detail the skills as this will guide the content generation
4. What level of expertise user is seeking to acquire. this can be mastery or till intermediate level or specific skills the user intend to have learned fully
###

````
AN EXAMPLE CONVERSATION FLOW
User: Hi Centri
AI: Hi, How may i help you today?
User: I would like to get into Data Analytics
AI: Oh Great, Can I know a little about you background? Can you provide a detailed information of the skills you currently have? Remember: my output is as good as the information you provide.
User: I know how to use excel
AI: Thank you for this information. Can you also provide detailed information about the specific data analytics skills you want to master? Remember: my output is as good as the information you provide.
User: I want to master power bi.
\n
AI calls the function
````
NOTE ONE: Call the function only when you have all obtained all the relevant information from the user, if not keep asking the user for more information. They are: course query, current skills level and desired skills level
NOTE TWO: Politely decline to answer any other request if request is not related to learning a specific skills or asking about a course.
NOTE THREE: The final output after function call must be a valid JSON object.
"""
def chat_response(message: str, model= 'gpt-4',
                  system_context: str = system_context):
    chat_messages = [
            {"role": "system", "content": system_context},
            {"role": "user", "content": message},
        ]
    intermediate_response = client.chat.completions.create(
        model= model,
        messages=chat_messages,
        functions = functions,
        function_call='auto'
    )
    chat_messages.append(intermediate_response["choices"][0]["message"])

    args = json.loads(intermediate_response["choices"][0]["message"]["function_call"]["arguments"])
    observation = course_content_crew(**args)

    chat_messages.append(
        {
            "role": "function",
            "name": "course_content_crew",
            "content": observation,
        }
    )

    response = client.chat.completions.create(
        model=model,
        messages=chat_messages,
    )

    return response.choices[0].message.content