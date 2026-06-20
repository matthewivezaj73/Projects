from pipelines.ingest_documents import ingest_documents
from pipelines.chunker import chunk_text
from pipelines.metadata_extractor import extract_metadata
from embeddings.embedder import get_embedding
from vector_store.faiss_store import add_vector

def build_index():
    docs = ingest_documents()

    for doc in docs:
        chunks = chunk_text(doc["text"])

        for chunk in chunks:
            embedding = get_embedding(chunk)

            metadata = extract_metadata(
                doc["file_name"],
                doc["file_path"],
                chunk
            )

            metadata["text"] = chunk

            add_vector(embedding, metadata)
