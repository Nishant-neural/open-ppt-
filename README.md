# OpenPPT

OpenPPT is a local-first AI presentation generator that turns a plain-language prompt into a slide deck structure and renders the result in a React-based presentation viewer.

It uses a FastAPI backend, a stage based content-generation pipeline, and a local Ollama model so you can experiment with AI-generated presentations without depending on a hosted LLM.

## Demo

Repository: [github.com/Nishant-neural/open-ppt-](https://github.com/Nishant-neural/open-ppt-)

Demo video: [Watch the project demo](./demo/demo_vid.mp4)

Demo configuration: the showcased generation flow was recorded using Ollama with the `llama3.2:3b` model.

## What It Does

- Takes a topic or prompt from the user
- Generates an outline and slide plan with an LLM
- Produces structured slide content for multiple slide types
- Renders the generated deck in a presentation-style frontend
- Runs locally with Ollama as the default model provider

## Why I Built It

I built OpenPPT to explore how LLM pipelines can be used for structured content generation instead of simple chat responses. The goal was to create a project that combines product thinking, prompt design, backend orchestration, and frontend rendering in one end-to-end application.

## Tech Stack

- Frontend: React, Vite, Framer Motion
- Backend: FastAPI, Pydantic
- LLM Runtime: Ollama
- Language: JavaScript and Python

## Project Structure

```text
open-ppt-/
|-- backend/
|   |-- main.py
|   |-- settings.py
|   |-- pipeline/
|   |-- llm/
|   |-- prompt/
|   `-- config/
|-- demo/
|   `-- demo_vid.mp4
|-- open-ppt-frontend/
|   |-- src/
|   |-- public/
|   `-- package.json
|-- .env.example
`-- README.md
```

## How It Works

The backend uses a staged pipeline:

1. `OutlineStage` generates a high-level presentation outline from the user prompt.
2. `SlidePlannerStage` converts that outline into a slide-by-slide plan with layout and slide type decisions.
3. `SlideContentStage` generates the final content for each slide in structured JSON.

The frontend sends the prompt to the backend, receives the generated slide JSON, and displays the deck in a presentation viewer.

## Local Setup

### 1. Clone the repository

```powershell
git clone https://github.com/Nishant-neural/open-ppt-.git
cd open-ppt-
```

### 2. Configure environment variables

Copy `.env.example` to `.env`.

Example:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
OLLAMA_TIMEOUT_SECONDS=120
```

### 3. Start Ollama

Make sure Ollama is installed and running, then pull the default model:

```powershell
ollama pull llama3.2:3b
```

### 4. Run the backend

Install the Python dependencies you use locally, then start the FastAPI server from the project root:

```powershell
uvicorn backend.main:app --reload
```

The backend will be available at `http://localhost:8000`.

### 5. Run the frontend

```powershell
cd open-ppt-frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`.

## Example Flow

Prompt:

```text
Create a presentation on how startups validate product-market fit
```

Output:

- AI-generated slide outline
- Planned slide layouts
- Generated slide content rendered in the frontend viewer

## Highlights

- Local-first AI workflow using Ollama
- Modular backend pipeline design
- Structured JSON generation instead of free-form text output
- Multiple slide layouts and presentation rendering in the frontend

## Current Scope

This project currently focuses on presentation generation and on-screen slide rendering. 

## Future Improvements

- Add export and download flows for generated presentations
- Improve prompt controls for audience, tone, and length
- Add stronger validation and retry handling around model output
- Support additional themes and slide templates
- Add tests for pipeline stages and API responses

## Author

Built by Nishant as a portfolio project focused on AI application development, full-stack integration, and local LLM workflows.
