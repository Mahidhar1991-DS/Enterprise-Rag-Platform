# Enterprise RAG Platform

An enterprise-grade Retrieval-Augmented Generation (RAG) platform built using Python, FastAPI, FAISS, and OpenAI. The platform provides intelligent document ingestion, semantic search, document versioning, asynchronous processing, monitoring, and analytics for enterprise knowledge management.

---

## Features

### Document Management

- Document Upload
- Duplicate Detection using SHA-256
- Document Versioning
- Document Metadata Management
- Delete Documents

### Intelligent Processing

- Recursive Text Chunking
- Embedding Generation
- FAISS Vector Search
- Retrieval-Augmented Generation (RAG)

### Background Processing

- Asynchronous Job Queue
- Background Worker
- Job Status Tracking

### Monitoring & Analytics

- Upload Metrics
- Search Metrics
- Search Response Time
- Dashboard Analytics
- System Health Monitoring

### Enterprise Features

- Audit Logging
- Version History
- Access Levels
- Permission Engine (Foundation)
- Modular Architecture

---

## Technology Stack

### Backend

- Python
- FastAPI
- Uvicorn

### AI

- OpenAI
- LangChain
- SentenceTransformers

### Vector Database

- FAISS

### Database

- SQLite

### Development

- Git
- GitHub

---

## REST APIs

| Method | Endpoint                 | Description         |
| ------ | ------------------------ | ------------------- |
| POST   | /upload                  | Upload a document   |
| POST   | /search                  | Semantic Search     |
| GET    | /dashboard               | Analytics Dashboard |
| GET    | /documents               | List Documents      |
| GET    | /documents/{id}          | Document Details    |
| GET    | /documents/{id}/versions | Document Versions   |
| DELETE | /documents/{id}          | Delete Document     |

---

## Project Structure

```
src/
├── analytics/
├── api/
├── background/
├── configs/
├── constants/
├── database/
├── embeddings/
├── ingestion/
├── llm/
├── models/
├── monitoring/
├── orchestrator/
├── permissions/
├── preprocessing/
├── services/
├── sync/
├── vectorstore/
└── versioning/
```

---

## Current Features

- Document Upload
- Background Processing
- Semantic Search
- Retrieval-Augmented Generation
- Document Versioning
- Audit Logs
- Monitoring
- Analytics Dashboard
- Enterprise Architecture

---

## Future Enhancements

- Hybrid Search
- Query Expansion
- Cross Encoder Re-ranking
- Role Based Access Control
- Docker Deployment
- Kubernetes Deployment
- Multi-LLM Support
- Redis Cache
- CI/CD Pipeline

---

## Documentation

Detailed documentation is available under the **docs/** directory.

- Architecture
- Database Schema
- API Specification
- Monitoring
- Deployment Guide
- Product Roadmap

---
