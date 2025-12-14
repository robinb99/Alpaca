from ollama import chat
import re

class CodeBlock:
    """
    Generates and executes code based on the provided prompt.
    """

    def __init__(self, model="llama3.1"):
        self.model = model

    def generate_and_execute(self, prompt):
        response = chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )

        try:
            code = response["message"]["content"]
            code = re.sub(r"^```[\w]*\n|```$", "", code.strip())
            exec(code)
        except Exception as e:
            print(f"Error executing code: {e}")

    def summarize(self, prompt):
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Please summarize the following prompt in only a few words: {prompt}"
                }
            ],
        )
        return response["message"]["content"]
    
class Orchestrator:
    def __init__(self, prompt, model="llama3.1"):
        self.prompt = prompt
        self.model = model
        self.codeblock = CodeBlock(model=self.model)

    def run(self):
        print("Executing Code...")
        self.codeblock.generate_and_execute(self.prompt)
        print(f"Running task: {self.codeblock.summarize(self.prompt)}")

        print("Execution Complete.")

if __name__ == "__main__":
    orchestrator = Orchestrator(
        prompt="Generate a Python Hello World script. Only provide the raw code.",
        model="llama3.1"
    )
    orchestrator.run()
