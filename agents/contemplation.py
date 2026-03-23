from core.ollama_client import query_ollama


def generate_contemplation():
    prompt = """
    Generate a daily contemplation from Indian philosophy.

    Output format:

    Topic: <short topic>

    Thought:
    <150 words reflection>

    Rules:
    - Based on Gita / Upanishads / Epics
    - Deep but simple
    - End with a question
    """

    response = query_ollama(prompt)

    # Simple parsing
    try:
        topic = response.split("Topic:")[1].split("Thought:")[0].strip()
        thought = response.split("Thought:")[1].strip()
    except:
        topic = "Daily Reflection"
        thought = response

    return topic, thought
