from fastapi import FastAPI, Query, Depends
from agents.scraper import get_mythology_topics
from agents.classifier import analyze_mythology
from agents.linker import link_to_static
from agents.answer_writer import generate_mythology_insight
from agents.revision import generate_flashcards
from core.orchestrator import run_daily_contemplation
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from core.ollama_client import stream_ollama
from agents.gita import get_random_shloka
from api.security import security_middleware
from api.security import verify_api_key
from core.rag.rag_pipeline import rag_stream
import json


app = FastAPI()

app = FastAPI(title="Mythology Research Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(security_middleware)


# -----------------------------------
# Health Check
# -----------------------------------
@app.get("/")
def root():
    return {"message": "Mythology Research Running 🚀"}

@app.get("/stream-answer")
def stream_answer(question: str, _: None = Depends(verify_api_key)):

    def generator():
        for chunk in stream_ollama(question):
            try:
                data = json.loads(chunk)

                # ONLY send actual text
                if "response" in data:
                    yield data["response"]
            except:
                continue

    return StreamingResponse(generator(), media_type="text/plain")

@app.get("/rag-stream")
def rag_stream_endpoint(question: str):

    def generator():
        for chunk in rag_stream(question):
            if not chunk:
                continue

            try:
                # 🔥 chunk is raw bytes or string JSON from Ollama
                if isinstance(chunk, bytes):
                    chunk = chunk.decode("utf-8")

                data = json.loads(chunk)

                # ✅ ONLY send actual text
                if "response" in data:
                    yield data["response"]

                # ✅ stop when done
                if data.get("done"):
                    break

            except:
                continue

    return StreamingResponse(generator(), media_type="text/plain")

# -----------------------------------
# Raw News
# -----------------------------------
@app.get("/news")
def fetch_news():
    news = get_mythology_topics()
    return {"news": news}

@app.get("/daily-shloka")
def daily_shloka():
    return get_random_shloka()


# -----------------------------------
# Classified News
# -----------------------------------
@app.get("/classified-news")
def classified_news():
    news_list = get_mythology_topics()

    result = []
    for news in news_list:
        category = analyze_mythology(news)
        result.append({
            "news": news,
            "category": category
        })

    return {"data": result}


# -----------------------------------
# Linked News (Static Mapping)
# -----------------------------------
@app.get("/linked-news")
def linked_news():
    news_list = get_mythology_topics()

    result = []
    for news in news_list:
        linkage = link_to_static(news)
        result.append({
            "news": news,
            "linkage": linkage
        })

    return {"data": result}


# -----------------------------------
# Answer Writing
# -----------------------------------
@app.get("/answer")
def answer(question: str = Query(..., description="Dharma in Mahabharata")):
    response = generate_mythology_insight(question)
    return {
        "question": question,
        "answer": response
    }


# -----------------------------------
# Flashcards (Revision)
# -----------------------------------
@app.get("/flashcards")
def flashcards(content: str = Query(...)):
    cards = generate_flashcards(content)
    return {
        "input": content,
        "flashcards": cards
    }


# -----------------------------------
# Full Pipeline Trigger
# -----------------------------------
@app.get("/run-pipeline")
def trigger_daily_contemplation():
    run_daily_contemplation()
    return {"status": "Pipeline executed and sent to Discord"}
