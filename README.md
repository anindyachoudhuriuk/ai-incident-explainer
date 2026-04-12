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
└── outputs/
    ├── sample_run.json