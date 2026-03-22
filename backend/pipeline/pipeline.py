
from pipeline.engine import PipelineEngine
from pipeline.stages import OutlineStage, SlideStage
from llm.selector import get_llm


def generate_presentation(user_prompt):
    llm = get_llm()

    pipeline = PipelineEngine([
        OutlineStage(llm),
        SlideStage(llm)
    ])

    result = pipeline.run(user_prompt)

    if "error" in result:
        return result

    return {
        "title": result.get("title", ""),
        "slides": result.get("slides", [])
    }