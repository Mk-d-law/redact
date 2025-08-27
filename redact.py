import pandas as pd
import json
from datafog import Detector, Redactor

detector = Detector()
redactor = Redactor()
def classify_records(input_file, output_file):
    df = pd.read_csv(input_file)
    results = []
    for _, row in df.iterrows():
        record_id = row["record_id"]
        data_json = row["data_json"]
        try:
            record = json.loads(data_json)
        except json.JSONDecodeError:
            results.append({
                "record_id": record_id,
                "redacted_data_json": "{}",
                "is_pii": False
            })
            continue
        text = json.dumps(record)
        findings = detector.detect(text)
        if not findings:
            is_pii = False
            redacted = record
        else:
            pii_types = {f["type"] for f in findings}
            redacted = json.loads(redactor.redact(text))
            if any(p in {"PHONE_NUMBER", "AADHAAR", "PASSPORT", "UPI"} for p in pii_types):
                is_pii = True
            elif any(p in {"EMAIL", "NAME", "ADDRESS", "IP_ADDRESS"} for p in pii_types) and len(pii_types) > 1:
                is_pii = True
            else:
                is_pii = False
        results.append({
            "record_id": record_id,
            "redacted_data_json": json.dumps(redacted),
            "is_pii": is_pii
        })
    pd.DataFrame(results).to_csv(output_file, index=False)
    print(f"Output saved to {output_file}")
if __name__ == "__main__":
    classify_records("iscp_pii_dataset.csv", "iscp_pii_output.csv")
