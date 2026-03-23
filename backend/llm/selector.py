from llm.ollama import OllamaLLM

import os


def get_llm():
    provider = os.getenv("LLM_PROVIDER", "ollama")

    if provider == "ollama":
        return OllamaLLM()

    else:
        raise ValueError(f"Unknown LLM provider: {provider}")
