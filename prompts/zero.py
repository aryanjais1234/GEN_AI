from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDFYCYze4jYrPR5h0ylBCehA_B0wdyeBdQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Zero Shot Prompting: Directly asking the model to do a task without any examples.
SYSTEM_PROMPT = "You should only and only ans coding related question. Your name is Alexa. If the query is not related to coding. Just say sorry and do not answer that."

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hi Alex can you write python code to translate hindi to english?"}
    ]
)

print(response.choices[0].message)

# 1. What is Zero Shot Prompting?
# Zero Shot Prompting is a technique where you directly ask the model to perform a task without providing any examples or demonstrations. The model relies on its pre-trained knowledge to understand and respond to the prompt.
# Example: "Translate the following sentence from English to French: 'Hello, how are you?'"
# 2. When to use Zero Shot Prompting?
# Use Zero Shot Prompting when you want a quick response for a task that the model is likely to understand based on its training data. It is useful for straightforward tasks where examples are not necessary.