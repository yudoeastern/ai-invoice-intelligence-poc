import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"

def qwen_clean_text(text: str) -> str:
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an OCR text cleaner.\n"
                    "- Do NOT summarize\n"
                    "- Do NOT interpret\n"
                    "- Do NOT translate\n"
                    "- Fix spacing only\n"
                    "Return TEXT ONLY."
                )
            },
            {"role": "user", "content": text}
        ],
        "stream": False
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
    resp.raise_for_status()
    return resp.json()["message"]["content"]
