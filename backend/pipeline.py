
import json
from llm import call_llm
from prompts import OUTLINE_PROMPT, SLIDE_PROMPT, CLEANUP_PROMPT


def safe_json_parse(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def fix_json(bad_json):
    fixed = call_llm(CLEANUP_PROMPT + bad_json)
    return safe_json_parse(fixed)


def generate_outline(user_prompt):
    prompt = OUTLINE_PROMPT + "\nTopic:\n" + user_prompt
    response = call_llm(prompt)

    parsed = safe_json_parse(response)
    if parsed:
        return parsed
    
    return fix_json(response)


def generate_slides(outline_json):
    prompt = SLIDE_PROMPT + "\nOutline:\n" + json.dumps(outline_json)
    response = call_llm(prompt)

    parsed = safe_json_parse(response)
    if parsed:
        return parsed
    
    return fix_json(response)


def generate_presentation(user_prompt):
    
    outline = generate_outline(user_prompt)

    if outline is None:
        return {"error": "Outline generation failed"}

  
    slides = generate_slides(outline)

    if slides is None:
        return {"error": "Slide generation failed"}

    return {
        "title": outline.get("title", ""),
        "slides": slides.get("slides", [])
    }