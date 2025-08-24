# Enterprise RAG Chatbot - Docker Deployment

This directory contains the complete Docker Compose stack for the Enterprise RAG Chatbot system.

## Architecture

The system consists of 5 core services and 2 database services:

### Core Services
- **app**: FastAPI backend with RAG orchestration logic
- **weaviate**: Vector database for embeddings storage
- **vllm**: Local LLM inference server (GPU-accelerated)
- **zep**: Conversation memory backend
- **langfuse**: Observability and tracing dashboard

### Database Services
- **zep_db**: PostgreSQL database for Zep memory storage
- **langfuse_db**: PostgreSQL database for Langfuse observability data

### Optional Services
- **redis**: Caching layer (enabled with `cache` profile)
- **nginx**: Reverse proxy for production (production configuration)

## Quick Start

1. **Copy environment configuration**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

2. **Start the stack**:
   ```bash
   # Development mode (with local LLM)
   docker-compose --profile local-llm up -d
   
   # Development mode (OpenRouter API only)
   docker-compose up -d
   
   # Production mode
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
   ```

3. **Access the services**:
   - **API**: http://localhost:8000
   - **API Docs**: http://localhost:8000/docs
   - **Weaviate**: http://localhost:8080
   - **Langfuse**: http://localhost:3000
   - **Zep**: http://localhost:8002

## Configuration Modes

### LLM Provider Configuration

#### Local Inference (Default)
```env
LLM_PROVIDER=local
VLLM_MODEL_NAME=microsoft/WizardLM-2-7B
```
- Requires GPU for optimal performance
- Uses vLLM service
- Complete data privacy

#### OpenRouter API
```env
LLM_PROVIDER=openrouter
OPENROUTER_API_KEY=your-api-key
OPENROUTER_DEFAULT_MODEL=microsoft/wizardlm-2-8x22b
```
- No local GPU required
- Access to multiple models
- Requires internet connection

### Service Profiles

- `local-llm`: Enables vLLM service for local inference
- `cache`: Enables Redis caching service
- `dev`: Development-specific configurations

## Environment Variables

Key configuration options in `.env`:

### Core Settings
```env
ENVIRONMENT=development|production
LLM_PROVIDER=local|openrouter
VECTOR_DB_PROVIDER=weaviate
MEMORY_PROVIDER=zep
OBSERVABILITY_PROVIDER=langfuse
```

### API Keys
```env
OPENAI_API_KEY=your-openai-key
OPENROUTER_API_KEY=your-openrouter-key
VOYAGE_API_KEY=your-voyage-key
```

### Performance
```env
MAX_CONCURRENT_REQUESTS=10
REQUEST_TIMEOUT=120
CHUNK_SIZE=512
TOP_K_RETRIEVAL=5
```

### Security
```env
GUARDRAILS_ENABLED=true
PII_DETECTION_ENABLED=true
CITATION_REQUIRED=true
```

## GPU Support

For local LLM inference with GPU acceleration:

1. **Install NVIDIA Container Toolkit**:
   ```bash
   # Ubuntu/Debian
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
   curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
   curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   sudo apt-get update && sudo apt-get install -y nvidia-docker2
   sudo systemctl restart docker
   ```

2. **Verify GPU access**:
   ```bash
   docker run --rm --gpus all nvidia/cuda:11.8-base-ubuntu20.04 nvidia-smi
   ```

3. **Start with GPU profile**:
   ```bash
   docker-compose --profile local-llm up -d
   ```

## Data Persistence

### Volumes
- `weaviate_data`: Vector database storage
- `vllm_models`: Cached model files
- `zep_db_data`: Memory database storage
- `langfuse_db_data`: Observability database storage
- `redis_data`: Cache storage (optional)

### Local Directories
- `./data/uploads`: Document upload storage
- `./data/cache`: Application cache
- `./logs`: Application logs

## Health Checks

All services include health checks with automatic restart policies:

- **app**: HTTP health endpoint check
- **weaviate**: Ready endpoint check
- **vllm**: Health endpoint check (local mode)
- **zep**: Health endpoint check
- **langfuse**: Health endpoint check
- **databases**: PostgreSQL ready checks

## Scaling

### Horizontal Scaling
For production deployments:

```bash
# Scale app service
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --scale app=3

# Use Docker Swarm for multi-node deployment
docker stack deploy -c docker-compose.yml -c docker-compose.prod.yml rag-stack
```

### Resource Limits
Production configuration includes resource limits:
- **app**: 2 CPU, 4GB RAM
- **weaviate**: 4 CPU, 8GB RAM  
- **vllm**: 8 CPU, 16GB RAM + GPU
- **databases**: 2 CPU, 4GB RAM each

## Monitoring

### Health Monitoring
```bash
# Check service health
docker-compose ps

# View logs
docker-compose logs -f app
docker-compose logs -f weaviate
```

### Metrics Collection
- **Langfuse**: Application tracing and metrics at http://localhost:3000
- **Weaviate**: Prometheus metrics at http://localhost:2112 (dev mode)
- **System**: Docker stats via `docker stats`

## Security

### Production Security
1. **Change default passwords** in `.env`
2. **Enable authentication** for Weaviate:
   ```env
   WEAVIATE_API_KEY=your-secure-api-key
   ```
3. **Configure TLS** with nginx reverse proxy
4. **Enable rate limiting** via nginx configuration
5. **Use secrets management** for sensitive environment variables

### Network Security
- Services communicate via internal Docker network
- Only necessary ports exposed to host
- Nginx reverse proxy for production traffic

## Troubleshooting

### Common Issues

1. **GPU not detected**:
   ```bash
   # Check NVIDIA runtime
   docker info | grep nvidia
   
   # Verify GPU access
   docker run --rm --gpus all nvidia/cuda:11.8-base-ubuntu20.04 nvidia-smi
   ```

2. **Model download issues**:
   ```bash
   # Check vLLM logs
   docker-compose logs vllm
   
   # Manually download model
   docker-compose exec vllm huggingface-cli download microsoft/WizardLM-2-7B
   ```

3. **Memory issues**:
   ```bash
   # Increase Docker memory limits
   # Adjust GPU memory utilization in .env
   VLLM_GPU_MEMORY_UTILIZATION=0.8
   ```

4. **Connection refused**:
   ```bash
   # Check service status
   docker-compose ps
   
   # Restart services
   docker-compose restart
   ```

### Log Analysis
```bash
# Application logs
docker-compose logs -f app

# Database logs
docker-compose logs zep_db langfuse_db

# All service logs
docker-compose logs -f
```

## Development

### Local Development
```bash
# Development mode with hot reload
docker-compose -f docker-compose.yml -f docker-compose.override.yml up -d

# Run tests
docker-compose exec app pytest

# Access development shell
docker-compose exec app bash
```

### Configuration Testing
```bash
# Validate docker-compose configuration
docker-compose config

# Test specific profiles
docker-compose --profile local-llm config
```

## Backup and Recovery

### Database Backups
```bash
# Backup Zep database
docker-compose exec zep_db pg_dump -U zep_user zep_db > backup_zep.sql

# Backup Langfuse database  
docker-compose exec langfuse_db pg_dump -U langfuse_user langfuse_db > backup_langfuse.sql

# Backup Weaviate data (filesystem)
docker run --rm -v rag_weaviate_data:/data -v $(pwd):/backup alpine tar czf /backup/weaviate_backup.tar.gz -C /data .
```

### Restore
```bash
# Restore database
docker-compose exec -T zep_db psql -U zep_user zep_db < backup_zep.sql

# Restore Weaviate
docker run --rm -v rag_weaviate_data:/data -v $(pwd):/backup alpine tar xzf /backup/weaviate_backup.tar.gz -C /data
```

## Support

For issues and questions:
1. Check the [troubleshooting section](#troubleshooting)
2. Review service logs
3. Consult the main project documentation
4. Submit issues to the project repository