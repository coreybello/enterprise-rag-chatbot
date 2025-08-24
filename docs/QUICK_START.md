# Quick Start Guide

## 🚀 Get Up and Running in 5 Minutes

This guide provides the fastest way to get the Agentic RAG system running for development and testing purposes.

## Prerequisites Checklist

- [ ] **Python 3.8+** installed
- [ ] **Node.js 18+** installed  
- [ ] **Docker & Docker Compose** installed
- [ ] **Git** installed

## Option 1: Docker Compose (Recommended)

### Step 1: Clone and Configure
```bash
# Clone the repository
git clone https://github.com/your-org/agentic-rag.git
cd agentic-rag

# Copy environment configuration
cp deploy/compose/.env.example deploy/compose/.env
```

### Step 2: Start Services
```bash
# Start all services with local LLM support
docker-compose -f deploy/compose/docker-compose.yml --profile local-llm up -d
```

### Step 3: Verify Installation
```bash
# Check service status
docker-compose ps

# View logs
docker-compose logs -f app
```

### Step 4: Access the Application
- **Frontend**: http://localhost:3000
- **API Documentation**: http://localhost:8000/docs
- **Weaviate Console**: http://localhost:8080
- **Langfuse Dashboard**: http://localhost:3000

## Option 2: Local Development Setup

### Backend Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Start backend server
python -m src.app.main
```

### Frontend Setup
```bash
# Install dependencies
cd frontend
npm install

# Start development server
npm run dev
```

## Quick Configuration

### Minimal .env Configuration
```env
# LLM Provider (choose one)
LLM_PROVIDER=local        # Use local vLLM
# LLM_PROVIDER=openrouter  # Use OpenRouter API

# Local LLM Settings (if using local)
VLLM_BASE_URL=http://localhost:8001
VLLM_MODEL_NAME=microsoft/DialoGPT-medium

# OpenRouter Settings (if using OpenRouter)
OPENROUTER_API_KEY=your-api-key-here
OPENROUTER_MODEL_NAME=anthropic/claude-3-sonnet

# Vector Database
VECTOR_DB_PROVIDER=weaviate
WEAVIATE_URL=http://localhost:8080

# Basic Security
JWT_SECRET=your-super-secret-jwt-key-here
```

## First Steps After Installation

### 1. Test the API
```bash
# Health check
curl http://localhost:8000/api/v1/health

# Test chat endpoint
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, how does this work?", "use_rag": false}'
```

### 2. Upload a Document
```bash
# Upload a sample document
curl -X POST http://localhost:8000/api/v1/documents/upload \
  -F "file=@path/to/your/document.pdf" \
  -F "auto_process=true"
```

### 3. Try RAG Query
```bash
# Ask a question using RAG
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is our remote work policy?", "use_rag": true}'
```

## Common Quick Issues

### Port Conflicts
If ports are already in use:
```bash
# Change ports in .env
APP_PORT=8001
FRONTEND_PORT=3001
```

### Docker Permissions
```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

### Model Download Issues
```bash
# Check vLLM logs
docker-compose logs vllm

# Manual model download
docker-compose exec vllm huggingface-cli download microsoft/DialoGPT-medium
```

## Next Steps

1. **Explore API Documentation** at http://localhost:8000/docs
2. **Configure authentication** in the frontend
3. **Upload your documents** for testing
4. **Review security settings** for production readiness
5. **Check out the full documentation** for advanced features

## Need Help?

- Check the [Troubleshooting Guide](TROUBLESHOOTING.md)
- Review service logs: `docker-compose logs -f`
- Visit the [API Documentation](http://localhost:8000/docs)
- Check [GitHub Issues](https://github.com/your-org/agentic-rag/issues)

---

*This quick start guide is designed to get you running quickly. For production deployment, please refer to the full [Deployment Guide](DEPLOYMENT.md).*