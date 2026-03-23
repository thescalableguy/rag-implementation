# 🧠 Local RAG + Streaming Intelligence System

> A **local-first AI system** that combines Retrieval-Augmented Generation (RAG), streaming responses, and philosophical reasoning — built entirely on a laptop.

---

## 🚀 Overview

This project is an end-to-end **AI knowledge system** designed to:

* 📚 Answer questions using **custom PDFs (RAG)**
* ⚡ Stream responses in real-time (ChatGPT-like UX)
* 🕉️ Generate **daily philosophical contemplations**
* 🔒 Run **fully local (Ollama + FastAPI + React)**

No cloud dependencies. Full control over data and compute.

---

## 🧩 Architecture

```
PDFs → Embeddings → FAISS Index
        ↓
User Query → Retrieval → LLM (Ollama)
                     ↓
             Streaming Response → UI
```

---

## ⚙️ Tech Stack

### Backend

* FastAPI (Python)
* FAISS (Vector Search)
* Sentence Transformers (Embeddings)
* Ollama (Llama 3.2 - Local LLM)

### Frontend

* React + Vite
* Streaming Fetch API

### Integrations

* Discord Webhook (Daily Contemplations)

---

## 🔥 Key Features

### 1. 📚 Retrieval-Augmented Generation (RAG)

* Context-aware answers from your own PDFs
* Smart chunking + embedding pipeline
* Local vector database (FAISS)

---

### 2. ⚡ Streaming AI Responses

* Token-by-token streaming (like ChatGPT)
* Optimized for local inference
* Fault-tolerant fallback to non-stream mode

---

### 3. 🕉️ Daily Contemplation Engine

* AI-generated philosophy (Gita, Upanishads, Epics)
* Automatically sent to Discord
* Dynamic topic generation (no static prompts)

---

### 4. 🔒 Local-First AI System

* Runs entirely on laptop
* No external API dependency
* Full data privacy

---

### 5. 🧠 Prompt Engineering Layer

* Structured reasoning prompts
* Context grounding (no hallucination)
* Insight generation (not copy-paste)

---

### 6. 📊 Performance-Aware Design

* Batched embeddings for scalability
* Chunk limiting to prevent overload
* Streaming optimization for latency

---

## 🛠️ Setup

### 1. Clone Repo

```
git clone https://github.com/thescalableguy/rag-implementation.git
cd rag-implementation
```

---

### 2. Backend

```
pip install -r requirements.txt
uvicorn api.server:app --reload
```

---

### 3. Frontend

```
cd ui
npm install
npm run dev
```

---

### 4. Run Ollama

```
ollama serve
ollama run llama3.2
```

---

### 5. Ingest PDFs

```
python core/rag/ingest.py
```

---

## 🧪 Example Use Cases

* 📖 Ask: *"What is Dharma according to Bhagavad Gita?"*
* 🧠 Get: Context-grounded, explained answer
* ⚡ Delivered via streaming UI

---

## 🎯 Why This Project Stands Out

* Combines **LLMs + Systems Engineering + Performance Thinking**
* Demonstrates **local AI deployment (future trend)**
* Implements **real-world RAG pipeline**
* Focuses on **latency, scalability, and reliability**

---

## 🧠 Learnings

* RAG is primarily a **data + retrieval problem**, not just LLM usage
* Streaming systems require **careful state management**
* Local AI introduces **performance constraints → design trade-offs**

---

## 🚀 Future Enhancements

* Source-level citation (Perplexity-style)
* Memory layer (personalized responses)
* LLM observability (latency, tokens/sec)
* Krishna Mode (philosophy-driven reasoning engine)

---

## 👨‍💻 Author

**Sayan Bhattacharya**
Senior Performance Engineer | AI Systems Builder

> Building systems where **performance meets intelligence**

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to contribute!

---

