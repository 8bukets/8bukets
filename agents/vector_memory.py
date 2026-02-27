import faiss
import numpy as np
import os
import json
from sentence_transformers import SentenceTransformer

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "data/vector_store")
MODEL_NAME = 'all-MiniLM-L6-v2'

class VectorMemory:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)
        self.dimension = 384 # MiniLM-L6-v2 dimension
        self.index_file = os.path.join(VECTOR_DB_PATH, "index.faiss")
        self.meta_file = os.path.join(VECTOR_DB_PATH, "metadata.json")

        os.makedirs(VECTOR_DB_PATH, exist_ok=True)

        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
            with open(self.meta_file, 'r') as f:
                self.metadata = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(self.dimension)
            self.metadata = []

    def add_entry(self, text, meta):
        embedding = self.model.encode([text])
        self.index.add(np.array(embedding).astype('float32'))
        meta["text"] = text
        self.metadata.append(meta)
        self.save()

    def search(self, query, top_k=5):
        if self.index.ntotal == 0:
            return []

        query_vector = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vector).astype('float32'), top_k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1 and idx < len(self.metadata):
                results.append({
                    "metadata": self.metadata[idx],
                    "distance": float(distances[0][i])
                })
        return results

    def save(self):
        faiss.write_index(self.index, self.index_file)
        with open(self.meta_file, 'w') as f:
            json.dump(self.metadata, f)
