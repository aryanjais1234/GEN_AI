# Few Short Prompting: Providing a few examples to guide the model's response.

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDFYCYze4jYrPR5h0ylBCehA_B0wdyeBdQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Few Short Prompting: Providing a few examples to guide the model's response.
SYSTEM_PROMPT = """
You should only and only ans coding related question. Your name is Alexa. If the query is not related to coding. Just say sorry and do not answer that.

Rule:
- Strictly follow the output in JSON format.

Output Format:
{{
"code": "string" or "None",
"isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square formula?
A: {{"code":null, "isCodingQuestion": false}}

Q: Hi Alex can you write python code for add two numbers?
A: {{"code":"def add(a, b):
return a + b", "isCodingQuestion": true}}

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "write a code to add n number in js"}
    ]
)

print(response.choices[0].message.content)
# 1. What is Few Shot Prompting?
# Few Shot Prompting is a technique where you provide the model with a few examples of the task you want it to perform. This helps the model understand the context and format of the desired output.
# Example: "Translate the following sentences from English to French:
# Example: "Translate the following sentences from English to French:
# 1. 'Hello, how are you?' -> 'Bonjour, comment ça va?
# 2. 'What is your name?' -> 'Comment tu t'appelles?'"
# 2. When to use Few Shot Prompting?
# Use Few Shot Prompting when the task is complex or when you want to ensure that the model understands the specific format or style of the response. It is particularly useful for tasks that require a specific structure or when the model might not have enough context from a single prompt.