from enum import Enum

class EmbeddingType(Enum):
    dense = 'dense'
    sparse = 'sparse'
    colbert = 'colbert'
    hybrid = 'hybrid'