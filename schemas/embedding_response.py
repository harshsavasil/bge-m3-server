from typing import List, Dict, Optional
from pydantic import BaseModel

class EmbeddingResponse(BaseModel):
    dense_embedding: Optional[List[List[float]]] = None
    sparse_embedding: Optional[List[Dict[int, float]]] = None
    colbert_embedding: Optional[List[List[float]]] = None