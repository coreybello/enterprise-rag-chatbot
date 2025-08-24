# Agentic RAG Documentation

Welcome to the Agentic RAG (Retrieval-Augmented Generation) application documentation. This project provides a comprehensive platform for building and deploying retrieval-augmented generation systems with enterprise-grade features.

## Documentation Index

For a comprehensive and organized view of all documentation, see the **[Documentation Hub](INDEX.md)**.

### Core Documentation
- **[API Documentation](API.md)** - Complete API reference with endpoints, examples, and authentication details
- **[Deployment Guide](DEPLOYMENT.md)** - Instructions for deploying in various environments including local, Docker, and cloud platforms
- **[Development Guide](DEVELOPMENT.md)** - Setup instructions, coding standards, and contribution guidelines
- **[Architecture Overview](ARCHITECTURE.md)** - System architecture, components, and design decisions
- **[Security Guidelines](SECURITY.md)** - Security best practices, authentication, and compliance
- **[System Overview](OVERVIEW.md)** - High-level introduction to the Agentic RAG system

### Role-Based Guides
- **[Developer Onboarding](roles/DEVELOPER.md)** - Step-by-step setup for new developers
- **[Frontend Developer Guide](roles/FRONTEND.md)** - Frontend-specific development practices
- **[DevOps Engineer Guide](roles/DEVOPS.md)** - Infrastructure and deployment responsibilities
- **[Security Engineer Guide](roles/SECURITY.md)** - Security monitoring and incident response

### Reference
- **[Configuration Reference](CONFIGURATION.md)** - All configuration options and environment variables
- **[Troubleshooting Guide](TROUBLESHOOTING.md)** - Common issues and solutions
- **[FAQ](FAQ.md)** - Frequently asked questions and answers

## Quick Links

- [GitHub Repository](https://github.com/your-org/agentic-rag)
- [Issue Tracker](https://github.com/your-org/agentic-rag/issues)
- [Changelog](CHANGELOG.md)

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL (for production)
- Redis (optional, for caching)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/agentic-rag.git
   cd agentic-rag
   ```

2. **Set up the backend:**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Set up the frontend:**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application:**
   ```bash
   # Start backend
   python start_server.py
   
   # Start frontend (in separate terminal)
   cd frontend
   npm run dev
   ```

## Features

- **Retrieval-Augmented Generation**: Combine retrieval systems with generative AI
- **Multiple LLM Providers**: Support for OpenAI, Anthropic, Azure, and custom providers
- **Enterprise Features**: Authentication, authorization, and audit logging
- **Real-time Updates**: WebSocket support for streaming responses
- **Scalable Architecture**: Designed for horizontal scaling and high availability
- **Comprehensive API**: RESTful API with OpenAPI documentation

## Architecture

The application follows a modular architecture:

- **Backend**: FastAPI-based Python application with async support
- **Frontend**: Next.js React application with TypeScript
- **Database**: PostgreSQL for persistent storage
- **Vector Store**: Qdrant for semantic search and retrieval
- **Cache**: Redis for caching and session management

## Support

- **Documentation**: This documentation site
- **Issues**: [GitHub Issues](https://github.com/your-org/agentic-rag/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/agentic-rag/discussions)
- **Email**: support@your-org.com

## Contributing

We welcome contributions! Please see our [Development Guide](DEVELOPMENT.md) for details on how to contribute, including:

- Code style guidelines
- Testing requirements
- Pull request process
- Code review standards

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a history of changes and releases.

---

*Last updated: August 2024*