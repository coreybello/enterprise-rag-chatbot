# Deployment Guide

This guide covers deploying the Agentic RAG application in various environments, including local development, production with Docker, and cloud platforms.

## Table of Contents

- [Local Development](#local-development)
- [Docker Deployment](#docker-deployment)
- [Production Deployment](#production-deployment)
- [Environment Variables](#environment-variables)
- [Monitoring and Logging](#monitoring-and-logging)

## Local Development

### Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL (optional, for production-like setup)
- Redis (optional, for caching)

### Setup Steps

1. **Clone and install dependencies:**
   ```bash
   git clone <repository-url>
   cd agentic-rag
   pip install -r requirements.txt
   cd frontend
   npm install
   ```

2. **Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/ragdb
   REDIS_URL=redis://localhost:6379
   JWT_SECRET=your-secret-key
   OPENAI_API_KEY=your-openai-key
   ```

3. **Start the services:**
   ```bash
   # Start backend
   python start_server.py
   
   # Start frontend (in separate terminal)
   cd frontend
   npm run dev
   ```

## Docker Deployment

### Using Docker Compose

The project includes a comprehensive Docker Compose setup for development and production:

1. **Build and start containers:**
   ```bash
   docker-compose -f deploy/compose/docker-compose.yml up --build
   ```

2. **Environment-specific configurations:**
   - Development: Uses local volumes for hot reloading
   - Production: Optimized build with minimal layers

### Dockerfile Configuration

The application uses multi-stage Docker builds:

- **Backend Dockerfile**: Located in the root directory
- **Frontend Dockerfile**: Located in the frontend directory

### Health Checks

Docker Compose includes health checks for all services:
- API service health endpoint: `/api/health`
- Database connection verification
- Cache service connectivity

## Production Deployment

### Cloud Deployment Options

#### AWS ECS/EKS
1. Build Docker images
2. Push to ECR
3. Deploy using ECS task definitions or EKS manifests

#### Google Cloud Run
1. Build and push container
2. Deploy with Cloud Run configuration

#### Azure Container Apps
1. Build and push container
2. Deploy using Azure Container Apps

### Environment Configuration

Create environment-specific configs in `config/environments/`:

- `production.yaml`: Production settings
- `staging.yaml`: Staging environment
- `development.yaml`: Development settings

### Database Setup

For production databases:

1. **PostgreSQL:**
   ```yaml
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```

2. **Redis for caching:**
   ```yaml
   REDIS_URL=redis://host:6379
   ```

## Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `postgresql://user:pass@host/db` |
| `JWT_SECRET` | Secret for JWT token generation | `your-secret-key` |
| `OPENAI_API_KEY` | OpenAI API key | `sk-...` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Application port | `8000` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `CACHE_TTL` | Cache time-to-live | `300` |

## Monitoring and Logging

### Logging Configuration

Configure logging in `config/logging.yaml`:

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
  file:
    class: logging.FileHandler
    filename: app.log
    formatter: simple
```

### Health Checks

Implement health checks for:
- Database connectivity
- External API availability
- Cache service status

### Metrics and Monitoring

- Prometheus metrics endpoint: `/metrics`
- Grafana dashboards for visualization
- Alerting rules for critical services

## Scaling

### Horizontal Scaling

- Use load balancers for API services
- Implement database connection pooling
- Configure Redis cluster for distributed caching

### Performance Optimization

- Enable Gzip compression
- Configure CDN for static assets
- Implement query caching
- Optimize database indexes

## Backup and Recovery

### Database Backups

```bash
# PostgreSQL backup
pg_dump -h host -U user dbname > backup.sql

# Restore
psql -h host -U user dbname < backup.sql
```

### Configuration Backups

- Version control all configuration files
- Regular backups of environment configurations
- Document all deployment changes

## Troubleshooting

### Common Issues

1. **Port conflicts**: Change default ports in configuration
2. **Database connections**: Verify connection strings and network access
3. **Memory issues**: Monitor container memory usage and adjust limits

### Log Analysis

Check application logs for:
- Authentication errors
- Database connection issues
- External API failures

## Security Considerations

- Use HTTPS in production
- Regular security updates
- Network segmentation
- Access control policies

## Updates and Maintenance

### Version Updates

1. Test updates in staging environment
2. Follow semantic versioning
3. Maintain changelog

### Regular Maintenance

- Monitor performance metrics
- Review security patches
- Update dependencies regularly