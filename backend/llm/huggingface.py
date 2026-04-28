import os
import requests
from llm.base import BaseLLM


class HuggingFaceLLM(BaseLLM):
    def __init__(self):
        self.token = os.getenv("HF_TOKEN")
        self.model = os.getenv("HF_MODEL", "Qwen/Qwen2.5-7B-Instruct-1M:fastest")
        self.base_url = os.getenv("HF_BASE_URL", "https://router.huggingface.co/v1/chat/completions")
        self.timeout = int(os.getenv("HF_TIMEOUT_SECONDS", "120"))

        if not self.token:
            raise RuntimeError("HF_TOKEN is missing")

    def generate(self, prompt: str, retries=3) -> str:
        for attempt in range(retries):
            try:
                response = requests.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self.token}",
                        "Content-Type": "application/json",
                    },
                    json={
                        "model": self.model,
                        "messages": [
                            {"role": "user", "content": prompt}
                        ],
                        "temperature": 0.2,
                        "stream": False,
                    },
                    timeout=self.timeout,
                )

                payload = response.json()

                if response.ok:
                    return payload["choices"][0]["message"]["content"]

                if attempt == retries - 1:
                    raise RuntimeError(payload)

            except Exception as e:
                if attempt == retries - 1:
                    raise e

        raise RuntimeError("Hugging Face failed after retries")
