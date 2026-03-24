import json
from llm.ollama import OllamaLLM
from prompt.prompts import OUTLINE_PROMPT, CLEANUP_PROMPT
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


class SlidePlannerStage(BaseStage):
    def __init__(self, llm):
        self.llm = llm

    def run(self, outline_json):
        prompt = f"""
Create a slide plan for this presentation.

Outline:
{outline_json}

Return ONLY JSON:
{{
  "slides": [
    {{
      "heading": "string",
      "description": "what this slide should cover"
    }}
  ]
}}

Rules:
- 5–10 slides
- logical flow
- no bullet points yet
"""

        response = self.llm.generate(prompt)

        parsed = self.safe_parse(response)
        return parsed or self.fix_json(response)
    

class SlideContentStage(BaseStage):
    def __init__(self, llm):
        self.llm = llm

    def run(self, slide_plan_json):
        slides = []

        for slide in slide_plan_json.get("slides", []):
            content = self.generate_slide_content(slide)
            if content:
                slides.append(content)

        return {
            "title": "Generated Presentation",
            "slides": slides
        }

    def generate_slide_content(self, slide):
        prompt = f"""
Generate content for ONE slide.
strictly follow given schema.
The contents should strictly be in points  along with heading in the output JSON.

Slide plan:
{slide}

Return ONLY JSON:
{{
  "heading": "string",
  "points": ["point1", "point2", "point3"]
}}
"""

        response = self.llm.generate(prompt)

        parsed = self.safe_parse(response)
        return parsed or self.fix_json(response)
    