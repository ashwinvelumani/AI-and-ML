"""Helper to convert CSV to JSONL training examples for Ollama-style instruction tuning.        Edit this script to match the exact JSONL format required by your Ollama version."""
import csv, json, argparse

def row_to_example(row):
    # Customize how a CSV row becomes an instruction->response pair
    inp = (f"Applicant: age={row['age']}, income={row['income']}, credit_score={row['credit_score']}, "
           f"loan_amount={row['loan_amount']}, existing_debt={row.get('existing_debt','')}, "
           f"employment_years={row.get('employment_years','')}, loan_purpose={row.get('loan_purpose','')}.\n"
           "Question: Should the applicant be approved for a loan?")
    # Use the CSV label if present, otherwise leave placeholder
    label = row.get('decision','Approved' if int(row.get('credit_score',0))>650 else 'Rejected')
    out = f"Decision: {label}. Reason: Provide a short justification based on the features."
    return {'input': inp, 'output': out}

def csv_to_jsonl(csv_path, jsonl_path):
    with open(csv_path, 'r', newline='', encoding='utf-8') as f_in, open(jsonl_path, 'w', encoding='utf-8') as f_out:
        reader = csv.DictReader(f_in)
        for r in reader:
            ex = row_to_example(r)
            f_out.write(json.dumps(ex, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', default='dataset/sample_loan_data.csv')
    parser.add_argument('--out', default='dataset/train.jsonl')
    args = parser.parse_args()
    csv_to_jsonl(args.csv, args.out)
    print('Wrote', args.out)
