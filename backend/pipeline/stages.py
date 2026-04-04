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
Create a presentation slide plan.

Outline:
{outline_json}

Return ONLY JSON:
{{
  "slides": [
    {{
      "type": "title | bullets | image_text",
      "layout": "center | two_column",
      "heading": "string",
      "description": "short description "
    }}
  ]
}}

Rules:
- First slide must be "title"
- Keep variety in layouts
- Do not invent new types and layouts.
- Stick to the  types and layouts  given in example only.
- 5-10 slides
- logical flow
- no bullet points yet

- Use two_column when:
  - comparing ideas
  - listing categories
  - showing pros/cons

- Use center when:
  - explaining concepts
  - storytelling

- Use "image_text" when:
  - concept is visual
  - diagram helps
  - architecture explanation
  - Use "two_column" for image_text
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
        if slide["type"] == "image_text":
           return self.generate_image_slide(slide)
        
        if slide.get("layout") not in ["center", "two_column"]:
           slide["layout"] = "center"

        layout = slide.get("layout")
        
        if layout == "two_column":
           response = self.generate_two_column(slide)
        else:
           response = self.generate_center(slide)

        parsed = self.safe_parse(response)
        return parsed or self.fix_json(response)
        

    def generate_two_column(self, slide):
       prompt = f"""
       You are a presentation slide content generator.
      Generate content for a two_column slide.

 Slide:
{slide}

Return only JSON:
{{
  "type": "bullets",
  "layout": "two_column",
  "heading": "...",
  "left": ["...", "..."],
  "right": ["...", "..."]
}}
"""
       return self.llm.generate(prompt)
        
    
    def generate_center(self, slide):
       prompt = f"""
       You are a presentation slide content generator.
Generate content for slide.

Slide:
{slide}

Return only JSON:
{{
  "type": "bullets",
  "layout": "center",
  "heading": "...",
  "points": ["...", "..."]
}}
"""
       return self.llm.generate(prompt)
        
    def generate_image_slide(self, slide):
       prompt = f"""
Generate an image-based slide.

Slide:
{slide}

Return JSON:
{{
  "type": "image_text",
  "layout": "two_column",
  "heading": "...",
  "text": "short explanation",
  "image_query": "search keywords"
}}

Rules:
- image_query should be specific (e.g., 'neural network layers diagram')
- text should be short (2–3 lines)
"""
       return self.llm.generate(prompt)