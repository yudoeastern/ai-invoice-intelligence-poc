import requests, json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"

def extract_invoice_semantic(text: str) -> dict:
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Extract RAW invoice tokens.\n"
                    "- NEVER infer\n"
                    "- NEVER calculate\n"
                    "- If multiple values exist, return ALL\n"
                    "- Numbers = digits only\n"
                    "- Return VALID JSON ONLY"
                )
            },
            {
                "role": "user",
                "content": f"""
TEXT:
{text}

Return JSON:
{{
  "vendor_name_candidates": [],
  "invoice_number_candidates": [],
  "invoice_date_candidates": [],
  "total_candidates": [],
  "payment_amount_candidates": [],
  "admin_fee_candidates": []
}}
"""
            }
        ],
        "stream": False
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
    resp.raise_for_status()
    return json.loads(resp.json()["message"]["content"])


def extract_amounts(text: str) -> dict:
    payload = {
        "model": MODEL,
        "options": {
            "temperature": 0,      # 🔒 PENTING
            "top_p": 0.1
        },
        "messages": [
            {
                "role": "system",
                "content": (
                    "Extract monetary values ONLY.\n"
                    "- DO NOT extract vendor\n"
                    "- DO NOT extract invoice number\n"
                    "- DO NOT extract date\n"
                    "- Numbers only\n"
                    "- Return JSON ONLY"
                )
            },
            {
                "role": "user",
                "content": f"""
TEXT:
{text}

Return JSON:
{{
  "total": null,
  "admin_fee": null,
  "down_payment": null,
  "balance_due": null
}}
"""
            }
        ],
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload, timeout=120)
    r.raise_for_status()
    return json.loads(r.json()["message"]["content"])
