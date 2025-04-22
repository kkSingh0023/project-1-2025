
from litellm import completion
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()

## set ENV variables
os.environ["OPENAI_API_KEY"] =os.getenv("OPENAI_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

prompt=input("Enter anything for ur assistant")
messages = [{"role": "system", "content": "You are a helpful assistant."},{ "content": prompt,"role": "user"}]

# openai call
# response = completion(model="openai/gpt-4o", messages=messages)

# gemini call
response = completion(model="gemini/gemini-2.0-flash", messages=messages)
print(response.choices[0].message.content)