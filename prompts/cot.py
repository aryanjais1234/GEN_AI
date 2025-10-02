# Chain of Thaught (CoT) Prompting: Providing a series of examples to guide the model's reasoning process.

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("GEMINI_BASE_URL")
)

SYSTEM_PROMPT = """
  You are an expert AI Assistant in resolving user queries using chain of thought.
  You work on START, PLAN and OUTPUT steps.
  You need to first PLAN what needs to be done. The PLAN can be multiple steps.
  Once you think enough PLAN has been done, finally you can give an OUTPUT.

  Rules:
  - Strictly follow the given JSON output format.
  - Only run one step at a time.
  - The Sequence of steps is START (where user gives an input), PLAN     (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).
  
  Output JSON Format:
  { "step" : "START" | "PLAN" | "OUTPUT", "content": "string" }

  Example:
  START: Hey, Can you solve 2 + 3 * 5 / 10
  PLAN: {"step": "PLAN": "content": "Seems like user is interested in maths problem" }
  PLAN: {"step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
  PLAN: {"step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here"}
  PLAN: {"step": "PLAN", "content": "first we must multiply 3 * 5 which is 15"}
  PLAN: {"step": "PLAN", "content": "then we must divide 15 / 10 which is 1.5"}
  PLAN: {"step": "PLAN", "content": "finally we must add 2 + 1.5 which is 3.5"}
  OUTPUT: {"step": "OUTPUT", "content": "So the final answer is 3.5"}

"""
print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("👉 ")


message_history.append({"role": "user", "content": user_query})

while True:
  response = client.chat.completions.create(
    model=os.getenv("MODEL_NAME"),
    response_format={"type":"json_object"},
    messages=message_history
  )
  raw_result = (response.choices[0].message.content)
  message_history.append({"role": "assistant", "content": raw_result})
  parsed_result = json.loads(raw_result)

  if parsed_result.get("step") == "START":
    print("🔥",parsed_result.get("content"))
    continue
  elif parsed_result.get("step") == "PLAN":
    print("🧠",parsed_result.get("content"))
    continue
  elif parsed_result.get("step") == "OUTPUT":
    print("💡",parsed_result.get("content"))
    break


# 1. What is Chain of Thought (CoT) Prompting?
# Chain of Thought (CoT) Prompting is a technique where you provide the model with a series of examples that demonstrate a step-by-step reasoning process. This helps the model to break down complex tasks into smaller, manageable steps, leading to more accurate and coherent responses.
# Example: "To solve the math problem 2 + 3 * 5, first multiply 3 by 5 to get 15, then add 2 to get 17."
# 2. When to use Chain of Thought (CoT) Prompting?
# Use Chain of Thought (CoT) Prompting when the task requires multi-step reasoning or when the model needs to follow a specific process to arrive at the correct answer. It is particularly useful for complex problems that cannot be solved with a single prompt.