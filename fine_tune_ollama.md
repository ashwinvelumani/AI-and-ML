# Fine-tuning with Ollama (example workflow)

**Prerequisites**
- Ollama installed and running locally: follow Ollama's official docs.
- A base model available in Ollama (e.g., `llama2`, `mistral`, or any local model you have).
- Python 3.8+

**1) Prepare your dataset**
- Use `dataset/sample_loan_data.csv` as a schema example. For instruction tuning / supervised fine-tuning, create JSONL records with `input` and `output` fields (or the format your Ollama fine-tune expects).

Example JSONL entry (instruction/response style):
```json
{"input":"Applicant: {age: 35, income: 45000, credit_score: 680, loan_amount: 15000, employment_years: 4}\nQuestion: Should the applicant be approved for a loan?","output":"Approved — Reason: credit score and income are adequate, debt-to-income ratio acceptable."}
```

**2) Convert CSV -> JSONL**
- Use `ollama_finetune.py` included in this repo to convert CSV to JSONL training examples.

**3) Fine-tune with Ollama**
- Ollama's fine-tuning CLI varies with releases. A typical flow:
  1. `ollama pull <base_model>` (if needed)
  2. `ollama fine-tune --base <base_model> --data train.jsonl --output my-loan-model`
- Replace flags with the exact options of your Ollama version. Check `ollama --help` or docs.

**4) Validate & iterate**
- Use a validation set and human review. Ensure the model's explanations are factual and don't invent specifics.

**5) Run app**
- Start the Flask app: `python app/backend.py`
- Query `POST /predict` with applicant JSON.

