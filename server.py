from typing import List, Tuple
from FlagEmbedding import BGEM3FlagModel
from fastapi import FastAPI
import uvicorn
import os

from enums.embedding_type import EmbeddingType
from schemas.embedding_response import EmbeddingResponse
from schemas.embedding_request import EmbeddingRequest
from schemas.reranker_request import RerankerRequest
from schemas.reranker_response import RerankerResponse

# gpu batch_size in order of your available vram
batch_size = 12 if os.getenv('BGE_M3_BATCH_SIZE') == "" or os.getenv('BGE_M3_BATCH_SIZE') == None else int(os.getenv('BGE_M3_BATCH_SIZE'))
# max context length for embeddings and passages in re-ranker
max_length = 8192 if os.getenv('BGE_M3_MAX_LENGTH') == "" or os.getenv('BGE_M3_MAX_LENGTH') == None else int(os.getenv('BGE_M3_MAX_LENGTH'))
# max context length for questions in re-ranker
max_query_length = 512 if os.getenv('BGE_M3_MAX_QUERY_LENGTH') == "" or os.getenv('BGE_M3_MAX_QUERY_LENGTH') == None else int(os.getenv('BGE_M3_MAX_QUERY_LENGTH'))
# re-rank score weights
rerank_weights = [0.4, 0.2, 0.4] if os.getenv('BGE_M3_RERANKER_WEIGHTS') == "" or os.getenv('BGE_M3_RERANKER_WEIGHTS') == None else [float(x) for x in os.getenv('BGE_M3_RERANKER_WEIGHTS').split(",")]
model_name = 'BAAI/bge-m3' if os.getenv('BGE_M3_MODEL_NAME') == "" or os.getenv('BGE_M3_MODEL_NAME') == None else os.getenv('BGE_M3_MODEL_NAME')



class FlagEmbeddingModelRunner:
    def __init__(self, model_name: str):
        self.model = BGEM3FlagModel(model_name, use_fp16=True)

    def embedding(self, sentences: List[str], type: EmbeddingType) -> EmbeddingResponse:
        if type == EmbeddingType.hybrid:
            embeddings = self.model.encode(
                sentences,
                batch_size=batch_size,
                max_length=max_length,
                return_dense=True,
                return_sparse=True,
                return_colbert_vecs=False,
            )
        else:
            embeddings = self.model.encode(
                sentences,
                batch_size=batch_size,
                max_length=max_length,
                return_dense=True if type == None or type == EmbeddingType.dense else False,
                return_sparse=True if type == EmbeddingType.sparse else False,
                return_colbert_vecs=True if type == EmbeddingType.colbert else False,
            )
        if type == EmbeddingType.hybrid:
            dense_embedding = embeddings['dense_vecs'].tolist() if embeddings['dense_vecs'] is not None else []
            sparse_embedding = [dict(embedding) for embedding in embeddings.get('lexical_weights', [])]
            return { "dense_embedding": dense_embedding, "sparse_embedding": sparse_embedding }
        elif type == EmbeddingType.dense:
            dense_embedding = embeddings['dense_vecs'].tolist() if embeddings['dense_vecs'] is not None else []
            return { "dense_embedding": dense_embedding }
        elif type == EmbeddingType.sparse:
            sparse_embedding = [dict(embedding) for embedding in embeddings.get('lexical_weights', [])]
            return { "sparse_embedding": sparse_embedding }
        else: # colbert
            vectors = embeddings.get('colbert_vecs', [])[0] if len(embeddings.get('colbert_vecs', [])) > 0 else []
            colbert_embedding = [embedding.tolist() for embedding in vectors]
            return { "colbert_embedding": colbert_embedding }

    def reranker(self, sentences: List[Tuple[str, str]]) -> List[float]:
        scores = self.model.compute_score(
            sentences,
            batch_size=batch_size,
            max_query_length=max_query_length,
            max_passage_length=max_length,
            weights_for_different_modes=rerank_weights,
        )
        return scores['colbert+sparse+dense']


model = FlagEmbeddingModelRunner(model_name)


app = FastAPI()


@app.post("/embedding", response_model=EmbeddingResponse)
async def get_embeddings(request: EmbeddingRequest):
    return EmbeddingResponse(**model.embedding(request.sentences, request.type))


@app.post("/reranker", response_model=RerankerResponse)
async def rerank(request: RerankerRequest):
    sentence_pars = []
    for s in request.sentences:
        sentence_pars.append([request.target, s])
    return RerankerResponse(scores=model.reranker(sentence_pars))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)