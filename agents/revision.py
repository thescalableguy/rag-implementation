from core.ollama_client import stream_ollama

def generate_flashcards(content: str) -> str:
    prompt = f"""
    Convert the following into flashcards:

    {content}

    Format:
    Q:
    A:
    """

    return stream_ollama(prompt)
