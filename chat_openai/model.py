
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("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")

def gerar_resposta(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
