from openai import OpenAI
from dotenv import load_dotenv

import json
import os

load_dotenv()



# Configurar el cliente de deepseek con openai
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
    base_url=os.getenv("base_url")
    )

system_prompt = """
The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format. 

EXAMPLE INPUT: 
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "question": "Which is the highest mountain in the world?",
    "answer": "Mount Everest"
}
"""

# Prompt para deepseek
prompt_input = input ("Hola, que deseas saber? ")

messages = [{"role": "system", "content": system_prompt}, 
            {"role": "user", "content": prompt_input}]

# Crear la instancia para que responda el modelo. 
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    response_format={
        'type': 'json_object'
    },
    max_tokens=1024,
    temperature=0.7,
    stream=False
)

# Imprimir la respuesta. 
print(json.loads(response.choices[0].message.content))