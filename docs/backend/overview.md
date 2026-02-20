# Backend Overview

_Last reviewed: 2026-02-20_

## Purpose

The Tracepipe backend provides APIs for Session ingestion, Suite/Action/Tool management, and Example retrieval. It serves both the storefront frontend and external API consumers.

## Architecture

```mermaid
graph LR
    Frontend[Storefront] --> API[Backend API]
    External[External Clients] --> API
    API --> Auth[Auth Middleware]
    Auth --> Sessions[Session Service]
    Auth --> Catalog[Catalog Service]
    Auth --> Examples[Example Service]
    
    Sessions --> Storage[(Object Storage)]
    Examples --> Storage
    Catalog --> DB[(Database)]
```

## Authentication

API requests require an API key in the `X-API-Key` header. Keys are generated through the [storefront](https://tracepipe.example.com) after registration and adding a payment method.

**API Key Header Format**:
```
X-API-Key: tp_live_abcdef123456789...
```

**Example Request**:
```bash
curl -X GET https://api.tracepipe.example.com/v1/sessions \
  -H "X-API-Key: tp_live_abcdef123456789..."
```

API keys are scoped to your user account and can be revoked at any time through the storefront dashboard.

## Services

### Session Service

Handles trace ingestion from users:

- **POST** `/sessions` — Upload input event trace
  ```bash
  curl -X POST https://api.tracepipe.example.com/v1/sessions \
    -H "X-API-Key: tp_live_..." \
    -F "input_events=@input_events.jsonl" \
    -F "suite_id=<suite-uuid>"
  ```

- **GET** `/sessions/{id}` — Retrieve session metadata
  ```bash
  curl -X GET https://api.tracepipe.example.com/v1/sessions/{id} \
    -H "X-API-Key: tp_live_..."
  ```

- **GET** `/sessions` — List sessions for authenticated user
  ```bash
  curl -X GET https://api.tracepipe.example.com/v1/sessions?suite_id=<uuid> \
    -H "X-API-Key: tp_live_..."
  ```

Sessions are stored in object storage at paths defined by the data model.

### Catalog Service

Manages the Suite, Action, MCP Server, and Tool entities:

- **CRUD** `/suites` — Suite management
- **CRUD** `/suites/{id}/actions` — Action definitions
- **CRUD** `/mcp-servers` — MCP server catalog
- **CRUD** `/mcp-servers/{id}/tools` — Tool definitions

### Example Service

Provides access to processed training data:

- **POST** `/examples` — Trigger pipeline processing for a session
  ```bash
  curl -X POST https://api.tracepipe.example.com/v1/examples \
    -H "X-API-Key: tp_live_..." \
    -H "Content-Type: application/json" \
    -d '{"session_id": "<uuid>", "model_id": "<uuid>", "model_configuration": {"temperature": 0.7}}'
  ```

- **GET** `/examples` — List examples, filterable by session, model, suite
  ```bash
  curl -X GET "https://api.tracepipe.example.com/v1/examples?session_id=<uuid>&suite_id=<uuid>" \
    -H "X-API-Key: tp_live_..."
  ```

- **GET** `/examples/{id}` — Retrieve example metadata
  ```bash
  curl -X GET https://api.tracepipe.example.com/v1/examples/{id} \
    -H "X-API-Key: tp_live_..."
  ```

- **GET** `/examples/{id}/messages` — Stream JSONL training messages
  ```bash
  curl -X GET https://api.tracepipe.example.com/v1/examples/{id}/messages \
    -H "X-API-Key: tp_live_..." \
    -o training_data.jsonl
  ```

### User Service

Manages user accounts and API keys:

- **GET** `/users/me` — Current user profile
- **POST** `/api-keys` — Generate new API key
- **DELETE** `/api-keys/{id}` — Revoke API key
- **GET** `/api-keys` — List active keys

## Authentication

- API keys for external access
- Session tokens for storefront access
- Scoped permissions by Suite

## Related Documents

- [Data Model](../data_model.md) — Entity schemas
- [Frontend Overview](../frontend/overview.md) — Storefront that consumes this API
- [Pipelines Overview](../pipelines/overview.md) — Session-to-Example processing
- [Backend MVP](../milestones/mvp/backend.md) — Current milestone
