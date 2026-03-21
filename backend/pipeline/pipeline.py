from pipeline.engine import PipelineEngine
from pipeline.stages import OutlineStage, SlideStage


def generate_presentation(user_prompt):
    pipeline = PipelineEngine([
        OutlineStage(),
        SlideStage()
    ])

    result = pipeline.run(user_prompt)

    if "error" in result:
        return result

    return {
        "title": result.get("title", ""),
        "slides": result.get("slides", [])
    }