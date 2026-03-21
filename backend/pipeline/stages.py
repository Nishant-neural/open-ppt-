import json
from llm import call_llm
from prompts import OUTLINE_PROMPT, SLIDE_PROMPT, CLEANUP_PROMPT


class BaseStage:
    def safe_parse(self, text):
        try:
            return json.loads(text)
        except:
            return None

    def fix_json(self, bad_json):
        fixed = call_llm(CLEANUP_PROMPT + bad_json)
        return self.safe_parse(fixed)


class OutlineStage(BaseStage):
    def run(self, user_prompt):
        prompt = OUTLINE_PROMPT + "\nTopic:\n" + user_prompt
        response = call_llm(prompt)

        parsed = self.safe_parse(response)
        return parsed or self.fix_json(response)


class SlideStage(BaseStage):
    def run(self, outline_json):
        prompt = SLIDE_PROMPT + "\nOutline:\n" + json.dumps(outline_json)
        response = call_llm(prompt)

        parsed = self.safe_parse(response)
        return parsed or self.fix_json(response)