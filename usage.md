# Usage

1. Create a Python virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. Convert CSV to JSONL training data:
   ```
   python ollama_finetune.py --csv dataset/sample_loan_data.csv --out dataset/train.jsonl
   ```

3. Run Ollama fine-tune (example - adapt to your version):
   ```
   ollama fine-tune --base <base-model> --data dataset/train.jsonl --output my-loan-model
   ```

4. Start Flask backend:
   ```
   export OLLAMA_MODEL=my-loan-model
   export OLLAMA_API=http://localhost:11434
   python app/backend.py
   ```

5. Test prediction:
   ```bash
   curl -X POST http://localhost:9000/predict -H 'Content-Type: application/json' -d '{ "age":35, "income":45000, "credit_score":680, "loan_amount":15000, "existing_debt":2000, "employment_years":4, "loan_purpose":"car" }'
   ```
