
from pipeline.pipelineGen import generate_presentation
from presentation.ppt import create_ppt
prompt = input('Enter your prompt->')
result = generate_presentation(prompt)
print(result)
file = create_ppt(result)
print("Saved:", file)
