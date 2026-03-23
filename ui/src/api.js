const BASE_URL = "/api";
const API_KEY = "";

export const api = {
  // 🔥 RAG Streaming
  ragStream: async (question, onChunk) => {
    const res = await fetch(
      `/api/rag-stream?question=${encodeURIComponent(question)}`
    );

    if (!res.ok || !res.body) {
      console.error("API failed:", res.status);
      return;
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();

    let fullText = "";

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value, { stream: true });

      if (chunk) {
        fullText += chunk;
        console.log("Streaming:", fullText); // 🔍 DEBUG
        onChunk(fullText);
      }
    }
  },

  // 🚀 Pipeline trigger (Discord)
  pipeline: async () => {
    const res = await fetch("/api/run-pipeline");

    if (!res.ok) {
      console.error("Pipeline failed");
      return;
    }

    return res.json();
  }
};

export const streamAnswer = async (question, onChunk) => {
  const res = await fetch(`/api/stream-answer?question=${encodeURIComponent(question)}`, {
    headers: {
        "x-api-key": API_KEY
      }
  });

  if (!res.body) return;

  const reader = res.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
    const { value, done } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value);
    if (chunk) onChunk(chunk);
  }
};