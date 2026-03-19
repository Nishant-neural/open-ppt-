
import requests

from settings import OLLAMA_BASE_URL, OLLAMA_MODEL, OLLAMA_TIMEOUT_SECONDS


def call_llm(prompt, model=None):
    model = model or OLLAMA_MODEL

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.3
        },
        timeout=OLLAMA_TIMEOUT_SECONDS
    )

    payload = response.json()

    if not response.ok:
        error_message = payload.get("error")
        if error_message:
            raise RuntimeError(f"Ollama request failed for model '{model}': {error_message}")
        raise RuntimeError(
            f"Ollama request failed with status {response.status_code}: {payload}"
        )

    if "response" in payload:
        return payload["response"]

    error_message = payload.get("error")
    if error_message:
        raise RuntimeError(f"LLM API error: {error_message}")

    if payload.get("message", {}).get("content"):
        return payload["message"]["content"]

    raise RuntimeError(f"Unexpected LLM response format: {payload}")
