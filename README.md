# **Enterprise RAG Chatbot**

> Private, high-accuracy Retrieval-Augmented Generation for enterprise knowledge — self-hosted, observable, and safe.

## 🚀 Overview

The **Enterprise RAG Chatbot** is a **self-hosted, Dockerized** RAG system for answering organization-specific questions from your internal documentation. Designed for **IT/support** and **knowledge-heavy teams**, it returns **cited answers**, enforces **guardrails**, and ships with **observability + evaluation**.

---

## ✨ Key Features

* **Agentic pipeline:** retrieve → (optional) rerank → synthesize → guard → cite.
* **Self-hosted stack with Docker Compose** (vector DB, memory, tracing, local LLM).
* **Switchable Level 2 (LLM):** **local** (vLLM / LM Studio / Ollama) **or** **OpenRouter**.
* **Observability:** Langfuse or Arize Phoenix tracing; cost/latency tracking.
* **Evaluation:** Nightly **Ragas** for faithfulness, correctness, precision/recall.

---

## 🧩 Tech Stack (Levels 0–8)

| Level                   | Purpose                 | Tools                                                  |
| ----------------------- | ----------------------- | ------------------------------------------------------ |
| **8 – Alignment**       | Governance & guardrails | Guardrails AI, Langfuse, Arize Phoenix                 |
| **7 – Memory**          | Role-based persistence  | Zep, Mem0                                              |
| **6 – Data Extraction** | Parse web/docs          | Firecrawl, Docling, LlamaParse                         |
| **5 – Embedding**       | Vector encoding         | OpenAI, Voyage, Nomic                                  |
| **4 – Vector DB**       | Store/query             | Weaviate (default), Milvus, Pinecone, Chroma (dev)     |
| **3 – Framework**       | Orchestration           | LangChain / LangGraph-style                            |
| **2 – LLMs**            | Response generation     | **Local:** vLLM/LM Studio/Ollama • **API:** OpenRouter |
| **1 – Evaluation**      | Quality checks          | Ragas (optional: DeepEval, LangSmith)                  |
| **0 – Deployment**      | Hosting/scaling         | **Docker Compose** / K8s-ready manifests               |

---

## 🏗 Architecture

```mermaid
graph TD
    A[User Query] --> B[Intent & Preprocess]
    B --> C[Retriever: Vector DB + Filters]
    C --> D[Reranker (optional)]
    D --> E[LLM Synthesis (Local or OpenRouter)]
    E --> F[Guardrails (must-cite, PII, policy)]
    F --> G[Answer + Citations]
    G --> H[Tracing & Evals (Langfuse/Phoenix + Ragas)]
```

---

## ⚙️ Quickstart (Docker)

### 1) Clone & env

```bash
git clone https://github.com/your-org/enterprise-rag-chatbot.git
cd enterprise-rag-chatbot
cp .env.example .env
```

### 2) Configure `.env`

```ini
# LLM selection
LLM_PROVIDER=local            # local | openrouter
OPENAI_BASE_URL=http://vllm:8000/v1  # used when LLM_PROVIDER=local
OPENROUTER_API_KEY=sk-or-...        # used when LLM_PROVIDER=openrouter

# Embeddings
EMBEDDINGS_PROVIDER=openai     # openai | voyage | nomic
OPENAI_API_KEY=sk-...          # required if using OpenAI embeddings
VOYAGE_API_KEY=...
NOMIC_API_KEY=...

# Vector DB
VECTOR_DB=weaviate
WEAVIATE_URL=http://weaviate:8080
WEAVIATE_API_KEY=dev-key       # can be dummy for local

# Memory (optional)
MEMORY_BACKEND=zep             # zep | mem0 | none
ZEP_API_URL=http://zep:8001
ZEP_API_KEY=dev-key

# Observability (optional)
OBSERVABILITY=langfuse         # langfuse | phoenix | none
LANGFUSE_HOST=http://langfuse:3000
LANGFUSE_PUBLIC_KEY=dev
LANGFUSE_SECRET_KEY=dev

# Guardrails
GUARDRAILS_ENABLED=true
```

### 3) Start the stack

```bash
docker compose up -d --build
```

This brings up:

* `app` (FastAPI)
* `weaviate` (vector DB) + `weaviate-etcd`
* `vllm` (local LLM server; change or disable if using OpenRouter)
* `zep` (memory) — optional
* `langfuse` (observability) — optional

**URLs**

* App API & UI: [http://localhost:8000](http://localhost:8000)
* Langfuse: [http://localhost:3000](http://localhost:3000)
* Weaviate Console (if enabled): [http://localhost:8080](http://localhost:8080)

---

## 🐳 `docker-compose.yml` (excerpt)

```yaml
version: "3.9"
services:
  app:
    build: ./app
    env_file: .env
    depends_on: [weaviate]
    ports: ["8000:8000"]
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000

  weaviate:
    image: semitechnologies/weaviate:1.24.6
    environment:
      QUERY_DEFAULTS_LIMIT: "20"
      AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: "true"
      PERSISTENCE_DATA_PATH: "/var/lib/weaviate"
      DEFAULT_VECTORIZER_MODULE: "none"
    ports: ["8080:8080"]
    volumes: ["weaviate_data:/var/lib/weaviate"]

  vllm:
    image: vllm/vllm-openai:latest
    command: >
      --model meta-llama/Meta-Llama-3.1-8B-Instruct
      --host 0.0.0.0
      --port 8000
    ports: ["8001:8000"]        # container:8000 → host:8001
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: ["gpu"]
    # If no GPU, comment this service and set LLM_PROVIDER=openrouter

  zep:
    image: getzep/zep:latest
    environment:
      ZEP_AUTH_REQUIRED: "false"
    ports: ["8001:8001"]

  langfuse:
    image: langfuse/langfuse:latest
    environment:
      NEXTAUTH_SECRET: "dev"
      DATABASE_URL: "file:/data/langfuse.db?connection_limit=1"
    volumes: ["langfuse_data:/data"]
    ports: ["3000:3000"]

volumes:
  weaviate_data:
  langfuse_data:
```

> **No GPU?** Comment out the `vllm` service, set `LLM_PROVIDER=openrouter`, and provide `OPENROUTER_API_KEY`.

---

## 🖥 Running (Local vs OpenRouter)

### Local LLM (vLLM / LM Studio / Ollama)

* With Compose: keep the `vllm` service and `LLM_PROVIDER=local`.
* **LM Studio/Ollama** alternative: remove `vllm`, run your local server, and set:

  ```
  LLM_PROVIDER=local
  OPENAI_BASE_URL=http://host.docker.internal:11434/v1   # Ollama default, adjust port
  ```

### OpenRouter

```
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-or-...
```

---

## 📥 Ingestion (Docker)

Run ingestion inside the `app` container so paths and envs match:

```bash
docker compose exec app python ingest/pipelines/docling.py --source /data/docs
docker compose exec app python ingest/pipelines/firecrawl.py --url https://internal.portal/docs --out /data/crawled
```

Configure **`ingest/config.yml`**:

* Auth & refresh cadence
* PII redaction rules
* Metadata tags: `app`, `version`, `audience`, `last_reviewed`

---

## 🔎 Retrieval Pipeline

1. **Embeddings:** OpenAI / Voyage / Nomic (toggle via env).
2. **Vector Search:** Weaviate (default) with metadata filters.
3. **Rerank (optional):** Voyage reranker for long contexts.
4. **Synthesis:** Local LLM (vLLM/LM Studio/Ollama) **or** OpenRouter.
5. **Guardrails:** must-cite, PII/secret checks, allow-lists/deny-lists.
6. **Observability:** Langfuse/Phoenix traces and cost/latency.

---

## 📊 Evaluation (Ragas)

```bash
docker compose exec app python eval/ragas_pipeline.py \
  --dataset eval/datasets/support_queries.jsonl \
  --report out/eval_report.json
```

* **Metrics:** faithfulness, groundedness, context precision/recall, latency, cost
* Add a CI job to fail on regression (example workflow in `.github/workflows/evals.yml`).

---

## 🔒 Security & Compliance

* All services run in your environment; no vendor lock-in.
* Ingestion-time and output redaction.
* Role-based memory (Zep/Mem0) keyed to department/user.
* Deterministic abstain path when confidence is low.

---

## 🧭 Configuration Matrix

| Concern             | Toggle                        |              |          |          |
| ------------------- | ----------------------------- | ------------ | -------- | -------- |
| Local vs OpenRouter | \`LLM\_PROVIDER=local         | openrouter\` |          |          |
| Local LLM URL       | `OPENAI_BASE_URL`             |              |          |          |
| Embeddings          | \`EMBEDDINGS\_PROVIDER=openai | voyage       | nomic\`  |          |
| Vector DB           | \`VECTOR\_DB=weaviate         | milvus       | pinecone | chroma\` |
| Memory              | \`MEMORY\_BACKEND=zep         | mem0         | none\`   |          |
| Observability       | \`OBSERVABILITY=langfuse      | phoenix      | none\`   |          |
| Guardrails          | \`GUARDRAILS\_ENABLED=true    | false\`      |          |          |

---

## 🗺 Roadmap

* [ ] Letta-based agentic memory
* [ ] Multi-tenant vector indexes
* [ ] Semantic retrieval cache (TTL + eviction)
* [ ] Domain-tuned reranker

---

## 🤝 Contributing

PRs welcome — small, focused changes with a brief design note in the PR body.

## 📜 License

MIT — see **LICENSE**.

---
