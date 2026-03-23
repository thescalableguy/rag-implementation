from core.ollama_client import stream_ollama

def generate_mythology_insight(topic: str) -> str:
    prompt = f"""
    Provide a deep philosophical insight on:

    {topic}

    Include:
    - Story/context
    - Key teaching
    - Interpretation
    - Real life application
    """

    return stream_ollama(prompt)
