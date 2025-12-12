from ollama import chat
import re

response = chat(
    model="llama3.1",
    messages=[
        {
            "role": "user",
            "content": "Write a Python hello world script. Only provide the raw code.",
        }
    ],
)


code = response["message"]["content"]
code = re.sub(r"^```[\w]*\n|```$", "", code.strip())

exec(code)
