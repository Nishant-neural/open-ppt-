# Further work needed 
#ignore for now
class BaseLLM:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("LLM must implement generate()")