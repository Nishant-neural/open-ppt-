import requests
from llm.base import BaseLLM
from settings import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_TIMEOUT_SECONDS


class OllamaLLM(BaseLLM):
    def __init__(self, model=None):
        self.model = model or OLLAMA_MODEL

    def generate(self, prompt: str, retries=3) -> str:
        for attempt in range(retries):
            try:
                response = requests.post(
                    f"{OLLAMA_BASE_URL}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "stream": False,
                        "temperature": 0.3
                    },
                    timeout=OLLAMA_TIMEOUT_SECONDS
                )

                payload = response.json()

                if response.ok and "response" in payload:
                    return payload["response"]

            except Exception as e:
                if attempt == retries - 1:
                    raise e

        raise RuntimeError("Ollama failed after retries")
