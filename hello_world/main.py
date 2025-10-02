import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("GEMINI_BASE_URL")
)

response = client.chat.completions.create(
    model=os.getenv("MODEL_NAME"),
    messages=[
        {"role": "system", "content": "You are an expert in maths and only and only ans math related question. That If the query is not related to maths. Just say sorry and do not answer that."},
        {"role": "user", "content": "what is a+b whole square"}
    ]
)

print(response.choices[0].message)