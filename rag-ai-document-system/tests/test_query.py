from embeddings.embedder import get_embedding
from vector_store.faiss_store import search

query = "Can contractors access VPN?"

vector = get_embedding(query)
results = search(vector)

print(results)
