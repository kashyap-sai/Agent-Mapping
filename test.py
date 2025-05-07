import ollama

class LLM_handler:
    def __init__(self,model_name="llama3"):
        self.model_name=model_name

    def interaction(self,prompt):
        response=ollama.chat(self.model_name,messages=[{"role":'user',"content":prompt}])
        
        return response["message"]["content"]
    
llm=LLM_handler()
answer=llm.interaction("what is the capital of china?")
print("LLM response:",answer)

