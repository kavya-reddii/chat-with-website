import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch

class EmbeddingStore:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.vector_dimension = self.model.config.hidden_size
        self.index = faiss.IndexFlatL2(self.vector_dimension)
        self.text_chunks = []

    def embed_text(self, texts):
        tokens = self.tokenizer(texts, padding=True, truncation=True, return_tensors="pt").to(self.device)
        with torch.no_grad():
            embeddings = self.model(**tokens).last_hidden_state.mean(dim=1)
        return embeddings.cpu().numpy()

    def add_texts(self, texts):
        vectors = self.embed_text(texts)
        self.index.add(vectors)
        self.text_chunks.extend(texts)

    def search(self, query, top_k=3):
        query_vector = self.embed_text([query]).reshape(1, -1)
        _, indices = self.index.search(query_vector, top_k)
        return [self.text_chunks[i] for i in indices[0]]
