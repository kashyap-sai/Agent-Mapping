from langchain.schema.runnable import Runnable
import ollama

class LLMHandler(Runnable):
    def __init__(self, model_name="tinyllama:latest"):
        self.model_name = model_name

    def _generate_response(self, prompt):
        try:
            response = ollama.generate(
                model=self.model_name,
                prompt=prompt,
                options={
                    "num_predict": 512,
                    "temperature": 0.7,
                }
            )
            return response["response"].strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return None

    def invoke(self, input):
        return self._generate_response(input)  # Ensures compatibility with `initialize_agent`
