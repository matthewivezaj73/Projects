from fastapi import FastAPI
from embeddings.embedder import get_embedding
from vector_store.faiss_store import search

app = FastAPI()

@app.post("/ask")
def ask(question: str):
    query_vector = get_embedding(question)
    results = search(query_vector)

    context = "\n".join([r["text"] for r in results])

    prompt = f"""
    Answer ONLY using context below.

    Context:
    {context}

    Question:
    {question}
    """

    return {
        "context_used": context,
        "answer_prompt": prompt
    }
