# Loan Eligibility Assistant (Ollama Fine-tune)

This project scaffold helps you fine-tune an Ollama model for a Loan Eligibility Assistant and run a small Flask API that queries the fine-tuned model.

## Contents
- `dataset/sample_loan_data.csv` — small example dataset for fine-tuning and testing.
- `fine_tune_ollama.md` — step-by-step instructions to prepare data and fine-tune using Ollama.
- `ollama_finetune.py` — helper script to format dataset into training examples and call Ollama CLI (example).
- `app/backend.py` — simple Flask API that sends prompts to the Ollama model and returns responses.
- `utils/preprocessing.py` — basic preprocessing utilities for the dataset.
- `prompts/prompt_templates.json` — prompt templates for training and inference.
- `requirements.txt` — Python dependencies for the project.
- `docs/usage.md` — how to run the app locally and test endpoints.

## Notes
- This scaffold assumes you have Ollama installed and running locally (refer to Ollama docs).
- Edit model names/paths in `ollama_finetune.py` and `app/backend.py` to match your environment.
