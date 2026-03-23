def build_prompt(base_prompt, config):
    config_text = f"""
Presentation Style:
- Mode: {config.mode}
- Tone: {config.tone}
- Length: {config.length}
- Audience: {config.audience}
- Theme: {config.theme}
"""

    return base_prompt + "\n" + config_text