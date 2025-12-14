from ollama import chat
import re

class CodeBlock:
    """
    Generates and executes code based on the provided prompt.
    """

    def __init__(self, model="llama3.1", run_count=1):
        self.model = model
        self.run_count = run_count

    def generate_and_execute(self, prompt):
        self.prompt = prompt
        response = chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        
        # show current task as running
        print(f"Running task {self.show_status_loading()}: {self.summarize(self.prompt)}")

        try:
            code = response["message"]["content"]
            code = re.sub(r"^```[\w]*\n|```$", "", code.strip())
            exec(code)
            
        except Exception as e:
            print(f"Error executing code: {e}")

    # print current run count and increment it
    def show_status_loading(self):
        run_count_old = self.run_count
        self.run_count += 1
        return run_count_old

    # provide brief summarization of current executed task
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
        for i in range(3):
            print("Executing Code...")
            self.codeblock.generate_and_execute(self.prompt)
            print("Execution Complete.")

if __name__ == "__main__":
    orchestrator = Orchestrator(
        prompt="Generate a Python Hello World script. Only provide the raw code.",
        model="llama3.1"
    )
    orchestrator.run()
