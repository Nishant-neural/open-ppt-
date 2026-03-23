
from pipeline.engine import PipelineEngine
from pipeline.stages import OutlineStage, SlideStage
from llm.selector import get_llm
from config.blueprint import PresentationConfig

def generate_presentation(user_prompt, user_config=None):
    llm = get_llm()

    config = user_config or PresentationConfig()

    pipeline = PipelineEngine([
        OutlineStage(llm, config),
        SlideStage(llm, config)
    ])

    return pipeline.run(user_prompt)