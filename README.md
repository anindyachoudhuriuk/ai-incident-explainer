ai-incident-explainer/
│
├── README.md
├── requirements.txt
├── .gitignore
├── config.yaml
│
├── data/
│   ├── incident_logs.json
│   ├── sample_inputs.txt
│
├── prompts/
│   ├── system_prompt.txt
│   ├── incident_prompt_template.txt
│
├── src/
│   ├── main.py
│   ├── llm_client.py
│   ├── prompt_loader.py
│   ├── processor.py
│   ├── models.py
│   ├── utils.py
│
├── tests/
│   ├── test_processor.py
│
├── outputs/
│   ├── sample_run.json

## Project Overview

`ai-incident-explainer` is a lightweight incident explanation prototype that reads incident logs, invokes an LLM to generate structured JSON analysis, and writes results to `outputs/sample_run.json`.

## File Details

### `README.md`
- Project documentation and structure overview.
- Describes inputs, outputs, and how the repository is organized.

### `requirements.txt`
- Python dependency manifest for the project.
- Install dependencies for running the tool and tests.

### `.gitignore`
- Files and folders excluded from version control.
- Typically ignores Python caches, local environment files, and output artifacts.

### `config.yaml`
- Central configuration for the LLM and model settings.
- Defines model name, temperature, and token limits.

## Data

### `data/incident_logs.json`
- Sample incident log input used by the application.
- Contains incident records with `id`, `system`, `error`, `severity`, `timestamp`, and `context`.

### `data/sample_inputs.txt`
- Example raw input lines or notes for incident ingestion.
- Useful as a reference for expected input format.

## Prompts

### `prompts/system_prompt.txt`
- System prompt sent to the LLM.
- Instructs the model to return strict JSON using the expected schema.

### `prompts/incident_prompt_template.txt`
- Incident prompt template used to format each incident for the LLM.
- Inserts incident fields like system, error, and context into the prompt.

## Source Code

### `src/main.py`
- Application entry point.
- Loads incidents, processes them via `processor.py`, and saves results to `outputs/sample_run.json`.

### `src/llm_client.py`
- Sends prompts to the configured LLM endpoint.
- Handles HTTP requests and checks for response errors.

### `src/prompt_loader.py`
- Loads prompt templates and system prompt text from disk.

### `src/processor.py`
- Core processing logic for each incident.
- Builds the prompt, calls the LLM, parses JSON output, and extracts analysis fields.

### `src/models.py`
- Project data models and schema definitions.
- Can be used to define structured types for incidents and analysis output.

### `src/utils.py`
- Utility helpers for JSON loading and saving.
- Common file operations used across the codebase.

## Tests

### `tests/test_processor.py`
- Placeholder for processor unit tests.
- Should validate prompt construction, response parsing, and error handling.

## Outputs

### `outputs/sample_run.json`
- Example output produced by the application.
- Stores the parsed incident explanations and root cause analysis.

## Architecture Plan

A high-level incident processing pipeline is defined in `PLAN.md`.

```text
Live Logs
   ↓
Kafka Stream
   ↓
Sliding Window Engine
   ↓
Incident Detection
   ↓
LLM Reasoning Layer
        ↑
        │
   RAG Context Layer (optional enrichment)
        │
   Runbooks + Docs + Incident History
   ↓
Agent Decision Layer
   ↓
Actions
   ↓
Feedback Loop
```

