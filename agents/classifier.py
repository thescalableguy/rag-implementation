from core.ollama_client import stream_ollama

def analyze_mythology(topic: str) -> str:
    prompt = f"""
    Analyze the following Indian mythology topic:

    {topic}

    Provide:
    1. Source (Vedas / Upanishads / Ramayana / Mahabharata / Puranas)
    2. Core concept explanation
    3. Philosophical meaning
    4. Modern relevance
    """

    return stream_ollama(prompt)
