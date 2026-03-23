import os
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# 🔹 Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 🔹 Config
CHUNK_SIZE = 1500
MAX_CHUNKS = 5000   # 🔥 prevents overload


# 🔹 Extract text safely
def load_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text


# 🔹 Smart chunking (paragraph-based)
def chunk_text(text):
    paragraphs = text.split("\n")

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk) + len(para) < CHUNK_SIZE:
            current_chunk += para + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


# 🔹 Main ingestion
def ingest_pdfs(folder="data"):
    print("🚀 Starting ingestion...")
    print("📂 Looking in folder:", folder)

    if not os.path.exists(folder):
        print("❌ Folder not found")
        return

    files = os.listdir(folder)
    print("📄 Files found:", files)

    all_chunks = []

    for file in files:
        if file.endswith(".pdf"):
            print(f"\n📘 Processing: {file}")

            path = os.path.join(folder, file)
            text = load_pdf_text(path)

            print("📏 Text length:", len(text))

            if len(text) == 0:
                print("⚠️ Skipping empty PDF")
                continue

            chunks = chunk_text(text)
            print("🧩 Chunks created:", len(chunks))

            all_chunks.extend(chunks)

    if len(all_chunks) == 0:
        print("❌ No chunks created. Stopping.")
        return

    # 🔥 LIMIT chunks (critical)
    print("\n⚡ Limiting chunks to:", MAX_CHUNKS)
    all_chunks = all_chunks[:MAX_CHUNKS]

    print("🚀 Final chunks count:", len(all_chunks))

    # 🔹 Generate embeddings (batched)
    print("\n🧠 Generating embeddings...")
    embeddings = model.encode(
        all_chunks,
        batch_size=32,
        show_progress_bar=True
    )

    print("✅ Embeddings generated")

    # 🔹 Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    print("💾 Saving index...")

    faiss.write_index(index, "vector.index")

    with open("chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)

    print("✅ Ingestion complete")


# 🔹 Entry point
if __name__ == "__main__":
    print("🚀 Starting Ingestion...")
    ingest_pdfs()
