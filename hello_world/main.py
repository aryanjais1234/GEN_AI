from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyDFYCYze4jYrPR5h0ylBCehA_B0wdyeBdQ",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in maths and only and only ans math related question. That If the query is not related to maths. Just say sorry and do not answer that."},
        {"role": "user", "content": "what is a+b whole square"}
    ]
)

print(response.choices[0].message)