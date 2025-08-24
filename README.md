# Agentic RAG System - Enterprise-Grade AI-Powered Knowledge Management

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com)
[![Next.js](https://img.shields.io/badge/Next.js-14.2.5-black.svg)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.5.3-blue.svg)](https://typescriptlang.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.5.0-red.svg)](https://pydantic.dev)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

**Agentic RAG** is a production-ready, enterprise-grade **Retrieval-Augmented Generation** system with intelligent automation capabilities. Built with modern **Next.js 14 frontend** and **FastAPI backend**, featuring comprehensive **security guardrails**, **compliance frameworks**, and **observability systems** for mission-critical deployments.

### 🧠 Agentic Intelligence Features

✅ **Intelligent Automation**
- **Claude-Flow orchestration** for multi-agent coordination and task automation
- **Adaptive memory management** with Zep integration for context-aware conversations
- **Smart document processing** with automatic categorization and metadata extraction
- **Dynamic prompt engineering** with context-aware response generation

✅ **Enterprise Security & Compliance**
- **PII detection and redaction** with configurable sensitivity levels
- **Content filtering and topic moderation** for safe AI interactions
- **Citation enforcement** ensuring all responses are properly sourced
- **Compliance logging** with GDPR, HIPAA, and SOC2 audit trails
- **Role-based access control** with granular permission management

✅ **Production-Ready RAG Pipeline**
- **Multi-provider embedding support** (OpenAI, Voyage, Nomic, SentenceTransformers)
- **Advanced chunking strategies** (fixed-size, semantic, recursive, paragraph-based)
- **Hybrid search capabilities** with BM25 + vector similarity
- **Neural reranking** with Cohere integration for enhanced relevance
- **Vector database abstraction** (Weaviate, Pinecone, Chroma, Milvus)

✅ **Comprehensive Observability**
- **Langfuse integration** for AI model performance tracking
- **Structured logging** with security event correlation
- **Real-time monitoring** with health checks and alerting
- **Performance analytics** with detailed usage metrics

## 📚 Documentation Hub

This README provides a high-level overview. For detailed information, explore our comprehensive documentation:

**📖 [Complete Documentation Hub](docs/INDEX.md)**

### Quick Access
- **[Quick Start Guide](docs/QUICK_START.md)** - Get running in 5 minutes
- **[System Overview](docs/OVERVIEW.md)** - Architecture and capabilities deep-dive
- **[API Reference](docs/API_REFERENCE.md)** - Complete API documentation
- **[Configuration Guide](docs/CONFIGURATION.md)** - Environment and service configuration
- **[Security Guidelines](docs/SECURITY.md)** - Security policies and compliance
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Production deployment instructions

### Role-Based Guides
- **[Developer Onboarding](docs/roles/DEVELOPER.md)** - Complete development setup
- **[Frontend Development](docs/roles/FRONTEND.md)** - Frontend-specific guidelines

## 🚀 Quick Start

### Prerequisites
- **Node.js** 18.17.0+ and npm 9.0.0+
- **Python** 3.9+ with pip
- **Docker** and Docker Compose (recommended)
- **Git** for version control

### 1. Docker Compose Setup (Recommended)

```bash
# Clone and setup
git clone <repository-url>
cd agentic-rag

# Configure environment
cd deploy/compose
cp .env.example .env
# Edit .env with your API keys and configuration

# Start all services
docker-compose up -d

# View service status
docker-compose ps
```

**Services Available:**
- **Frontend** (Next.js): http://localhost:3000
- **Backend API** (FastAPI): http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Weaviate** (Vector DB): http://localhost:8080
- **Langfuse** (Observability): http://localhost:3001
- **Zep** (Memory): http://localhost:8002

### 2. Local Development

```bash
# Backend setup
pip install -r requirements.txt
cp .env.example .env
# Configure .env with your settings

# Frontend setup  
cd frontend
npm install
cp .env.example .env.local
# Configure .env.local with your settings

# Run services (separate terminals)
# Terminal 1: Backend
python -m src.app.main

# Terminal 2: Frontend  
cd frontend && npm run dev
```

## 🏗️ Project Structure

```
agentic-rag/
├── frontend/                    # Next.js 14 Frontend Application
│   ├── src/app/                # App Router (login, chat, documents, admin)
│   ├── src/components/         # Reusable UI components
│   ├── src/contexts/          # React contexts (Auth, Theme)
│   ├── src/hooks/             # Custom React hooks
│   ├── src/lib/               # Utilities (API client, WebSocket)
│   └── src/types/             # TypeScript definitions
├── src/                        # Backend RAG System
│   ├── app/                   # FastAPI application
│   ├── core/                  # Core RAG components
│   ├── guardrails/            # Security and compliance systems
│   ├── security/              # Authentication and authorization
│   ├── memory/                # Conversation memory management
│   ├── observability/         # Monitoring and logging
│   ├── providers/             # LLM and embedding providers
│   ├── vector_db/            # Vector database abstractions
│   ├── retrieval/            # Search and retrieval engine
│   └── ingestion/            # Document processing pipeline
├── deploy/compose/            # Docker Compose deployment
├── docs/                      # Comprehensive documentation
├── coordination/              # Claude-Flow orchestration
├── config/                    # Configuration management
├── tests/                     # Test suites (unit, integration, e2e)
└── scripts/                   # Utility and setup scripts
```

## 🔧 Key Components

### Agentic Capabilities
- **Claude-Flow Integration**: Multi-agent coordination and task orchestration
- **Memory Management**: Persistent conversation context with Zep
- **Intelligent Routing**: Smart decision-making for complex queries
- **Adaptive Learning**: System improvement through usage patterns

### Security Guardrails (`src/guardrails/`)
- **PII Detection**: Automatic detection and redaction of sensitive information
- **Content Filtering**: Topic moderation and inappropriate content blocking
- **Citation Enforcement**: Ensures all AI responses include proper source attribution
- **Compliance Logging**: Comprehensive audit trails for regulatory compliance

### Multi-Provider Architecture (`src/providers/`)
- **LLM Providers**: OpenRouter, vLLM, local models with automatic failover
- **Embedding Providers**: OpenAI, Voyage AI, Nomic, SentenceTransformers
- **Vector Databases**: Weaviate (primary), Pinecone, Chroma, Milvus

### Enterprise Features
- **Role-Based Access Control**: Granular user permissions and data access
- **Observability**: Real-time monitoring with Langfuse integration
- **Scalable Architecture**: Horizontal scaling with Docker and Kubernetes
- **Health Monitoring**: Comprehensive health checks and automated recovery

## ⚙️ Configuration

### Environment Variables

Key configuration options (see [Configuration Guide](docs/CONFIGURATION.md) for complete reference):

```env
# Core Settings
ENVIRONMENT=production
LOG_LEVEL=INFO

# LLM Configuration
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your-api-key

# Embedding Provider
EMBEDDING_PROVIDER=openai
OPENAI_API_KEY=your-api-key

# Vector Database
VECTOR_DB_PROVIDER=weaviate
WEAVIATE_URL=http://localhost:8080

# Security & Compliance
GUARDRAILS_ENABLED=true
PII_DETECTION_ENABLED=true
CITATION_REQUIRED=true

# Observability
OBSERVABILITY_PROVIDER=langfuse
LANGFUSE_SECRET_KEY=your-secret-key
```

### Provider Configuration

The system supports multiple providers with automatic failover:

| Component | Development | Production |
|-----------|-------------|------------|
| LLM | vLLM (local) | OpenRouter/vLLM |
| Embeddings | SentenceTransformers | OpenAI/Voyage |
| Vector DB | Chroma | Weaviate |
| Memory | Zep (local) | Zep (production) |
| Observability | Local logs | Langfuse |

## 🛡️ Security & Compliance

### Built-in Security Features
- **PII Detection**: Automatic identification and redaction of sensitive data
- **Input Validation**: Comprehensive request validation and sanitization
- **Output Filtering**: Response content moderation and safety checks
- **Audit Logging**: Complete activity tracking for compliance requirements

### Compliance Standards
- **GDPR**: Data protection and privacy compliance
- **HIPAA**: Healthcare information security (when configured)
- **SOC2**: Security and availability controls
- **Custom Policies**: Configurable compliance rules per organization

### Authentication & Authorization
- **JWT-based authentication** with secure token management
- **Role-based access control** with granular permissions
- **Session management** with automatic timeout and refresh
- **API key management** for service-to-service communication

## 📊 Performance & Monitoring

### Performance Characteristics
- **Response Times**: < 1.5s median (local GPU inference)
- **Vector Search**: < 300ms for 1M+ documents
- **Document Processing**: ~50ms per page
- **Concurrent Users**: 100+ with horizontal scaling

### Monitoring & Observability
- **Real-time Dashboards**: System health and performance metrics
- **Usage Analytics**: AI model usage and cost tracking
- **Error Tracking**: Comprehensive error monitoring and alerting
- **Security Events**: Security incident detection and logging

## 🧪 Testing

### Running Tests

```bash
# Backend tests
pytest tests/ -v --cov=src

# Frontend tests
cd frontend
npm test

# End-to-end tests
cd frontend && npm run test:e2e

# Integration tests
pytest tests/integration/ -v
```

### Test Coverage
- **Unit Tests**: Core components and business logic
- **Integration Tests**: API endpoints and service interactions
- **End-to-End Tests**: Complete user workflows
- **Performance Tests**: Load testing and benchmarking

## 🚀 Deployment

### Production Deployment

```bash
# Production setup
cd deploy/compose
cp .env.example .env
# Configure production environment variables

# Deploy with production profile
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Scale services as needed
docker-compose up -d --scale app=3 --scale frontend=2
```

### Deployment Options
- **Docker Compose**: Single-server deployment
- **Kubernetes**: Enterprise orchestration (configs in `config/scaling/`)
- **Cloud Providers**: AWS, GCP, Azure compatible
- **Hybrid**: On-premises with cloud integration

### Health Checks & Monitoring
All services include comprehensive health checks:
- **API Health**: `GET /api/v1/health`
- **Frontend**: `GET /`
- **Vector DB**: Service-specific health endpoints
- **Memory Service**: `GET /healthz`

## 🛠️ Development

### Technology Stack

#### Frontend
- **Next.js 14.2.5** - React framework with App Router
- **React 18.3.1** - UI library with concurrent features
- **TypeScript 5.5.3** - Type-safe development
- **Tailwind CSS 3.4.6** - Utility-first styling
- **React Query 5.51.11** - Server state management
- **Socket.IO** - Real-time communication

#### Backend
- **FastAPI 0.104.1** - Modern Python web framework
- **Python 3.9+** - Programming language
- **Pydantic 2.5.0** - Data validation and settings
- **SQLAlchemy 2.0.23** - Database ORM
- **Uvicorn** - ASGI server

#### Infrastructure & AI
- **Weaviate 1.25.4** - Vector database
- **Langfuse** - AI observability platform
- **Zep** - Memory management
- **vLLM** - Local LLM inference
- **PostgreSQL 15** - Relational database

### Development Commands

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Code formatting and linting
black src/ tests/
isort src/ tests/
ruff check src/ tests/

# Type checking
mypy src/

# Frontend development
cd frontend
npm run lint        # ESLint
npm run typecheck   # TypeScript
npm run build       # Production build
```

## 🤝 Contributing

### Development Workflow
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes with proper tests
4. **Run** the full test suite
5. **Submit** a pull request with detailed description

### Code Standards
- **Python**: Black formatting, isort imports, type hints required
- **TypeScript**: Strict mode, ESLint rules enforced
- **Testing**: Minimum 90% code coverage required
- **Documentation**: Update docs for any API changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Resources

### Getting Help
- **[Troubleshooting Guide](docs/TROUBLESHOOTING.md)** - Common issues and solutions
- **[GitHub Issues](https://github.com/your-org/agentic-rag/issues)** - Bug reports and feature requests
- **[GitHub Discussions](https://github.com/your-org/agentic-rag/discussions)** - Community support

### Additional Resources
- **[Architecture Deep Dive](docs/ARCHITECTURE.md)** - Technical architecture details
- **[API Documentation](docs/API_REFERENCE.md)** - Complete API reference
- **[Security Guidelines](docs/SECURITY.md)** - Security best practices
- **[Troubleshooting Guide](docs/TROUBLESHOOTING.md)** - Common issues and solutions

---

**Built with ❤️ by the Agentic RAG Team**

**Core Technologies**: FastAPI + Next.js + Weaviate + Langfuse + Zep
**Orchestration**: Claude-Flow for intelligent automation
**Security**: Enterprise-grade guardrails and compliance systems

*For detailed implementation guides, API references, and advanced configuration, explore the [comprehensive documentation](docs/INDEX.md).*
