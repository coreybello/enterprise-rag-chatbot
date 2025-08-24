# Enterprise RAG Chatbot - Backend Implementation

## 🎯 Overview

This is a complete FastAPI backend implementation for an Enterprise RAG (Retrieval-Augmented Generation) Chatbot with dual LLM provider support, modular architecture, and comprehensive API endpoints.

## 🏗️ Architecture

### Core Components

1. **FastAPI Application** (`src/app/main.py`)
   - Application entry point with lifespan management
   - Middleware setup (CORS, rate limiting, error handling)
   - Router integration for modular endpoints

2. **RAG Pipeline** (`src/core/rag_pipeline.py`)
   - Document ingestion (file upload + text processing)
   - Embedding generation and vector storage
   - Semantic retrieval with multiple strategies
   - LLM-based answer generation

3. **LLM Providers** (`src/providers/`)
   - **vLLM Provider**: Local inference server integration
   - **OpenRouter Provider**: Cloud API integration
   - Factory pattern for easy provider switching

4. **Vector Storage** (`src/core/vector_store.py`)
   - ChromaDB integration for semantic search
   - Chunk storage and retrieval
   - Similarity search with filtering

5. **Document Processing** (`src/core/document_processor.py`)
   - Multi-format support (PDF, DOCX, TXT, MD, HTML)
   - Text extraction and chunking
   - Metadata preservation

## 🚀 Features

### API Endpoints

#### Health & Status
- `GET /api/v1/health` - Health check
- `GET /api/v1/health/detailed` - Detailed system status

#### Chat Interface
- `POST /api/v1/chat` - Process chat messages with RAG
- `POST /api/v1/chat/stream` - Streaming chat responses
- `GET /api/v1/conversations` - List conversations
- `GET /api/v1/conversations/{id}` - Get conversation
- `DELETE /api/v1/conversations/{id}` - Delete conversation

#### Document Management
- `POST /api/v1/documents/upload` - Upload files
- `POST /api/v1/documents/upload-text` - Upload text content
- `POST /api/v1/documents/{id}/process` - Process document
- `POST /api/v1/documents/search` - Semantic document search
- `GET /api/v1/documents` - List documents
- `DELETE /api/v1/documents/{id}` - Delete document
- `POST /api/v1/documents/bulk` - Bulk operations

#### RAG Operations
- `POST /api/v1/rag/query` - Advanced RAG queries
- `POST /api/v1/rag/embeddings` - Generate embeddings
- `POST /api/v1/rag/reindex` - Reindex documents
- `GET /api/v1/rag/metrics` - Performance metrics
- `GET /api/v1/rag/vector-store/stats` - Vector store statistics

### Key Features

- **Dual LLM Support**: Switch between local vLLM and OpenRouter
- **Streaming Responses**: Real-time chat with SSE
- **Background Processing**: Async document ingestion
- **Rate Limiting**: Built-in API protection
- **Error Handling**: Comprehensive error management
- **Validation**: Pydantic models for all I/O
- **Observability**: Health checks and metrics
- **File Support**: PDF, DOCX, TXT, MD, HTML
- **Chunking Strategies**: Configurable text splitting
- **Retrieval Methods**: Similarity, MMR, diversity ranking

## 🛠️ Setup & Usage

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

Copy `.env.example` to `.env` and configure:

```bash
# Choose LLM provider
LLM_PROVIDER="vllm"  # or "openrouter"

# vLLM Configuration
VLLM_BASE_URL="http://localhost:8001"
VLLM_MODEL_NAME="microsoft/DialoGPT-medium"

# OpenRouter Configuration (if using)
OPENROUTER_API_KEY="your-api-key"
OPENROUTER_MODEL_NAME="anthropic/claude-3-sonnet"

# Vector Database
VECTOR_DB_PATH="./data/vectordb"
CHROMA_COLLECTION_NAME="rag_documents"

# Embedding Model
EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_DEVICE="cpu"  # or "cuda"
```

### 3. Start the Server

```bash
# Using the startup script
python start_server.py

# Or directly with uvicorn
uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Access API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 📁 Project Structure

```
src/
├── app/                    # FastAPI application (canonical API implementation)
│   ├── main.py            # Application entry point with lifespan management
│   ├── api/               # API route modules
│   │   ├── chat.py        # Chat endpoints
│   │   ├── documents.py   # Document management
│   │   ├── rag.py         # RAG operations
│   │   └── health.py      # Health checks
│   └── middleware/        # Middleware components
│       ├── cors.py        # CORS setup
│       ├── error_handler.py # Error handling
│       ├── logging.py     # Request logging
│       └── rate_limiting.py # Rate limiting
├── core/                  # Core business logic
│   ├── rag_pipeline.py    # Main RAG orchestrator
│   ├── embedding_service.py # Embedding generation
│   ├── vector_store.py    # Vector database
│   ├── document_processor.py # Document processing
│   └── retriever.py       # Retrieval strategies
├── providers/             # LLM provider implementations
│   ├── base_provider.py   # Enhanced base provider interface
│   ├── vllm_provider.py   # vLLM integration
│   ├── openrouter_provider.py # OpenRouter integration
│   └── provider_factory.py # Comprehensive provider factory
├── models/                # Pydantic data models
│   ├── chat.py            # Chat-related models
│   ├── documents.py       # Document models
│   ├── rag.py             # RAG-specific models
│   └── common.py          # Common models
├── config/                # Configuration management
│   ├── environments/      # Environment-specific configurations
│   ├── services/          # Service-specific configurations
│   ├── settings.yaml      # Main application settings
│   └── logging.yaml       # Logging configuration
└── utils/                 # Utility functions
    ├── file_utils.py      # File operations
    └── text_utils.py      # Text processing
```

### 🧹 Cleanup and Optimization

This codebase has undergone comprehensive cleanup and optimization:

- **Removed duplicate API structure**: Deleted `src/api/` directory (duplicate of `src/app/`)
- **Eliminated deprecated code**: Removed wrapper files (`base.py`, `factory.py`, `llm_factory.py`) that just re-exported from canonical modules
- **Cleaned up empty directories**: Removed `src/llm/` directory that served no functional purpose
- **Excluded runtime data**: Deleted `memory/` and `qdrant_storage/` directories (should not be in version control)
- **Optimized build context**: Added comprehensive `.dockerignore` and `frontend/.dockerignore` files
- **Simplified documentation**: Replaced over-engineered 5-level nested docs structure with flat, practical organization
- **Consolidated configuration**: Reorganized config files into logical categories (`environments/`, `services/`)
- **Enhanced git hygiene**: Updated `.gitignore` to prevent runtime data and build artifacts from being committed

The result is a clean, optimized codebase with no dead code, improved build performance, and better maintainability.

## 🔧 Configuration Options

### LLM Providers

**vLLM (Local Inference)**
- Requires running vLLM server
- High performance for production
- Full control over model and resources

**OpenRouter (Cloud API)**
- Access to multiple models
- No local infrastructure needed
- Pay-per-use pricing

### RAG Configuration

- **Chunk Size**: 512 characters (configurable)
- **Chunk Overlap**: 50 characters
- **Retrieval Top-K**: 5 documents
- **Similarity Threshold**: 0.7
- **Max Context Length**: 4000 tokens

### File Processing

- **Supported Formats**: PDF, DOCX, TXT, MD, HTML
- **Max File Size**: 10MB (configurable)
- **Background Processing**: Async document ingestion
- **Batch Operations**: Bulk document management

## 🚦 API Usage Examples

### Chat with RAG

```bash
curl -X POST "http://localhost:8000/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is the main topic of the uploaded documents?",
    "use_rag": true,
    "max_tokens": 1000,
    "temperature": 0.7
  }'
```

### Upload Document

```bash
curl -X POST "http://localhost:8000/api/v1/documents/upload" \
  -F "file=@document.pdf" \
  -F "auto_process=true"
```

### Search Documents

```bash
curl -X POST "http://localhost:8000/api/v1/documents/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "machine learning",
    "top_k": 10,
    "similarity_threshold": 0.7
  }'
```

## 🏁 Next Steps

1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Configure Environment**: Copy `.env.example` to `.env`
3. **Start LLM Provider**: Set up vLLM server or get OpenRouter API key
4. **Run Server**: `python start_server.py`
5. **Test API**: Visit http://localhost:8000/docs

## 🔗 Integration Points

- **Frontend**: REST API ready for React/Vue/Angular integration
- **Vector Databases**: Easily extend to Pinecone, Weaviate, etc.
- **LLM Providers**: Add more providers via the factory pattern
- **Authentication**: Add JWT/OAuth2 middleware as needed
- **Monitoring**: Integrate with Prometheus, Grafana, etc.

This backend provides a solid foundation for an enterprise-grade RAG chatbot with room for customization and scaling.
