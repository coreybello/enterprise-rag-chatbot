# Configuration Reference

## 📋 Overview

This document provides a comprehensive reference for all configuration options available in the Agentic RAG system. Configuration is managed through environment variables, YAML files, and Docker Compose settings.

## 🏗️ Configuration Layers

### 1. Environment Variables (.env)
Primary configuration method for most settings. Loaded from `.env` files or system environment.

### 2. YAML Configuration Files
Structured configuration for complex settings in `config/` directory.

### 3. Docker Compose Configuration
Service definitions and deployment settings in `deploy/compose/`.

## 🔧 Core Configuration

### Application Settings

**Basic Application**
```env
# Environment mode
ENVIRONMENT=development  # development, staging, production

# Application settings
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=true  # Enable debug mode
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
```

**API Configuration**
```env
# API settings
API_PREFIX=/api/v1
CORS_ORIGINS=["http://localhost:3000","http://localhost:8000"]
RATE_LIMIT_ENABLED=true
MAX_REQUESTS_PER_MINUTE=100
```

### Database Configuration

**PostgreSQL (Primary Database)**
```env
# PostgreSQL connection
DATABASE_URL=postgresql://user:password@localhost:5432/rag_db
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
DB_POOL_RECYCLE=3600
```

**Redis (Caching)**
```env
# Redis connection
REDIS_URL=redis://localhost:6379/0
REDIS_CACHE_TTL=3600  # 1 hour
SESSION_TTL=86400  # 24 hours
```

### Vector Database Configuration

**Weaviate (Default)**
```env
# Weaviate settings
VECTOR_DB_PROVIDER=weaviate
WEAVIATE_URL=http://localhost:8080
WEAVIATE_API_KEY=optional-api-key
WEAVIATE_BATCH_SIZE=100
WEAVIATE_BATCH_TIMEOUT=30
```

**Alternative Vector Databases**
```env
# Pinecone
VECTOR_DB_PROVIDER=pinecone
PINECONE_API_KEY=your-pinecone-key
PINECONE_ENVIRONMENT=us-west1-gcp
PINECONE_INDEX=rag-index

# Chroma
VECTOR_DB_PROVIDER=chroma
CHROMA_HOST=localhost
CHROMA_PORT=8000
CHROMA_COLLECTION=rag-documents
```

## 🤖 LLM Provider Configuration

### Local LLM (vLLM)
```env
# vLLM settings
LLM_PROVIDER=local
VLLM_BASE_URL=http://localhost:8001
VLLM_MODEL_NAME=microsoft/DialoGPT-medium
VLLM_MAX_TOKENS=2048
VLLM_TEMPERATURE=0.7
VLLM_TOP_P=0.9
VLLM_TIMEOUT=30
```

### OpenRouter API
```env
# OpenRouter settings
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your-api-key
OPENROUTER_MODEL_NAME=anthropic/claude-3-sonnet
OPENROUTER_MAX_TOKENS=4000
OPENROUTER_TEMPERATURE=0.7
OPENROUTER_TIMEOUT=30
OPENROUTER_MAX_COST_PER_REQUEST=0.10
```

### Provider Fallback Configuration
```env
# Failover settings
FAILOVER_STRATEGY=priority  # priority, round_robin, health_weighted
CIRCUIT_BREAKER_ENABLED=true
CIRCUIT_BREAKER_THRESHOLD=5
HEALTH_CHECK_INTERVAL=300
```

## 📄 Document Processing Configuration

### Ingestion Settings
```env
# File processing
MAX_FILE_SIZE=52428800  # 50MB
ALLOWED_FILE_TYPES=pdf,docx,txt,md,html
INGESTION_BATCH_SIZE=10
INGESTION_WORKERS=4
AUTO_PROCESS_UPLOADS=true
```

### Chunking Configuration
```env
# Chunking strategies
CHUNKING_STRATEGY=semantic  # fixed, recursive, semantic, paragraph
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
MIN_CHUNK_SIZE=100
MAX_CHUNK_SIZE=2000
```

### Embedding Configuration
```env
# Embedding provider
EMBEDDING_PROVIDER=openai  # openai, voyage, nomic, sentence_transformers
EMBEDDING_MODEL=text-embedding-3-small
EMBEDDING_BATCH_SIZE=32
EMBEDDING_TIMEOUT=30
```

## 🔍 Retrieval Configuration

### Search Settings
```env
# Retrieval parameters
TOP_K_RETRIEVAL=10
RERANK_TOP_K=5
SIMILARITY_THRESHOLD=0.7
ENABLE_RERANKING=true
HYBRID_SEARCH=true
BM25_WEIGHT=0.3
```

### Reranking Configuration
```env
# Cohere reranking (if enabled)
COHERE_API_KEY=your-cohere-key
COHERE_MODEL=rerank-english-v2.0
RERANK_MAX_DOCUMENTS=100
RERANK_CONFIDENCE_THRESHOLD=0.5
```

## 🛡️ Security Configuration

### Authentication
```env
# JWT authentication
JWT_SECRET=your-super-secret-jwt-key-here
JWT_ALGORITHM=HS256
JWT_ACCESS_EXPIRE_MINUTES=15
JWT_REFRESH_EXPIRE_DAYS=7
JWT_ISSUER=agentic-rag
```

### Rate Limiting
```env
# Rate limiting
RATE_LIMIT_ENABLED=true
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_PERIOD=60  # seconds
RATE_LIMIT_STORAGE=memory  # memory, redis
```

### Security Headers
```env
# Security headers
CSP_ENABLED=true
CSP_DIRECTIVES="default-src 'self'"
XSS_PROTECTION_ENABLED=true
HSTS_ENABLED=true
HSTS_MAX_AGE=31536000
```

## 📊 Monitoring & Observability

### Logging Configuration
```env
# Logging settings
LOG_LEVEL=INFO
LOG_FORMAT=json  # json, console
LOG_FILE=/app/logs/app.log
LOG_ROTATION=100MB
LOG_RETENTION=7d
```

### Metrics Configuration
```env
# Metrics collection
METRICS_ENABLED=true
METRICS_PORT=9090
METRICS_PATH=/metrics
PROMETHEUS_ENABLED=true
```

### Tracing Configuration
```env
# Distributed tracing
TRACING_ENABLED=true
TRACING_PROVIDER=langfuse  # langfuse, phoenix, jaeger
LANGFUSE_PUBLIC_KEY=your-langfuse-key
LANGFUSE_SECRET_KEY=your-langfuse-secret
LANGFUSE_HOST=http://localhost:3000
```

## 🗄️ Memory Configuration

### Zep Memory Backend
```env
# Zep settings
MEMORY_PROVIDER=zep
ZEP_API_URL=http://localhost:8002
ZEP_API_KEY=optional-api-key
ZEP_AUTO_SUMMARIZE=true
ZEP_MEMORY_WINDOW_SIZE=12
ZEP_MAX_MESSAGES=100
ZEP_MAX_TOKENS=8000
```

### Memory Scoping
```env
# Role-based memory access
MEMORY_SCOPE_BY_ROLE=true
MEMORY_ADMIN_ACCESS_ALL=true
MEMORY_USER_ISOLATION=true
MEMORY_SESSION_TTL=86400
MEMORY_AUTO_CLEANUP_ENABLED=true
```

## 🚀 Performance Configuration

### Caching
```env
# Cache settings
CACHE_ENABLED=true
CACHE_BACKEND=redis  # redis, memory
CACHE_TTL=3600  # 1 hour
CACHE_MAX_SIZE=1000
```

### Connection Pooling
```env
# Database connection pooling
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
DB_POOL_RECYCLE=3600
DB_POOL_TIMEOUT=30
```

### Timeouts
```env
# Various timeouts
REQUEST_TIMEOUT=120
DATABASE_TIMEOUT=30
CACHE_TIMEOUT=5
EXTERNAL_API_TIMEOUT=30
```

## 🌐 Network Configuration

### Service URLs
```env
# Internal service URLs
WEAVIATE_URL=http://weaviate:8080
REDIS_URL=redis://redis:6379
POSTGRES_URL=postgresql://postgres:5432
ZEP_URL=http://zep:8002
LANGFUSE_URL=http://langfuse:3000
```

### External API URLs
```env
# External services
OPENAI_API_BASE=https://api.openai.com/v1
VOYAGE_API_BASE=https://api.voyageai.com/v1
COHERE_API_BASE=https://api.cohere.ai/v1
OPENROUTER_API_BASE=https://openrouter.ai/api/v1
```

## 🔧 Development Configuration

### Development Settings
```env
# Development-specific
DEBUG=true
RELOAD=true  # Auto-reload on code changes
PROFILE=false  # Enable profiling
TESTING=false  # Testing mode
```

### Test Configuration
```env
# Testing
TEST_DATABASE_URL=postgresql://test:test@localhost:5432/test_db
TEST_REDIS_URL=redis://localhost:6379/1
TEST_MODE=true
```

## 📁 Configuration Files

### compliance.yaml
Located at `config/compliance.yaml`:
```yaml
pii_detection:
  enabled: true
  detection_threshold: 0.8
  action_on_detection: "redact"
  entities_to_detect:
    - "PERSON"
    - "EMAIL_ADDRESS"
    - "PHONE_NUMBER"
    - "SSN"
    - "CREDIT_CARD"

citation:
  enforce_citations: true
  min_citations_required: 1
  max_citations_allowed: 5
  citation_format: "[{source_id}]"
  confidence_threshold: 0.7

topic_filter:
  enabled: true
  action_on_blocked_topic: "block"
  blocked_topics:
    - "personal_finances"
    - "medical_advice"
    - "legal_advice"
```

### logging.yaml
Located at `config/logging.yaml`:
```yaml
version: 1
formatters:
  simple:
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  json:
    format: json

handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    level: INFO
  file:
    class: logging.handlers.RotatingFileHandler
    formatter: json
    filename: /app/logs/app.log
    maxBytes: 10485760
    backupCount: 5

loggers:
  app:
    level: INFO
    handlers: [console, file]
    propagate: no
  database:
    level: WARNING
    handlers: [console]
    propagate: no
```

## 🔄 Environment-Specific Configuration

### Development Environment
```env
# .env.development
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=DEBUG
DATABASE_URL=postgresql://user:pass@localhost:5432/rag_dev
```

### Production Environment
```env
# .env.production
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=INFO
DATABASE_URL=postgresql://user:pass@production-db:5432/rag_prod
```

### Staging Environment
```env
# .env.staging
ENVIRONMENT=staging
DEBUG=false
LOG_LEVEL=INFO
DATABASE_URL=postgresql://user:pass@staging-db:5432/rag_staging
```

## 🚀 Deployment Configuration

### Docker Compose Overrides
`docker-compose.override.yml` for development:
```yaml
services:
  app:
    volumes:
      - ./src:/app/src
      - ./config:/app/config
    environment:
      - ENVIRONMENT=development
      - RELOAD=true
```

### Kubernetes Configuration
Example deployment config:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rag-app
spec:
  template:
    spec:
      containers:
      - name: app
        env:
        - name: ENVIRONMENT
          value: production
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: rag-secrets
              key: database-url
```

## 📋 Validation Rules

### Required Variables
- `JWT_SECRET` - Must be at least 32 characters
- `DATABASE_URL` - Must be a valid PostgreSQL connection string
- `LLM_PROVIDER` - Must be one of: local, openrouter
- `VECTOR_DB_PROVIDER` - Must be one of: weaviate, pinecone, chroma

### Optional Variables with Defaults
- `APP_PORT` - Default: 8000
- `LOG_LEVEL` - Default: INFO
- `CHUNK_SIZE` - Default: 1000
- `TOP_K_RETRIEVAL` - Default: 10

## 🐛 Troubleshooting Configuration

### Common Issues
- **Missing variables**: Ensure all required variables are set
- **Type mismatches**: Check that values match expected types (string, number, boolean)
- **File permissions**: Ensure config files are readable
- **Environment precedence**: System env vars override .env files

### Validation Commands
```bash
# Check configuration
python -c "from src.config.settings import settings; print(settings.json())"

# Validate environment
scripts/validate_env.py

# Test connections
scripts/test_connections.py
```

## 📚 Related Documentation

- [Deployment Guide](DEPLOYMENT.md) - How to deploy with these configurations
- [Security Guidelines](SECURITY.md) - Security best practices
- [Troubleshooting Guide](TROUBLESHOOTING.md) - Solving configuration issues

---

*This configuration reference is maintained by the development team. Please check for updates when upgrading versions.*