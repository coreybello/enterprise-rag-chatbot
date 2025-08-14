# **Product Requirements Document (PRD)**

**Product Name:** Enterprise RAG Chatbot
**Version:** 1.0
**Author:** Corey Bello
**Last Updated:** 2025-08-13

---

## **1. Purpose**

The Enterprise RAG Chatbot enables enterprise teams to query internal documentation in natural language and receive **accurate, grounded, and cited** answers.
The system is **self-hosted by default** for privacy and compliance, deployable via **Docker Compose**, and supports **two LLM modes**:

1. **Local inference** (vLLM, LM Studio, Ollama)
2. **OpenRouter API** for managed multi-model access.

This PRD outlines functional and non-functional requirements, architecture, and rollout plans.

---

## **2. Goals & Objectives**

### **Primary Goals**

* Provide a **production-ready, private RAG system** for internal document search and Q\&A.
* Ensure answers are **grounded in retrieved sources**, with clear citations.
* Offer **deployment flexibility**: local LLM inference or OpenRouter API.
* Support **observability**, **evaluation**, and **guardrails** for enterprise governance.

### **Secondary Goals**

* Enable **pluggable components** for embeddings, vector DBs, and memory backends.
* Facilitate **scaling** to millions of documents with minimal downtime.
* Maintain **developer-friendly modularity** for extending ingestion, retrieval, and orchestration.

---

## **3. Target Users**

* **Primary:** Enterprise IT teams, internal support desks, and operational teams.
* **Secondary:** Compliance, HR, legal, and policy departments.
* **Tertiary:** Developers and automation engineers integrating chatbot into internal tools.

---

## **4. Key Features**

### **Core**

1. **RAG Pipeline**

   * Document ingestion, chunking, and embedding.
   * Metadata tagging: `app`, `version`, `audience`, `last_reviewed`.
   * Vector database storage and retrieval.
   * Optional reranking for better context ordering.
   * LLM synthesis with must-cite enforcement.

2. **Deployment**

   * Docker Compose stack:

     * App API/UI (FastAPI)
     * Vector DB (Weaviate default)
     * Local LLM service (vLLM by default)
     * Memory backend (Zep)
     * Observability backend (Langfuse)
   * `.env` config for environment-specific setups.
   * GPU support for local inference.

3. **LLM Provider Switching**

   * `LLM_PROVIDER=local` → local inference via vLLM/LM Studio/Ollama.
   * `LLM_PROVIDER=openrouter` → OpenRouter API multi-model access.

4. **Guardrails**

   * Must cite retrieved sources.
   * PII and sensitive data detection.
   * Block/allow list for topics.
   * Configurable abstain thresholds.

5. **Observability**

   * Langfuse or Arize Phoenix for tracing, cost, and latency monitoring.
   * Span-level metrics for each pipeline stage.

6. **Evaluation**

   * Offline eval pipeline using **Ragas**.
   * Metrics: faithfulness, groundedness, retrieval precision/recall, latency, cost.
   * CI/CD integration to block deployments on regression.

---

## **5. Non-Functional Requirements**

* **Security**

  * All data processed within controlled environment for local mode.
  * Optional encryption for memory and vector DB.
* **Performance**

  * < 1.5s median response time for short queries on GPU-hosted local model.
  * Vector search latency < 300ms for 1M+ documents.
* **Scalability**

  * Horizontal scaling via Docker Swarm/Kubernetes.
  * Vector DB partitioning/sharding support.
* **Maintainability**

  * Modular codebase with documented interfaces for LLM, embeddings, vector DB, ingestion.
  * CI pipelines for linting, tests, and evals.
* **Compliance**

  * PII detection and redaction during ingestion and output stages.
  * Logs with audit-ready metadata.

---

## **6. Architecture**

### **High-Level Flow**

```
User → Preprocess → Embed Query → Vector Search → Rerank (opt) 
→ LLM (local/OpenRouter) → Guardrails → Answer + Citations → Observability + Eval Logging
```

### **Services (Docker Compose)**

* `app`: FastAPI backend + retrieval/orchestration logic.
* `weaviate`: vector DB (persistent volume).
* `vllm` (optional if `local` LLM mode): OpenAI-compatible local inference server.
* `zep`: conversation memory backend.
* `langfuse`: observability and tracing dashboard.

---

## **7. Configuration Matrix**

| Component         | Options                                            |
| ----------------- | -------------------------------------------------- |
| LLM Provider      | local \| openrouter                                |
| Local LLM Runtime | vLLM \| LM Studio \| Ollama                        |
| Embeddings        | OpenAI \| Voyage \| Nomic                          |
| Vector DB         | Weaviate (default) \| Milvus \| Pinecone \| Chroma |
| Memory            | Zep \| Mem0 \| None                                |
| Observability     | Langfuse \| Phoenix \| None                        |
| Guardrails        | Enabled \| Disabled                                |

---

## **8. User Stories**

1. *As an IT support agent*, I can query the chatbot for troubleshooting steps so I can resolve tickets faster.
2. *As a compliance officer*, I can review logs of answers with source citations for auditing.
3. *As a developer*, I can switch from local inference to OpenRouter API by changing `.env` values.
4. *As a manager*, I can run nightly evaluation reports to ensure accuracy remains above thresholds.

---

## **9. Success Metrics**

* **Precision/Recall**: ≥ 85% on internal QA dataset.
* **Faithfulness Score**: ≥ 90% in Ragas.
* **Latency**: p95 < 2.5s (local GPU inference).
* **Adoption**: ≥ 80% of support staff using chatbot weekly.
* **Governance Compliance**: 0 policy violations in quarterly audit.

---

## **10. Risks & Mitigations**

| Risk                                             | Mitigation                                         |
| ------------------------------------------------ | -------------------------------------------------- |
| GPU hardware not available for local mode        | Allow CPU fallback or OpenRouter API usage         |
| Ingestion failures due to unsupported file types | Support fallback to LlamaParse/Firecrawl           |
| Policy non-compliance in answers                 | Guardrails + abstain policy                        |
| Vector DB growth slowing search                  | Enable sharding, metadata filtering, and archiving |

---

## **11. Rollout Plan**

**Phase 1 — Core Build (Weeks 1–4)**

* Implement ingestion, retrieval, synthesis, guardrails, and Docker stack.
* Support vLLM and OpenRouter toggle.

**Phase 2 — Observability & Evaluation (Weeks 5–6)**

* Add Langfuse/Phoenix tracing and Ragas evals.
* Set up nightly CI/CD eval jobs.

**Phase 3 — Memory & Advanced Guardrails (Weeks 7–8)**

* Integrate Zep memory with role scoping.
* Expand guardrails for PII, topic restrictions, and tone.

**Phase 4 — Scale & Optimization (Weeks 9–10)**

* Test with >1M document embeddings.
* Optimize reranking and hybrid search.

---

## **12. Deliverables**

* Docker Compose stack (`/deploy/compose/`).
* Modular codebase for ingestion/retrieval/LLM/memory/guardrails.
* `.env.example` and full deployment docs.
* Ragas eval pipeline + example dataset.
* Observability dashboard templates.

---
