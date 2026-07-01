-- =====================================
-- DOCUMENTS
-- =====================================

CREATE TABLE IF NOT EXISTS documents (
    document_id TEXT PRIMARY KEY,
    document_name TEXT NOT NULL,
    category TEXT NOT NULL,
    source_type TEXT,
    access_level TEXT DEFAULT 'PUBLIC',
    source_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'ACTIVE'
);

-- =====================================
-- DOCUMENT VERSIONS
-- =====================================

CREATE TABLE IF NOT EXISTS document_versions (
    version_id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    version_number INTEGER NOT NULL,
    file_hash TEXT NOT NULL,
    file_size INTEGER,
    active INTEGER DEFAULT 1,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(document_id)
        REFERENCES documents(document_id)
        ON DELETE CASCADE
);

-- =====================================
-- DOCUMENT CHUNKS
-- =====================================

CREATE TABLE IF NOT EXISTS document_chunks (
    chunk_id TEXT PRIMARY KEY,
    version_id TEXT NOT NULL,

    chunk_index INTEGER NOT NULL,

    chunk_text TEXT NOT NULL,

    vector_id TEXT,

    embedding_status TEXT DEFAULT 'PENDING',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(version_id)
        REFERENCES document_versions(version_id)
        ON DELETE CASCADE
);

-- =====================================
-- AUDIT LOGS
-- =====================================

CREATE TABLE IF NOT EXISTS audit_logs (
    audit_id TEXT PRIMARY KEY,

    document_id TEXT,

    event_type TEXT NOT NULL,

    old_version INTEGER,

    new_version INTEGER,

    description TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(document_id)
        REFERENCES documents(document_id)
);


CREATE TABLE IF NOT EXISTS query_logs (
    query_id TEXT PRIMARY KEY,

    user_query TEXT NOT NULL,

    retrieved_chunks INTEGER,

    response_time_ms INTEGER,

    token_usage INTEGER,

    llm_cost REAL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_documents_category
ON documents(category);

CREATE INDEX IF NOT EXISTS idx_document_versions_document
ON document_versions(document_id);

CREATE INDEX IF NOT EXISTS idx_document_versions_active
ON document_versions(active);

CREATE INDEX IF NOT EXISTS idx_document_chunks_version
ON document_chunks(version_id);

CREATE INDEX IF NOT EXISTS idx_audit_logs_document
ON audit_logs(document_id);


-- =====================================
-- Creating Jobs Table
-- =====================================

CREATE TABLE jobs (

    job_id TEXT PRIMARY KEY,

    file_path TEXT NOT NULL,

    category TEXT NOT NULL,

    access_level TEXT NOT NULL,

    status TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    completed_at TIMESTAMP
);

- =====================================
-- Creating Metrics Table
-- =====================================


CREATE TABLE metrics (

    metric_id TEXT PRIMARY KEY,

    metric_name TEXT NOT NULL,

    metric_value REAL NOT NULL,

    metric_type TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);