
from pipeline.engine import PipelineEngine
from pipeline.stages import OutlineStage, SlidePlannerStage,SlideContentStage
from llm.selector import get_llm
from config.blueprint import PresentationConfig
from config.presets import startup_pitch_mode,student_mode,professional_mode

def generate_presentation(user_prompt, user_config=None):
    llm = get_llm()

    config = user_config or PresentationConfig()
     #parametrs in presentation config can be used or presets can be used here

    pipeline = PipelineEngine([
    OutlineStage(llm,config),
    SlidePlannerStage(llm),
    SlideContentStage(llm)
])
    return pipeline.run(user_prompt)
