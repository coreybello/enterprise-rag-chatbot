# API Documentation

## Overview

The Agentic RAG API provides a comprehensive set of endpoints for building retrieval-augmented generation applications. The API is built using FastAPI with enterprise features including authentication, middleware, WebSocket support, and comprehensive error handling.

## Base URL

The API is served from the root path `/`. All endpoints are prefixed with `/api/v1/` for versioning.

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your_token>
```

## Endpoints

### Health Check

**GET /api/health**
- Returns the health status of the application
- Response: `{"status": "healthy", "timestamp": "2023-01-01T00:00:00Z"}`

### RAG Endpoints

**POST /api/rag/query**
- Submit a query for retrieval-augmented generation
- Request body: `{"query": "your question", "context": "optional context"}`
- Response: `{"answer": "generated response", "sources": ["source1", "source2"]}`

**POST /api/rag/ingest**
- Ingest new documents into the vector database
- Request body: `{"documents": [{"id": "doc1", "content": "document content"}]}`
- Response: `{"status": "success", "ingested_count": 1}`

### Management Endpoints

**GET /api/management/status**
- Get system status and metrics
- Response: System status information

**POST /api/management/restart**
- Restart specific services (admin only)
- Request body: `{"service": "service_name"}`

### Analytics Endpoints

**GET /api/analytics/usage**
- Get usage statistics
- Query parameters: `start_date`, `end_date`
- Response: Usage statistics data

## WebSocket Support

**WS /api/ws/chat**
- Real-time chat interface for streaming responses
- Messages: `{"type": "message", "content": "user input"}`
- Responses: Streamed messages with type `response`

## Error Handling

The API returns standard HTTP status codes:

- `200 OK`: Successful request
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Rate Limiting

API requests are rate limited to prevent abuse. Check response headers for rate limit information:

- `X-RateLimit-Limit`: Maximum requests per period
- `X-RateLimit-Remaining`: Remaining requests
- `X-RateLimit-Reset`: Time when limit resets

## Examples

### Python Client Example

```python
import requests

BASE_URL = "http://localhost:8000/api/v1"
headers = {"Authorization": "Bearer your_token"}

# Health check
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# RAG query
data = {"query": "What is retrieval-augmented generation?"}
response = requests.post(f"{BASE_URL}/rag/query", json=data, headers=headers)
print(response.json())
```

### cURL Example

```bash
# Health check
curl -X GET http://localhost:8000/api/v1/health

# RAG query with authentication
curl -X POST http://localhost:8000/api/v1/rag/query \
  -H "Authorization: Bearer your_token" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is RAG?"}'
```

## Versioning

The API uses semantic versioning. The current version is v1. Backward compatibility will be maintained within major versions.

## Deprecation Policy

Endpoints marked for deprecation will continue to work for at least one major version before being removed. Deprecation notices will be included in response headers and documentation.