import requests
from config.settings import OLLAMA_URL, OLLAMA_MODEL

def stream_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            try:
                data = line.decode("utf-8")
                yield data
            except:
                continue

def query_ollama(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        if response.status_code != 200:
            raise Exception(f"Ollama error: {response.status_code}")

        data = response.json()

        # ✅ Extract response safely
        return data.get("response", "").strip()

    except Exception as e:
        print("❌ Ollama query failed:", e)
        return "Error generating response from model."
