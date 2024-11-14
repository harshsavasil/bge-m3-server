from typing import List
from pydantic import BaseModel, Field
from enums.embedding_type import EmbeddingType

class EmbeddingRequest(BaseModel):
    sentences: List[str] = Field(
        title="The reranker sentences", max_length=8192, max_items=10
    )
    type: EmbeddingType | None