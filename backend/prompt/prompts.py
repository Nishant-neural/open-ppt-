# prompts.py

OUTLINE_PROMPT = """
You are an expert presentation planner.

Your job:
Create a structured outline for a presentation.

Return ONLY valid JSON.

Format:
{
  "title": "Presentation Title",
  "sections": [
    {
      "section_title": "string",
      "description": "1-2 line description"
    }
  ]
}

Rules:
- 5 to 7 sections
- Logical flow (intro → core → advanced → conclusion)
- No explanations outside JSON
"""

SLIDE_PLAN_PROMPT = """
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

CLEANUP_PROMPT = """
Fix the following JSON.

Return ONLY valid JSON.
Do not change meaning.

JSON:
"""
BEAUTIFIER_PROMPT = """
Improve wording + make concise + professional


"""