import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector.index")

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def retrieve(query, top_k=5):
    query_embedding = model.encode([query])

    distances, indices = index.search(query_embedding, top_k)

    results = [chunks[i] for i in indices[0]]

    return results
    