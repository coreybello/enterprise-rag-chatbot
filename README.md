# **Enterprise RAG Chatbot**  
> Private, high-accuracy, agentic Retrieval-Augmented Generation for enterprise knowledge — self-hosted, observable, and safe.

---

## 🚀 Overview  
The **Enterprise RAG Chatbot** is an **agentic, self-hosted** RAG system for answering organization-specific questions from your internal documentation.  
Built for **IT/support** and **knowledge-heavy teams**, it:

- **Plans** how to answer,  
- **Chooses and sequences tools**,  
- **Checks and revises its own work**,  
- **Adapts based on policies, memory, and evals**,  
- **Cites every answer**.

The system runs fully in your environment via **Docker Compose**, with **observability, evaluation, and guardrails** baked in.

---

## ✨ Agentic Features

The chatbot is **not** a one-shot LLM—it’s a **goal-directed agent loop**:

1. **Perceive** → Parse intent, detect domain, classify sensitivity.
2. **Plan** → Choose retrieval parameters, decide on reranking, memory filters.
3. **Act** → Call tools (vector DB, reranker, LLM) to synthesize a draft answer.
4. **Critique** → Run guardrails (must-cite, PII checks, policy compliance).
5. **Adapt** → If checks fail, re-retrieve, revise, or abstain.
6. **Learn** → Log traces and nightly evals to improve configs/policies.

This end-to-end **perceive → plan → act → critique → adapt** loop is what makes the system **agentic**.

---

## 🧩 Tech Stack (Levels 0–8)

| Level                   | Purpose                  | Tools |
| ----------------------- | ------------------------ | ----- |
| **8 – Alignment**       | Governance & guardrails  | Guardrails AI, Langfuse, Arize Phoenix |
| **7 – Memory**          | Role-based persistence   | Zep, Mem0 |
| **6 – Data Extraction** | Parse web/docs           | Firecrawl, Docling, LlamaParse |
| **5 – Embedding**       | Vector encoding          | OpenAI, Voyage, Nomic |
| **4 – Vector DB**       | Store/query              | Weaviate (default), Milvus, Pinecone, Chroma |
| **3 – Framework**       | Orchestration            | LangChain / LangGraph-style |
| **2 – LLMs**            | Response generation      | **Local:** vLLM / LM Studio / Ollama • **API:** OpenRouter |
| **1 – Evaluation**      | Quality checks           | Ragas, optional: DeepEval, LangSmith |
| **0 – Deployment**      | Hosting/scaling          | Docker Compose, K8s-ready manifests |

---

## 🏗 Agentic Architecture

```mermaid
    graph TD
        A[User Query] --> B[Perceive: Intent & Preprocess]
        B --> C[Plan: Retrieval Params + Memory Filters]
        C --> D[Act: Retrieve from Vector DB + Optional Reranker]
        D --> E[Synthesize: Local or API LLM]
        E --> F[Critique: Guardrails (\\must-cite, PII, policy\\)]
        F -->|Fail| C
        F -->|Pass| G[Final Answer + Citations]
        G --> H[Learn: Trace + Eval (\\Langfuse/Phoenix + Ragas\\)]
```

**Agent moments:**
- **Tool choice**: Decides whether to use a reranker.  
- **Memory adaptation**: Department/user context changes retrieval filters.  
- **Self-critique**: Fails output that doesn’t meet guardrail rules.  
- **Config learning**: Adjusts parameters from eval feedback.

---

## ⚙️ Quickstart (Docker)

```bash
git clone https://github.com/your-org/enterprise-rag-chatbot.git
cd enterprise-rag-chatbot
cp .env.example .env
docker compose up -d --build
```

**URLs**
- App: [http://localhost:8000](http://localhost:8000)  
- Langfuse: [http://localhost:3000](http://localhost:3000)  
- Weaviate console: [http://localhost:8080](http://localhost:8080)  

---

## 🔎 Retrieval & Decision Flow

1. **Embeddings**: OpenAI, Voyage, or Nomic.  
2. **Vector Search**: Weaviate (default) with metadata filters.  
3. **Optional Rerank**: Voyage for long contexts.  
4. **Synthesis**: Local LLM or OpenRouter API.  
5. **Guardrails**: Must-cite, PII/secret checks, allow/deny lists.  
6. **Observability**: Langfuse/Phoenix trace and cost/latency tracking.  
7. **Adaptation**: If a check fails → re-plan and retry.

---

## 📊 Evaluation & Learning

- **Nightly Ragas** evals: faithfulness, groundedness, precision/recall, latency, cost.  
- **CI integration**: Fail builds on metric regression.  
- **Feedback loop**: Poor performance → auto-adjust retrieval params, reranker use, or filters.

---

## 🔒 Safety & Governance

- **Local-first**: All services run in your infra—no vendor lock-in.  
- **Policy-driven**: Output must meet alignment rules before delivery.  
- **Deterministic abstain**: If confidence or evidence is low, the agent refuses.  
- **Memory isolation**: Role-based memory keeps contexts department-scoped.

---

## 🗺 Roadmap

- Letta-based agentic long-term memory  
- Multi-tenant vector indexes  
- Semantic retrieval cache with TTL/eviction  
- Domain-tuned reranker  

---

## 🤝 Contributing

PRs welcome — keep changes small, focused, and include a brief design note.

## 📜 License
MIT — see **LICENSE**.
