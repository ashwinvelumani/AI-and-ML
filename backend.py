from flask import Flask, request, jsonify
import requests, os, json

app = Flask(__name__)

# Edit MODEL_NAME to the name you used when fine-tuning in Ollama
MODEL_NAME = os.environ.get('OLLAMA_MODEL','my-loan-model')
OLLAMA_API = os.environ.get('OLLAMA_API','http://localhost:11434')  # change if needed

def build_prompt(data):
    prompt = (f"Applicant: age={data.get('age')}, income={data.get('income')}, credit_score={data.get('credit_score')}, "
              f"loan_amount={data.get('loan_amount')}, existing_debt={data.get('existing_debt')}, "
              f"employment_years={data.get('employment_years')}, loan_purpose={data.get('loan_purpose')}.\n"
              "Question: Decide Approved or Rejected and give short Reason.")
    return prompt

@app.route('/predict', methods=['POST'])
def predict():
    req = request.get_json()
    if not req:
        return jsonify({'error':'send JSON body'}), 400
    prompt = build_prompt(req)

    # Example: calling Ollama local API - check your Ollama docs for the correct endpoint & payload
    try:
        payload = {"model": MODEL_NAME, "prompt": prompt, "max_tokens": 300}
        resp = requests.post(f"{OLLAMA_API}/api/generate", json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        # adapt parsing to your Ollama response format
        text = data.get('text') or data.get('output') or json.dumps(data)
        return jsonify({'prompt': prompt, 'response': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
