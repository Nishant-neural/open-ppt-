import json
from llm.ollama import OllamaLLM
from prompt.prompts import OUTLINE_PROMPT, SLIDE_PROMPT, CLEANUP_PROMPT
from prompt.builder import build_prompt

class BaseStage:
    def safe_parse(self, text):
        try:
            return json.loads(text)
        except:
            return None
        
    def fix_json(self, bad_json):
        fixed = self.llm.generate(CLEANUP_PROMPT + bad_json)
        return self.safe_parse(fixed)

    
class OutlineStage(BaseStage):
    def __init__(self, llm, config):
        self.llm = llm
        self.config = config

    def run(self, user_prompt):
        prompt = build_prompt(OUTLINE_PROMPT, self.config)
        prompt += "\nTopic:\n" + user_prompt

        response = self.llm.generate(prompt)

        parsed = self.safe_parse(response)
        return parsed or self.fix_json(response)


class SlideStage(BaseStage):
    def __init__(self, llm, config):
        self.llm = llm
        self.config = config

    def run(self, outline_json):
        prompt= build_prompt(SLIDE_PROMPT,self.config)
        prompt += "\nOutline:\n" + json.dumps(outline_json)
        response = self.llm.generate(prompt)

        parsed = self.safe_parse(response)
        return parsed or self.fix_json(response)
