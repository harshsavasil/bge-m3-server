from typing import List
from pydantic import BaseModel

class RerankerResponse(BaseModel):
    scores: List[float]