# Agentic AI Training Repository

This repository provides a structured environment for students to explore agentic behaviors in modern generative AI systems. The primary learning resources are a curated set of Jupyter notebooks supported by lightweight datasets and scripts.

## Repository Layout

```
notebooks/
  01_introduction.ipynb           # Overview of goals and environment checks
  02_function_calling_basics.ipynb # Function calling workflows and mock tooling
  03_model_context_protocol.ipynb # Sharing context through the Model Context Protocol
  04_agent_to_agent_protocol.ipynb # Collaboration patterns between agents

data/
  agent_sessions.csv              # Sample transcript fragments for analysis exercises

scripts/
  generate_mock_data.py           # Utility for creating additional mock session data
```

## Getting Started

1. Export your OpenAI API token as `OPENAI_API_KEY` (or have it ready to provide when prompted).
2. Launch your preferred Jupyter environment (e.g., VS Code, JupyterLab, or `jupyter notebook`).
3. Begin with `notebooks/01_introduction.ipynb` and work through the sequence.
4. Use the CSV data and helper script as optional extensions for hands-on experiments.

## Extending the Materials

- Add new notebooks to cover advanced scenarios such as tool orchestration or evaluation pipelines.
- Capture real or simulated agent transcripts in the `data/` directory to ground the exercises.
- Enhance `generate_mock_data.py` with richer sampling strategies or integrations with external APIs.

Contributions and iterations are encouraged to adapt the curriculum to different classroom settings.
