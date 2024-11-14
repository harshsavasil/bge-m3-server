from typing import List
from pydantic import BaseModel, Field

class RerankerRequest(BaseModel):
    target: str = Field(
        title="The reranker target string", max_length=8192
    )
    sentences: List[str] = Field(
        title="The reranker sentences", max_length=8192, max_items=10
    )