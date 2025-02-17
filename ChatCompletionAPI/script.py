import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "developer", 
            "content": "You are a helpful and pleasant assistant, present yourself accordingly."
        },
        # {
        #     "role": "user",
        #     "content": "H."
        # }
    ],
    max_tokens=100,
    temperature=0.9
)

print(completion.choices[0].message)