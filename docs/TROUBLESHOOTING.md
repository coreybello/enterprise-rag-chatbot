# Troubleshooting Guide

## 🚨 Common Issues and Solutions

This guide covers common problems you might encounter when setting up, running, or using the Agentic RAG system, along with step-by-step solutions.

## Table of Contents

- [Installation Issues](#installation-issues)
- [Docker Problems](#docker-problems)
- [API and Backend Issues](#api-and-backend-issues)
- [Frontend Issues](#frontend-issues)
- [Database Issues](#database-issues)
- [LLM Provider Issues](#llm-provider-issues)
- [Performance Issues](#performance-issues)
- [Network and Connectivity](#network-and-connectivity)

## Installation Issues

### Python Dependency Problems

**Problem**: `pip install` fails with dependency conflicts
```bash
# Solution: Use a clean virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Problem**: Missing system dependencies
```bash
# On Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev python3-venv build-essential

# On macOS with Homebrew
brew install python3
```

### Node.js Issues

**Problem**: `npm install` fails or has permission issues
```bash
# Solution: Clear cache and reinstall
npm cache clean --force
rm -rf node_modules/ package-lock.json
npm install
```

**Problem**: Node.js version incompatible
```bash
# Check Node version
node --version

# Use nvm to manage versions
nvm install 18
nvm use 18
```

## Docker Problems

### Docker Compose Issues

**Problem**: `docker-compose` command not found
```bash
# Install Docker Compose
sudo apt-get install docker-compose-plugin  # Ubuntu/Debian
# or
brew install docker-compose  # macOS
```

**Problem**: Permission denied errors
```bash
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker
```

**Problem**: Port conflicts
```bash
# Change ports in docker-compose.yml or .env
services:
  app:
    ports:
      - "8001:8000"  # Change host port
```

### Container Issues

**Problem**: Containers won't start
```bash
# Check logs
docker-compose logs

# Restart services
docker-compose down
docker-compose up -d

# Force rebuild
docker-compose up -d --build
```

**Problem**: Out of memory errors
```bash
# Increase Docker memory allocation
# Docker Desktop: Settings → Resources → Memory
# Or reduce service memory usage in compose file
```

## API and Backend Issues

### Server Won't Start

**Problem**: FastAPI server fails to start
```bash
# Check for missing environment variables
cp .env.example .env
# Fill in required values

# Check Python dependencies
pip install -r requirements.txt
```

**Problem**: Import errors or module not found
```bash
# Ensure you're in the correct directory
cd /path/to/agentic-rag

# Check Python path
export PYTHONPATH=/path/to/agentic-rag:$PYTHONPATH
```

### Authentication Issues

**Problem**: JWT token errors
```bash
# Set a strong JWT secret
echo "JWT_SECRET=$(openssl rand -hex 32)" >> .env

# Restart services
docker-compose restart
```

**Problem**: CORS errors
```bash
# Check CORS settings in configuration
# Ensure frontend URL is in allowed origins
CORS_ORIGINS=["http://localhost:3000","https://your-domain.com"]
```

## Frontend Issues

### Build Failures

**Problem**: `npm run build` fails
```bash
# Clear cache and dependencies
rm -rf node_modules/ .next/
npm install
npm run build
```

**Problem**: TypeScript compilation errors
```bash
# Check TypeScript configuration
npm run type-check

# Fix type issues or adjust tsconfig.json
```

### Runtime Errors

**Problem**: White screen or blank page
```bash
# Check browser console for errors
# Verify API endpoints are accessible
```

**Problem**: Styling issues
```bash
# Ensure Tailwind CSS is properly configured
# Check that styles are being imported
```

## Database Issues

### Connection Problems

**Problem**: Database connection refused
```bash
# Check database service is running
docker-compose ps

# Verify connection string in .env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

**Problem**: Migration errors
```bash
# Run migrations manually
docker-compose exec app alembic upgrade head

# Or reset database (development only)
docker-compose down -v
docker-compose up -d
```

### Performance Issues

**Problem**: Slow database queries
```bash
# Check database indexes
# Enable query logging for analysis
# Consider adding appropriate indexes
```

## LLM Provider Issues

### Local LLM (vLLM) Problems

**Problem**: vLLM service won't start
```bash
# Check GPU availability
nvidia-smi  # For NVIDIA GPUs

# Use CPU-only mode if no GPU
VLLM_DEVICE=cpu
```

**Problem**: Model download failures
```bash
# Check internet connection
# Verify model name is correct
# Manual download option:
docker-compose exec vllm huggingface-cli download model-name
```

### OpenRouter Issues

**Problem**: API key errors
```bash
# Verify OpenRouter API key
echo $OPENROUTER_API_KEY

# Check API key validity
curl -H "Authorization: Bearer $OPENROUTER_API_KEY" https://openrouter.ai/api/v1/auth/key
```

**Problem**: Rate limiting
```bash
# Implement retry logic
# Consider caching responses
# Upgrade plan if needed
```

## Performance Issues

### Slow Response Times

**Problem**: High latency in responses
```bash
# Check system resources
docker stats

# Optimize chunking settings
CHUNK_SIZE=512
CHUNK_OVERLAP=50

# Enable caching
REDIS_URL=redis://localhost:6379
```

**Problem**: Memory usage too high
```bash
# Adjust service memory limits in compose file
# Enable garbage collection
# Optimize batch sizes
```

### Scaling Issues

**Problem**: System can't handle load
```bash
# Scale horizontally
docker-compose up -d --scale app=3

# Add load balancer
# Optimize database queries
```

## Network and Connectivity

### Firewall Issues

**Problem**: Services can't communicate
```bash
# Check firewall settings
sudo ufw status

# Allow necessary ports
sudo ufw allow 3000  # Frontend
sudo ufw allow 8000  # Backend
sudo ufw allow 8080  # Weaviate
```

### DNS Issues

**Problem**: Hostname resolution failures
```bash
# Use IP addresses in development
# Check /etc/hosts for localhost mapping
# Use service names in Docker network
```

## Logging and Debugging

### Enable Debug Logging

**Problem**: Need more detailed logs
```bash
# Set debug environment variable
LOG_LEVEL=DEBUG

# Or for specific components
LOG_LEVEL_APP=DEBUG
LOG_LEVEL_DB=DEBUG
```

### Viewing Logs

```bash
# View all service logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f app
docker-compose logs -f frontend
docker-compose logs -f weaviate

# Follow logs in real-time
docker-compose logs -f --tail=100
```

## Getting Help

### When to Seek Additional Help

1. **Check Documentation First**
   - [API Documentation](API.md)
   - [Deployment Guide](DEPLOYMENT.md)
   - [Configuration Reference](CONFIGURATION.md)

2. **Search Existing Issues**
   - [GitHub Issues](https://github.com/your-org/agentic-rag/issues)
   - Check if your problem has been reported before

3. **Gather Information for Support**
   ```bash
   # System information
   docker --version
   docker-compose --version
   python --version
   node --version
   
   # Service status
   docker-compose ps
   
   # Relevant logs
   docker-compose logs --tail=50
   ```

4. **Create a Support Request**
   - Include error messages and logs
   - Describe steps to reproduce
   - Share your configuration (redact secrets)

### Emergency Contacts

- **Technical Support**: support@your-company.com
- **Security Issues**: security@your-company.com
- **GitHub Issues**: [Create new issue](https://github.com/your-org/agentic-rag/issues/new)

---

*This troubleshooting guide is maintained by the development team. Please contribute your solutions and experiences to help others.*