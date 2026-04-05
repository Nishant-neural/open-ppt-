
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


CLEANUP_PROMPT = """
You are a fixer.
Task:
Convert BAD_OUTPUT into strict JSON.

Return ONLY valid JSON.
Do not change meaning.

Rules:
- Return STRICT JSON.
- Do NOT include explanations, markdown, or extra text.
- Do NOT wrap the JSON in quotes.
- If the input looks like a single slide, return one JSON object.
- If the input looks like a presentation, return a JSON object with a "slides" array.

BAD_OUTPUT:
"""
