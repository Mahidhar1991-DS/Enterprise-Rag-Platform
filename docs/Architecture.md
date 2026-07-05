# Enterprise RAG Platform Architecture

## High Level Architecture

```
                        Client
                           │
                           ▼
                    FastAPI REST APIs
                           │
     ┌─────────────────────┼─────────────────────┐
     ▼                     ▼                     ▼
 Upload Routes        Search Routes      Analytics Routes
     │                     │                     │
     ▼                     ▼                     ▼
 Job Manager         Search Service      Analytics Manager
     │                     │                     │
     ▼                     ▼                     ▼
Background Worker   Retrieval Pipeline   Analytics Repository
                           │
                           ▼
                     Permission Engine
                           │
                           ▼
                         RAG Chain
                           │
                           ▼
                    OpenAI Language Model
                           │
                           ▼
                    Generated Response
```

---

# Layered Architecture

## API Layer

Responsibilities

- Accept HTTP requests
- Validate request payload
- Delegate processing
- Return HTTP responses

Components

- Upload Routes
- Search Routes
- Document Routes
- Analytics Routes

---

## Service Layer

Responsibilities

- Business Workflow
- Monitoring
- Performance Tracking
- Search Orchestration

Components

- SearchService

---

## Pipeline Layer

Responsibilities

- Document Ingestion
- Retrieval
- Chunking
- Embedding Generation
- RAG Workflow

Components

- IngestionPipeline
- RetrievalPipeline

---

## Business Layer

Responsibilities

- Analytics
- Version Management
- Background Jobs
- Monitoring

Components

- AnalyticsManager
- VersionManager
- JobManager
- MonitoringManager

---

## Repository Layer

Responsibilities

- Database Access
- CRUD Operations
- SQL Queries

Repositories

- DocumentRepository
- VersionRepository
- ChunkRepository
- JobRepository
- AuditRepository
- AnalyticsRepository

---

## Infrastructure Layer

Components

Database

- SQLite

Vector Store

- FAISS

Embeddings

- SentenceTransformers

LLM

- OpenAI

---

# Document Upload Flow

```
Client

↓

Upload API

↓

Job Manager

↓

Background Worker

↓

Ingestion Pipeline

↓

Version Manager

↓

Chunking

↓

Embeddings

↓

FAISS

↓

Database
```

---

# Search Flow

```
Client

↓

Search API

↓

Search Service

↓

Monitoring

↓

Retrieval Pipeline

↓

Permission Engine

↓

FAISS Search

↓

RAG Chain

↓

OpenAI

↓

Answer
```

---

# Analytics Flow

```
Client

↓

Dashboard API

↓

Analytics Manager

↓

Analytics Repository

↓

Metrics Database

↓

Dashboard Response
```

---

# Database Tables

- documents
- document_versions
- document_chunks
- jobs
- metrics
- audit_logs

---

# Design Patterns

Repository Pattern

Separates database access from business logic.

Service Layer

Encapsulates workflow and orchestration.

Pipeline Pattern

Processes documents in sequential stages.

Manager Pattern

Implements business rules and calculations.

Dependency Injection

Services instantiate reusable components.

---

# Monitoring

Metrics Captured

- Upload Count
- Search Count
- Search Time
- Job Status
- Dashboard Analytics

---

# Analytics Dashboard

Provides

- Total Documents
- Total Chunks
- Total Jobs
- Failed Jobs
- Pending Jobs
- Upload Count
- Search Count
- Average Search Time
- Success Rate
- System Health
- Queue Status

---

# Future Architecture

- Hybrid Search
- Query Expansion
- Cross Encoder Re-ranking
- RBAC
- Redis Cache
- Kubernetes
- Multi-LLM Support
- CI/CD
- Agentic RAG
