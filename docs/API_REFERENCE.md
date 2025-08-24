# API Reference

## 📋 Overview

This document provides comprehensive documentation for all API endpoints available in the Agentic RAG system. All endpoints are RESTful and return JSON responses.

## 🔐 Authentication

### Authentication Methods

**JWT Bearer Token**
```http
Authorization: Bearer <your_jwt_token>
```

**API Key** (For programmatic access)
```http
X-API-Key: <your_api_key>
```

### Obtaining Tokens

**Login Endpoint**
```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Refresh Token**
```http
POST /api/v1/auth/refresh
Authorization: Bearer <refresh_token>
```

## 📊 Health & System Status

### Health Check
```http
GET /api/v1/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-08-24T21:40:00Z",
  "services": {
    "database": "connected",
    "vector_db": "connected",
    "llm_provider": "healthy",
    "memory_service": "connected"
  }
}
```

### System Information
```http
GET /api/v1/system/info
```

Response:
```json
{
  "version": "1.0.0",
  "environment": "production",
  "uptime": "5d 12h 30m",
  "memory_usage": "45%",
  "active_connections": 42
}
```

## 💬 Chat & Conversation API

### Send Message
```http
POST /api/v1/chat
Content-Type: application/json
Authorization: Bearer <token>

{
  "message": "What is our remote work policy?",
  "use_rag": true,
  "conversation_id": "optional_conversation_id",
  "stream": false
}
```

Response:
```json
{
  "response": "Based on our company policy, remote work is allowed for all employees...",
  "conversation_id": "conv_12345",
  "sources": [
    {
      "id": "doc_67890",
      "title": "Remote Work Policy 2024",
      "content": "Remote work is permitted for all full-time employees...",
      "similarity": 0.87
    }
  ],
  "metadata": {
    "response_time": 1.2,
    "tokens_used": 150,
    "model": "gpt-4"
  }
}
```

### Streaming Response
```http
POST /api/v1/chat
Content-Type: application/json
Authorization: Bearer <token>

{
  "message": "Explain our vacation policy",
  "use_rag": true,
  "stream": true
}
```

Response (streaming):
```text
data: {"content": "Based", "is_final": false}
data: {"content": " on", "is_final": false}
data: {"content": " our policy", "is_final": false}
data: {"content": "...", "is_final": true}
```

### Get Conversation History
```http
GET /api/v1/conversations/{conversation_id}
Authorization: Bearer <token>
```

Response:
```json
{
  "id": "conv_12345",
  "title": "Remote Work Policy Discussion",
  "messages": [
    {
      "id": "msg_1",
      "role": "user",
      "content": "What is our remote work policy?",
      "timestamp": "2024-08-24T10:30:00Z"
    },
    {
      "id": "msg_2",
      "role": "assistant",
      "content": "Based on our company policy...",
      "timestamp": "2024-08-24T10:30:02Z",
      "sources": [...]
    }
  ],
  "created_at": "2024-08-24T10:30:00Z",
  "updated_at": "2024-08-24T10:30:02Z"
}
```

### List Conversations
```http
GET /api/v1/conversations
Authorization: Bearer <token>
Query Parameters:
  page: 1
  limit: 20
  search: "policy"
```

Response:
```json
{
  "conversations": [
    {
      "id": "conv_12345",
      "title": "Remote Work Policy",
      "message_count": 5,
      "last_message_at": "2024-08-24T10:30:02Z",
      "created_at": "2024-08-24T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 45,
    "pages": 3
  }
}
```

## 📄 Document Management API

### Upload Document
```http
POST /api/v1/documents/upload
Authorization: Bearer <token>
Content-Type: multipart/form-data

file: <file>
auto_process: true
metadata: '{"category": "policy", "department": "hr"}'
```

Response:
```json
{
  "id": "doc_67890",
  "filename": "remote-work-policy.pdf",
  "status": "processing",
  "size": 1048576,
  "uploaded_at": "2024-08-24T10:25:00Z",
  "metadata": {
    "category": "policy",
    "department": "hr"
  }
}
```

### Get Document Status
```http
GET /api/v1/documents/{document_id}
Authorization: Bearer <token>
```

Response:
```json
{
  "id": "doc_67890",
  "filename": "remote-work-policy.pdf",
  "status": "processed",
  "size": 1048576,
  "chunk_count": 15,
  "processed_at": "2024-08-24T10:26:30Z",
  "metadata": {
    "category": "policy",
    "department": "hr"
  }
}
```

### List Documents
```http
GET /api/v1/documents
Authorization: Bearer <token>
Query Parameters:
  page: 1
  limit: 20
  status: processed
  category: policy
  search: "remote work"
```

Response:
```json
{
  "documents": [
    {
      "id": "doc_67890",
      "filename": "remote-work-policy.pdf",
      "status": "processed",
      "size": 1048576,
      "chunk_count": 15,
      "uploaded_at": "2024-08-24T10:25:00Z",
      "metadata": {
        "category": "policy",
        "department": "hr"
      }
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 125,
    "pages": 7
  }
}
```

### Delete Document
```http
DELETE /api/v1/documents/{document_id}
Authorization: Bearer <token>
```

Response:
```json
{
  "success": true,
  "message": "Document deleted successfully"
}
```

## 🔍 Search API

### Semantic Search
```http
POST /api/v1/search
Content-Type: application/json
Authorization: Bearer <token>

{
  "query": "remote work policy",
  "filters": {
    "category": "policy",
    "department": "hr"
  },
  "limit": 10,
  "similarity_threshold": 0.7
}
```

Response:
```json
{
  "results": [
    {
      "id": "chunk_abc123",
      "document_id": "doc_67890",
      "content": "Remote work is permitted for all full-time employees...",
      "similarity": 0.87,
      "metadata": {
        "document_title": "Remote Work Policy 2024",
        "category": "policy",
        "page_number": 3
      }
    }
  ],
  "total_results": 15,
  "search_time": 0.45
}
```

### Hybrid Search (Vector + BM25)
```http
POST /api/v1/search/hybrid
Content-Type: application/json
Authorization: Bearer <token>

{
  "query": "remote work policy",
  "vector_weight": 0.7,
  "bm25_weight": 0.3,
  "limit": 10
}
```

## 👥 User Management API

### Get Current User
```http
GET /api/v1/users/me
Authorization: Bearer <token>
```

Response:
```json
{
  "id": "user_123",
  "username": "johndoe",
  "email": "john@company.com",
  "role": "admin",
  "permissions": ["read", "write", "delete"],
  "created_at": "2024-01-15T08:00:00Z",
  "last_login": "2024-08-24T09:30:00Z"
}
```

### Update User Profile
```http
PUT /api/v1/users/me
Content-Type: application/json
Authorization: Bearer <token>

{
  "email": "newemail@company.com",
  "preferences": {
    "theme": "dark",
    "notifications": true
  }
}
```

### List Users (Admin Only)
```http
GET /api/v1/users
Authorization: Bearer <token>
Query Parameters:
  page: 1
  limit: 20
  role: admin
```

## 📊 Analytics API

### Usage Statistics
```http
GET /api/v1/analytics/usage
Authorization: Bearer <token>
Query Parameters:
  start_date: 2024-08-01
  end_date: 2024-08-24
  granularity: daily
```

Response:
```json
{
  "period": {
    "start": "2024-08-01",
    "end": "2024-08-24"
  },
  "metrics": {
    "total_queries": 1245,
    "unique_users": 45,
    "avg_response_time": 1.2,
    "success_rate": 98.7
  },
  "daily_breakdown": [
    {
      "date": "2024-08-24",
      "queries": 67,
      "users": 12,
      "avg_response_time": 1.1
    }
  ]
}
```

### System Metrics
```http
GET /api/v1/analytics/system
Authorization: Bearer <token>
```

Response:
```json
{
  "timestamp": "2024-08-24T21:45:00Z",
  "cpu_usage": 45.2,
  "memory_usage": 62.1,
  "disk_usage": 35.7,
  "active_connections": 23,
  "queue_size": 5
}
```

## ⚙️ Configuration API

### Get Configuration
```http
GET /api/v1/config
Authorization: Bearer <token>
```

Response:
```json
{
  "llm_provider": "openrouter",
  "vector_db": "weaviate",
  "embedding_model": "text-embedding-3-small",
  "chunking_strategy": "semantic",
  "similarity_threshold": 0.7
}
```

### Update Configuration (Admin Only)
```http
PUT /api/v1/config
Content-Type: application/json
Authorization: Bearer <token>

{
  "similarity_threshold": 0.8,
  "chunk_size": 1200
}
```

## 🛡️ Security API

### Audit Logs
```http
GET /api/v1/audit/logs
Authorization: Bearer <token>
Query Parameters:
  start_date: 2024-08-01
  end_date: 2024-08-24
  action: login
  user_id: user_123
```

Response:
```json
{
  "logs": [
    {
      "id": "log_abc123",
      "timestamp": "2024-08-24T09:30:00Z",
      "user_id": "user_123",
      "action": "login",
      "ip_address": "192.168.1.100",
      "user_agent": "Mozilla/5.0...",
      "status": "success"
    }
  ],
  "total": 1345
}
```

### Security Events
```http
GET /api/v1/security/events
Authorization: Bearer <token>
```

## 🔧 Provider Management API

### Provider Health
```http
GET /api/v1/providers/health
Authorization: Bearer <token>
```

Response:
```json
{
  "overall_status": "healthy",
  "providers": {
    "vllm": {
      "status": "healthy",
      "response_time": 0.8,
      "success_rate": 99.2
    },
    "openrouter": {
      "status": "healthy",
      "response_time": 1.2,
      "success_rate": 98.7
    }
  }
}
```

### Test Provider
```http
POST /api/v1/providers/test/{provider}
Authorization: Bearer <token>
```

## 📝 Error Responses

### Common Error Codes

**400 Bad Request**
```json
{
  "error": "validation_error",
  "message": "Invalid input data",
  "details": {
    "field": "email",
    "error": "Invalid email format"
  }
}
```

**401 Unauthorized**
```json
{
  "error": "unauthorized",
  "message": "Invalid or expired token"
}
```

**403 Forbidden**
```json
{
  "error": "forbidden",
  "message": "Insufficient permissions"
}
```

**404 Not Found**
```json
{
  "error": "not_found",
  "message": "Resource not found"
}
```

**429 Too Many Requests**
```json
{
  "error": "rate_limit_exceeded",
  "message": "Too many requests",
  "retry_after": 60
}
```

**500 Internal Server Error**
```json
{
  "error": "internal_error",
  "message": "Internal server error"
}
```

## 🚀 Rate Limits

### Default Limits
- **Authenticated users**: 100 requests per minute
- **API keys**: 1000 requests per minute
- **Upload endpoints**: 10 requests per minute

### Headers
- `X-RateLimit-Limit`: Total requests allowed
- `X-RateLimit-Remaining`: Requests remaining
- `X-RateLimit-Reset`: Time when limit resets

## 📡 WebSocket API

### Connection
```javascript
const ws = new WebSocket('ws://localhost:8000/api/v1/ws');
```

### Events
- `connect`: Connection established
- `message`: New message received
- `error`: Connection error
- `close`: Connection closed

### Authentication
Send authentication message after connection:
```json
{
  "type": "auth",
  "token": "your_jwt_token"
}
```

## 📋 Pagination

All list endpoints support pagination:

### Query Parameters
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 20, max: 100)
- `sort`: Field to sort by
- `order`: asc or desc

### Response Format
```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 145,
    "pages": 8
  }
}
```

## 🔗 Related Documentation

- [Configuration Reference](CONFIGURATION.md) - Environment variables and settings
- [Deployment Guide](DEPLOYMENT.md) - API deployment instructions
- [Security Guidelines](SECURITY.md) - Authentication and security practices

---

*This API reference is automatically generated from the OpenAPI specification. For the most up-to-date information, visit `/docs` when the API is running.*