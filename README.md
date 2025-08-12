# Enterprise RAG Chatbot

**Status:** In development / internal testing  
**Owner:** Applied AI  
**Tech:** Python, retrieval middleware, embeddings, vector store (pluggable: FAISS/pgvector/Qdrant/Chroma), HTTP API, logging/telemetry, CI

## 1) What this is
A **Retrieval-Augmented Generation** chatbot that consumes the **KBMS** corpus (15 apps, 2k+ docs) and returns **cited, grounded** answers. Includes evaluation prompts, groundedness checks, a **no-answer** fallback, and usage logging. **Not yet in production; metrics pending.**

## 2) Architecture

```
KBMS Packs ──▶ Ingestion ▶ Cleaning ▶ Chunking ▶ Embeddings ──▶ Vector DB
                                                    ▲
                                                    │
                                           Retriever + Filters
                                                    │
User ▶ /chat ───────────────────────────▶ LLM with Response Templates
                                 ◀─────── Citations + No-Answer fallback
```

## 3) Repository Layout

```
rag-chatbot/
  README.md
  pyproject.toml / requirements.txt
  src/
    rag/
      ingest/
        from_kbms_pack.py
        enrich_metadata.py
      index/
        embed.py                 # pluggable model/provider
        vector_store.py          # driver abstraction
      retrieval/
        retriever.py
        filters.py
      llm/
        templates/
          answer.md.j2
          no_answer.md.j2
        generate.py
      eval/
        harness.py
        datasets/
          internal_qa.yml
          assertions.yml
      api/
        server.py                # FastAPI/Flask
      utils/
        logging.py
        config.py
  configs/
    vector_store.yml
    embedder.yml
    retriever.yml
  tests/
  .env.example
  Dockerfile
  Makefile
```

## 4) Configuration

`.env.example`:
```
ENV=dev
DATA_ROOT=../kbms/content
PACKS_GLOB=../kbms/content/*/*/meta/pack.json

# Embeddings (choose one provider)
EMBED_MODEL_PROVIDER=openai|azure|local
EMBED_MODEL_NAME=<model-name>
EMBED_API_KEY=...

# Vector store (choose one)
VECTOR_STORE=faiss|pgvector|qdrant|chroma
PG_DSN=postgresql://user:pass@host:5432/db
QDRANT_URL=http://localhost:6333

# Serving
HOST=0.0.0.0
PORT=8000
MAX_CONTEXT_TOKENS=4000

# Safety / Governance
NO_ANSWER_THRESHOLD=0.35
CITATION_MIN_COUNT=2
LOG_TO=stdout
```

`configs/retriever.yml`:
```yaml
k: 6
hybrid: true         # bm25 + dense
rerank: none         # or 'cross-encoder'
filters:
  - field: app
    include: ["okta","jira","servicenow"]
```

## 5) Quickstart

**Local:**
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env && edit .env
make index        # builds embeddings + vector index from KBMS packs
make serve        # starts API on :8000
```

**Docker:**
```bash
docker build -t rag:latest .
docker run --env-file .env -p 8000:8000 -v $PWD:/app rag:latest make index serve
```

## 6) API

- `GET /health` → `{status:"ok"}`
- `POST /reindex` → rebuild from `PACKS_GLOB`
- `POST /chat`
  ```json
  {
    "query": "How do I reset an Okta MFA token?",
    "filters": {"app":["okta"]},
    "session_id": "abc123"
  }
  ```
  **Response (example):**
  ```json
  {
    "answer": "To reset an Okta MFA token, ...",
    "citations": [
      {"title":"Reset MFA Token (Okta)","doc_id":"sha256:...","url":"..."}
    ],
    "meta":{"latency_ms": 812}
  }
  ```

## 7) Evaluation & Quality

**Datasets:**
- `eval/datasets/internal_qa.yml` — Q/A pairs derived from SOPs
- `eval/datasets/assertions.yml` — per-app must-include terms

**Metrics (reported to stdout or CSV):**
- **Groundedness** (source-overlap)
- **Citation coverage** (≥2 required)
- **No-answer precision** (avoid hallucinations)
- **Latency p50/p95**

Run:
```bash
make eval
python -m rag.eval.harness --dataset eval/datasets/internal_qa.yml --limit 100
```

## 8) Safety & Guardrails

- **No-answer fallback** if confidence < `NO_ANSWER_THRESHOLD`
- **Citations required**; failure → safe template
- **PII filters** (simple regex) before return
- **Prompt versioning** (`llm/templates/` with semver in comments)

## 9) Logging & Telemetry

- Request/response with hashed session IDs
- Indexing logs with doc counts and durations
- Optional export to CSV for weekly QA

## 10) Limitations / Roadmap

- Internal testing only; **no production SLOs yet**
- Add cross-encoder reranking
- Add per-tenant filtering and access control
- Live eval dashboard + regression alerts
