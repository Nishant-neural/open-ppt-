# open-ppt-
An open source ai based ppt pdf generator, generating ppt from prompts

## Local setup

1. Copy `.env.example` to `.env`
2. Make sure Ollama is running
3. Pull the default model:

```powershell
ollama pull llama3.2:3b
```

## Configuration

The backend reads settings from `.env` or your shell environment.

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
OLLAMA_TIMEOUT_SECONDS=120
```

`OLLAMA_MODEL` should use an exact installed model tag for reproducible runs.
