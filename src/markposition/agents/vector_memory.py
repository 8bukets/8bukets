import faiss
import numpy as np
import os
import json
from sentence_transformers import SentenceTransformer
from filelock import FileLock

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "data/vector_store")
MODEL_NAME = 'all-MiniLM-L6-v2'
LOCK_FILE = os.path.join(VECTOR_DB_PATH, "vector_memory.lock")

# Global model cache to prevent redundant loading
_model_cache = None

def get_model():
    global _model_cache
    if _model_cache is None:
        _model_cache = SentenceTransformer(MODEL_NAME)
    return _model_cache

class VectorMemory:
    def __init__(self):
        self.model = get_model()
        self.dimension = 384 # MiniLM-L6-v2 dimension
        self.index_file = os.path.join(VECTOR_DB_PATH, "index.faiss")
        self.meta_file = os.path.join(VECTOR_DB_PATH, "metadata.json")

        os.makedirs(VECTOR_DB_PATH, exist_ok=True)
        self.lock = FileLock(LOCK_FILE)

        self.index = None
        self.metadata = []

        # Initial load to setup state
        with self.lock:
            self._load_internal()

    def _load_internal(self):
        """Internal load without locking. Must be called within a lock context."""
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
            with open(self.meta_file, 'r') as f:
                self.metadata = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(self.dimension)
            self.metadata = []

    def _save_internal(self):
        """Internal save without locking. Must be called within a lock context."""
        faiss.write_index(self.index, self.index_file)
        with open(self.meta_file, 'w') as f:
            json.dump(self.metadata, f)

    def add_entry(self, text, meta):
        # Embedding can be done outside the lock to minimize hold time
        embedding = self.model.encode([text])
        with self.lock:
            # Reload to ensure we have the latest state before adding
            self._load_internal()
            self.index.add(np.array(embedding).astype('float32'))
            meta["text"] = text
            self.metadata.append(meta)
            self._save_internal()

    def search(self, query, top_k=5):
        # Embedding for query can be done outside the lock
        query_vector = self.model.encode([query])
        with self.lock:
            self._load_internal()
            if self.index.ntotal == 0:
                return []

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
        """Public save method with locking."""
        with self.lock:
            self._save_internal()
