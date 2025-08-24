# Development Guide

This guide covers setting up the development environment, contributing to the project, and understanding the development workflow for the Agentic RAG application.

## Table of Contents

- [Development Environment Setup](#development-environment-setup)
- [Project Structure](#project-structure)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Debugging](#debugging)
- [Contributing](#contributing)
- [Code Review Process](#code-review-process)

## Development Environment Setup

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL (for local development)
- Redis (optional, for caching)
- Git

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd agentic-rag
   ```

2. **Set up Python environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Unix/MacOS:
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

3. **Set up frontend:**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Configure environment:**
   ```bash
   # Copy example environment file
   cp .env.example .env
   
   # Edit .env with your configuration
   # Required: DATABASE_URL, JWT_SECRET, OPENAI_API_KEY
   ```

5. **Initialize database:**
   ```bash
   # Run migrations
   alembic upgrade head
   ```

6. **Start development servers:**
   ```bash
   # Backend (terminal 1)
   python start_server.py
   
   # Frontend (terminal 2)
   cd frontend
   npm run dev
   ```

## Project Structure

```
agentic-rag/
├── src/                    # Backend source code
│   ├── app/               # Main FastAPI application
│   │   ├── api/           # API routes and endpoints
│   │   ├── models/        # Database models
│   │   ├── providers/     # LLM provider implementations
│   │   └── utils/         # Utility functions
│   └── tests/             # Backend tests
├── frontend/              # React frontend
│   ├── src/
│   │   ├── app/           # Next.js app directory
│   │   ├── components/    # React components
│   │   ├── hooks/         # Custom React hooks
│   │   └── lib/           # Utility libraries
│   └── tests/             # Frontend tests
├── config/                # Configuration files
├── docs/                  # Documentation
├── deploy/                # Deployment configurations
└── scripts/               # Development and deployment scripts
```

## Coding Standards

### Python Code Style

- Follow PEP 8 guidelines
- Use type hints for all function signatures
- Maximum line length: 88 characters (Black formatting)
- Use descriptive variable and function names

### JavaScript/TypeScript Style

- Use TypeScript for all new code
- Follow Airbnb JavaScript style guide
- Use functional components with hooks
- Prefer async/await over promises

### Git Commit Messages

Use conventional commit format:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types: feat, fix, docs, style, refactor, test, chore

### Code Organization

- Keep files under 500 lines
- Functions should have single responsibility
- Use dependency injection for testability
- Document public APIs with docstrings

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_module.py

# Run with coverage
pytest --cov=src tests/

# Frontend tests
cd frontend
npm test
npm run test:e2e
```

### Test Structure

- **Unit tests**: Test individual functions and classes
- **Integration tests**: Test component interactions
- **E2E tests**: Test complete user flows

### Writing Tests

- Write tests before implementing features (TDD)
- Use descriptive test names
- Mock external dependencies
- Test edge cases and error conditions

## Debugging

### Backend Debugging

```bash
# Run with debug mode
python -m debugpy --listen 0.0.0.0:5678 start_server.py

# Use VS Code debug configuration
# Add breakpoints in your code
```

### Frontend Debugging

```bash
# Start development server with debug
npm run dev

# Use browser developer tools
# React DevTools extension recommended
```

### Logging

Configure log level in `.env`:
```
LOG_LEVEL=DEBUG
```

View logs in real-time:
```bash
# Backend logs
tail -f app.log

# Docker logs
docker-compose logs -f
```

## Contributing

### Workflow

1. **Create a feature branch:**
   ```bash
   git checkout -b feat/your-feature-name
   ```

2. **Make your changes:**
   - Follow coding standards
   - Write tests for new functionality
   - Update documentation

3. **Run tests:**
   ```bash
   pytest
   cd frontend && npm test
   ```

4. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat(module): description of changes"
   ```

5. **Push and create PR:**
   ```bash
   git push origin feat/your-feature-name
   # Create pull request on GitHub
   ```

### Pull Request Checklist

- [ ] Tests pass
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Changes are focused and minimal

## Code Review Process

### Review Guidelines

- Focus on code quality and maintainability
- Check for security vulnerabilities
- Verify test coverage
- Ensure documentation is clear

### Review Comments

- Be constructive and specific
- Suggest alternatives when possible
- Reference relevant standards or patterns
- Use GitHub review features

## Performance Considerations

### Backend Optimization

- Use async/await for I/O operations
- Implement caching for expensive operations
- Optimize database queries
- Monitor memory usage

### Frontend Optimization

- Code splitting for large bundles
- Lazy loading of components
- Optimize images and assets
- Minimize re-renders

## Troubleshooting

### Common Issues

1. **Database connection errors:**
   - Verify DATABASE_URL in .env
   - Check if database server is running

2. **Module import errors:**
   - Check Python path
   - Verify virtual environment activation

3. **Frontend build errors:**
   - Clear node_modules and reinstall
   - Check Node.js version compatibility

### Getting Help

- Check existing documentation
- Search GitHub issues
- Ask in team channels
- Create a detailed bug report

## Continuous Integration

The project uses GitHub Actions for CI/CD:

- Automated testing on pull requests
- Code quality checks
- Security scanning
- Deployment to staging environment

## Dependencies Management

### Python Dependencies

```bash
# Add new dependency
pip install package
pip freeze > requirements.txt

# Add development dependency
pip install package
pip freeze > requirements-dev.txt
```

### Node.js Dependencies

```bash
# Add production dependency
npm install package

# Add development dependency
npm install --save-dev package
```

### Security Updates

- Regularly update dependencies
- Use dependabot for automated updates
- Scan for vulnerabilities