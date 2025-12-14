from ollama import chat
import re

class CodeBlock:
    """"
    Generates code block based on the provided prompt using the specified model.
    """

    def __init__(self, prompt, model="llama3.1"):
        self.model=model
        self.prompt=prompt
        response = chat(
        model=self.model,
        messages=[
            {
                "role": "user",
                "content": self.prompt,
            }
        ],
    )
        try:
            code = response["message"]["content"]
            code = re.sub(r"^```[\w]*\n|```$", "", code.strip())
            print(code)
            return exec(code)
        except Exception as e:
            print(f"Error executing code: {e}")

flow = CodeBlock(
    prompt="""Generate a Python Hello World script. Only provide the raw code.""",
    model="llama3.1"
    )


