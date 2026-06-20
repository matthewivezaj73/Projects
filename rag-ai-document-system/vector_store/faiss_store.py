import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)

store = []

def add_vector(embedding, metadata):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    store.append(metadata)

def search(query_vector, k=3):
    vector = np.array([query_vector]).astype("float32")
    distances, indices = index.search(vector, k)

    results = [store[i] for i in indices[0]]
    return results
