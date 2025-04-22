import openai
import os
from dotenv import load_dotenv
load_dotenv()
# Set your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_question():
    question = input("Ask a question: ")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=300
        )

        print("\nAssistant:", response.choices[0].message.content)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    ask_question()