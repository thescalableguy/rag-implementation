from core.rag.retriever import retrieve
from core.ollama_client import stream_ollama


def rag_stream(question):
    context_chunks = retrieve(question)
    context = "\n\n".join(context_chunks)

    prompt = f"""
    Answer using ONLY the context below.

    Context:
    {context}

    Question:
    {question}

    Be clear and concise.
    """

    return stream_ollama(prompt)
