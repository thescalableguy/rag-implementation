from core.ollama_client import stream_ollama

def link_to_static(article: str) -> str:
    prompt = f"""
    Link this news to UPSC static syllabus topics.

    Article:
    {article}

    Output:
    - Static Topic
    - Related Concepts
    """

    return stream_ollama(prompt)
