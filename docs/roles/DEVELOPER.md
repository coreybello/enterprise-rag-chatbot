# Developer Onboarding Guide

## 🎯 Purpose
This guide provides a comprehensive onboarding process for developers joining the Agentic RAG project. It covers environment setup, development workflows, and best practices.

## 🚀 Quick Start for Developers

### 1. Prerequisites
- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **Node.js 18+** - [Download here](https://nodejs.org/)
- **Docker & Docker Compose** - [Installation guide](https://docs.docker.com/get-docker/)
- **Git** - Version control system

### 2. Clone the Repository
```bash
git clone https://github.com/your-org/agentic-rag.git
cd agentic-rag
```

### 3. Environment Setup
```bash
# Set up Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r src/config/requirements.txt
pip install -r requirements-dev.txt  # Development dependencies

# Install frontend dependencies
cd frontend
npm install
cd ..
```

### 4. Configuration
```bash
# Copy environment files
cp .env.example .env
cp deploy/compose/.env.example deploy/compose/.env

# Edit .env files with your local settings
# - Set API keys for external services
# - Configure database connections
# - Adjust performance settings
```

### 5. Start Development Services
```bash
# Option 1: Full stack with Docker Compose
docker-compose -f deploy/compose/docker-compose.yml --profile dev up -d

# Option 2: Backend only (for Python development)
python -m src.main

# Option 3: Frontend only (for React development)
cd frontend
npm run dev
```

## 🛠️ Development Workflow

### Code Structure
```
agentic-rag/
├── src/                 # Python backend
│   ├── config/         # Configuration management
│   ├── guardrails/     # Security and compliance
│   ├── security/       # Access control and encryption
│   └── main.py         # Application entry point
├── frontend/           # Next.js frontend
├── deploy/             # Deployment configurations
└── docs/              # Documentation
```

### Backend Development
```bash
# Run backend tests
pytest src/tests/

# Format Python code
black src/
isort src/

# Type checking
mypy src/

# Linting
flake8 src/
```

### Frontend Development
```bash
cd frontend

# Run frontend tests
npm test

# Format code
npm run format

# Type checking
npm run type-check

# Linting
npm run lint
```

### API Development
- **API Documentation**: http://localhost:8000/docs (when backend is running)
- **OpenAPI Schema**: Available at `/openapi.json`
- **Testing Endpoints**: Use tools like Postman or curl

## 🔧 Common Development Tasks

### Adding New Features
1. Create a feature branch: `git checkout -b feature/your-feature`
2. Implement changes with tests
3. Run tests and ensure they pass
4. Submit a pull request for review

### Debugging
```bash
# Backend debugging
python -m debugpy --listen 5678 -m src.main

# Frontend debugging
cd frontend
npm run dev  # Includes source maps for debugging

# Docker debugging
docker-compose logs -f app  # View backend logs
docker-compose logs -f frontend  # View frontend logs
```

### Database Operations
```bash
# Access database shell
docker-compose exec db psql -U postgres

# Run migrations (if applicable)
alembic upgrade head

# Seed test data
python scripts/seed_data.py
```

## 📚 Learning Resources

### Essential Reading
1. **[Architecture Overview](../OVERVIEW.md)** - High-level system design
2. **[API Documentation](../API_REFERENCE.md)** - Detailed API specifications
3. **[Security Guidelines](../SECURITY.md)** - Security best practices
4. **[Testing Guide](../TESTING.md)** - Testing strategies and examples

### Technology References
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Next.js Documentation**: https://nextjs.org/docs
- **Weaviate Documentation**: https://weaviate.io/developers/weaviate
- **Docker Documentation**: https://docs.docker.com/

## 🎯 Best Practices

### Code Quality
- Write unit tests for all new functionality
- Maintain 80%+ test coverage
- Use type hints throughout Python code
- Follow PEP 8 style guide
- Document complex algorithms and business logic

### Security
- Validate all user inputs
- Use prepared statements for database queries
- Implement proper error handling without exposing sensitive information
- Follow the principle of least privilege

### Performance
- Use async/await for I/O operations
- Implement caching where appropriate
- Monitor memory usage and response times
- Optimize database queries with indexes

## 🔄 Version Control

### Branching Strategy
- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - Feature development branches
- `hotfix/*` - Critical bug fixes

### Commit Messages
Use conventional commit format:
```
feat: add user authentication
fix: resolve memory leak in document processing
docs: update API documentation
test: add unit tests for citation enforcement
```

### Pull Request Process
1. Ensure all tests pass
2. Update documentation if needed
3. Request review from at least one team member
4. Address review comments
5. Squash and merge when approved

## 🐛 Troubleshooting Common Issues

### Dependency Issues
```bash
# Clear Python cache
pip cache purge
rm -rf venv/
python -m venv venv
pip install -r requirements.txt

# Clear npm cache
npm cache clean --force
rm -rf node_modules/
npm install
```

### Docker Issues
```bash
# Reset Docker environment
docker-compose down -v
docker system prune -a
docker-compose up -d

# Check service status
docker-compose ps
docker-compose logs -f
```

### Database Issues
```bash
# Reset database
docker-compose down -v
docker-compose up -d

# Run migrations
docker-compose exec app alembic upgrade head
```

## 📞 Getting Help

### Internal Resources
- **Team Slack Channel**: #agentic-rag-dev
- **Code Review Guidelines**: [Internal Wiki]
- **Architecture Decisions**: [ADR Documentation]

### External Resources
- **Stack Overflow**: Tag with #fastapi #nextjs #weaviate
- **GitHub Issues**: Report bugs and feature requests
- **Documentation**: Always check docs first

### Escalation Path
1. Check existing documentation and issues
2. Ask in team channel
3. Schedule pair programming session
4. Escalate to tech lead if blocked

---

*Welcome to the team! This guide will be updated regularly as the project evolves.*