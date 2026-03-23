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

SLIDE_PROMPT = """
You are an expert presentation creator.

Convert the given outline into slides.

Return ONLY valid JSON.

Format:
{
  "slides": [
    {
      "heading": "string",
      "points": ["point1", "point2", "point3"]
    }
  ]
}

Rules:
- Each section → 1-2 slides
- Max 5 bullet points per slide
- Each point ≤ 12 words
- Clear and concise
- No explanations outside JSON
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