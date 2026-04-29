from llm.ollama import OllamaLLM
from llm.huggingface import HuggingFaceLLM

import os


def get_llm():
    provider = os.getenv("LLM_PROVIDER", "ollama")

    if provider == "ollama":
        return OllamaLLM()

    if provider == "huggingface":
        return HuggingFaceLLM()

    raise ValueError(f"Unknown LLM provider: {provider}")
