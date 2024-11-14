# BGE-M3 FASTAPI Server
This server can be used for deploy bge-m3 embedding models as REST APIs.

Embedding type can be `hybrid`, `dense`, `sparse` and `colber`.

```
curl -X POST -k -v http://127.0.0.1:3000/embedding -H "Content-Type: application/json" -d '{"sentences":["xx"], "type":"dense"}'
```
```
curl -X POST -k -v http://127.0.0.1:3000/reranker -H "Content-Type: application/json" -d '{"target": "What is BGE M3?","sentences":["BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.", "xxx"], "type":"dense"}'
```