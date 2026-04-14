# AI Incident Explainer — Key Concepts

## Project purpose
- A lightweight pipeline to convert incident logs into structured incident analysis using an LLM.
- Designed to explain incidents by generating summaries, root cause analysis, and remediation/recommendations.

## Architecture and flow
- `src/main.py`: entry point.
  - Loads incident data from `data/incident_logs.json`.
  - Iterates through incidents and calls `processor.process_incident` for each.
  - Saves results to `outputs/sample_run.json`.
- `src/processor.py`: core incident processing.
  - Builds the prompt using a system prompt and an incident-specific template.
  - Sends prompt to the LLM and returns a structured result.
  - Currently includes placeholder/dummy values for summary and root cause.
- `src/prompt_loader.py`: loads prompt assets.
  - `system_prompt.txt` contains the system-level instructions.
  - `incident_prompt_template.txt` contains the prompt structure for each incident.
- `src/llm_client.py`: handles LLM API interaction.
  - Uses Ollama local API at `http://localhost:11434/api/generate`.
  - Reads model config and LLM options from `config.yaml`.
  - Posts JSON payload and returns `response.json()["response"]`.
- `src/utils.py`: JSON file helpers.
  - `load_json()` reads JSON data.
  - `save_json()` appends JSON output to a file with indentation.

## Configuration
- `config.yaml` defines:
  - `model.provider`: ollama
  - `model.name`: llama3.1
  - `llm.temperature`: 0.2
  - `llm.max_tokens`: 150
  - `llm.max_output_tokens`: 1000
  - `output.save_results`: true

## Data and artifacts
- Input: `data/incident_logs.json`, plus sample inputs in `data/sample_inputs.txt`.
- Prompts: `prompts/system_prompt.txt`, `prompts/incident_prompt_template.txt`.
- Output: `outputs/sample_run.json`.

## Interview-relevant concepts
- Prompt engineering with separate system and incident template prompts.
- Local LLM integration via HTTP API and config-driven model selection.
- Simple ETL flow: load, process, save.
- Modular separation of concerns: entrypoint, prompt loader, processor, LLM client, utils.
- Current technical debt / improvement areas:
  - `processor.process_incident()` is placeholder logic.
  - `models.py` and `tests/test_processor.py` are empty.
  - `save_json()` appends output instead of overwriting, which may cause invalid JSON across runs.
  - Error handling is minimal outside LLM response status check.

## To Do
- Sequential evaluation of multiple models along with a leaderboard to compare performance and output quality.

## Potential discussion points
- How prompt structure influences LLM output quality.
- Why a system prompt is separated from incident-specific data.
- Using config files vs hardcoding model parameters.
- Tradeoffs of storing outputs as JSON and appending vs full rewrite.
- Extending the project with actual analysis extraction, schema validation, or unit tests.
