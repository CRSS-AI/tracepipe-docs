# Tracepipe MVP GitHub Issues

**Status**: Draft — not yet filed in GitHub  
**Generated**: 2026-02-11

---

## Overview

This document contains issues for the three Tracepipe MVP milestones. Issues are filed in their **native repositories** and tracked via a centralized GitHub Project.

**Milestone Assignments**:
- **Backend MVP**: Issues filed in `CRSS-AI/tracepipe-backend`
- **Pipelines MVP**: Issues filed in `CRSS-AI/tracepipe-pipelines`
- **Frontend MVP**: Issues filed in `CRSS-AI/tracepipe-frontend`

**Issue Codes**: BE-XX, PL-XX, FE-XX are reference codes within this document. GitHub will auto-assign actual issue numbers.

---

## Filing Instructions

### Issue Naming Convention

**Format**: `Brief Title` (no component prefix — repo is implicit)

**Examples**:
- `Create Tracepipe Database Schema` (Issue BE-01 → filed in tracepipe-backend)
- `Port Bronze Trace Loader` (Issue PL-01 → filed in tracepipe-pipelines)
- `Next.js Project Scaffolding` (Issue FE-01 → filed in tracepipe-frontend)

### Issue Body Template

Each issue should use this markdown template:

```markdown
## Description

[Copy the "Description" section from this document]

## Status Annotation

**Carry-Over / Adaptation / New**: [One of these three]

[If Carry-Over or Adaptation, include:]
**Predecessor Work**: [Reference to autoactivity repo, e.g., "autoactivity-be #31 (closed)"]

## Changes Required

[Copy the "Changes Required" or relevant subsections from this document]

## Acceptance Criteria

[Copy the checklist from this document — these should remain as checkboxes]

## Priority

**P0** / **P1** / **P2**

## Related Issues

[Add links to dependent issues after filing, e.g., "Depends on #XX", "Blocks #YY"]

## Related Documentation

- [Data Model](https://github.com/CRSS-AI/tracepipe-docs/blob/main/docs/data_model.md)
- [Backend Overview](https://github.com/CRSS-AI/tracepipe-docs/blob/main/docs/backend/overview.md)
- [Milestone: Backend MVP](https://github.com/CRSS-AI/tracepipe-docs/blob/main/docs/milestones/mvp/backend.md)

[Adjust links based on issue's milestone]
```

### Label Strategy

**Status Labels** (indicate work type):
- `status: carry-over` — Work can be ported directly from autoactivity repos
- `status: adaptation` — Existing work that needs refactoring for Tracepipe
- `status: new` — Net-new implementation required

**Priority Labels** (indicate critical path):
- `priority: P0` — Critical path, must be done first
- `priority: P1` — High priority, needed for MVP
- `priority: P2` — Medium priority, nice-to-have for MVP

**Component Labels** (indicate which repo does the work):
- `component: backend` — Work happens in tracepipe-backend
- `component: pipelines` — Work happens in tracepipe-pipelines
- `component: frontend` — Work happens in tracepipe-frontend
- `component: infrastructure` — Cross-cutting work

**Type Labels** (indicate nature of work):
- `type: feature` — New feature implementation
- `type: refactor` — Code refactoring/cleanup
- `type: documentation` — Documentation updates
- `type: testing` — Test coverage
- `type: ci-cd` — CI/CD automation

### Milestone Assignment

| Issue Code | Milestone | Repository |
|------------|-----------|------------|
| BE-01 through BE-24 | Backend MVP | CRSS-AI/tracepipe-backend |
| PL-01 through PL-16 | Pipelines MVP | CRSS-AI/tracepipe-pipelines |
| FE-01 through FE-10 | Frontend MVP | CRSS-AI/tracepipe-frontend |
| CC-01 through CC-06 | (varies) | Component-specific |

### Label Mapping from Document

For each issue, apply labels based on these fields:

**Status Annotation** → Status Label:
- `[CARRY-OVER]` → `status: carry-over`
- `[ADAPTATION]` → `status: adaptation`
- `[NEW]` → `status: new`

**Priority** → Priority Label:
- `P0` → `priority: P0`
- `P1` → `priority: P1`
- `P2` → `priority: P2`

**Issue Prefix** → Component Label:
- `BE-XX` → `component: backend`
- `PL-XX` → `component: pipelines`
- `FE-XX` → `component: frontend`
- `CC-XX` → `component: infrastructure` (or specific component if applicable)

**Type Label** (infer from issue content):
- Database/schema issues → `type: refactor`
- New endpoints/services → `type: feature`
- Test issues → `type: testing`
- CI/CD issues → `type: ci-cd`
- Documentation issues → `type: documentation`

### Filing Order

**Recommended order** (to minimize dependency issues):

1. **Backend Infrastructure** (BE-01 through BE-04) — Foundation for all backend work
2. **Backend Services** (BE-05 through BE-23) — API endpoints needed by pipelines and frontend
3. **Pipelines Foundation** (PL-01 through PL-04) — Port existing work first
4. **Pipelines New Work** (PL-05 through PL-19) — Build on foundation
5. **Frontend** (FE-01 through FE-11) — Depends on backend APIs
6. **Cross-Cutting** (CC-01 through CC-06) — Can be done in parallel

### Automation with GitHub CLI

```bash
# Create an issue with labels and milestone
gh issue create \
  --repo CRSS-AI/tracepipe-backend \
  --title "Create Tracepipe Database Schema" \
  --body-file issue-be-01.md \
  --milestone "Backend MVP" \
  --label "status: new,priority: P0,type: feature"
```

### Cross-Repository Tracking

Issues are tracked in a centralized GitHub Project that aggregates from all repos. When referencing issues across repos, use the format: `CRSS-AI/tracepipe-backend#XX`.

### Label Creation Script

If labels don't exist yet, create them with:

```bash
gh label create "status: carry-over" --color "0E8A16" --repo CRSS-AI/tracepipe
gh label create "status: adaptation" --color "FBCA04" --repo CRSS-AI/tracepipe
gh label create "status: new" --color "D93F0B" --repo CRSS-AI/tracepipe
gh label create "priority: P0" --color "B60205" --repo CRSS-AI/tracepipe
gh label create "priority: P1" --color "D93F0B" --repo CRSS-AI/tracepipe
gh label create "priority: P2" --color "FBCA04" --repo CRSS-AI/tracepipe
gh label create "component: backend" --color "0052CC" --repo CRSS-AI/tracepipe
gh label create "component: pipelines" --color "5319E7" --repo CRSS-AI/tracepipe
gh label create "component: frontend" --color "1D76DB" --repo CRSS-AI/tracepipe
gh label create "component: infrastructure" --color "BFD4F2" --repo CRSS-AI/tracepipe
gh label create "type: feature" --color "A2EEEF" --repo CRSS-AI/tracepipe
gh label create "type: refactor" --color "EDEDED" --repo CRSS-AI/tracepipe
gh label create "type: documentation" --color "0075CA" --repo CRSS-AI/tracepipe
gh label create "type: testing" --color "D4C5F9" --repo CRSS-AI/tracepipe
gh label create "type: ci-cd" --color "C5DEF5" --repo CRSS-AI/tracepipe
```

### Maintenance

As work progresses:
- Update issue bodies with findings/decisions
- Close issues as work completes
- Create follow-up issues for scope creep ("nice-to-have" items)
- Update milestone due dates based on velocity
- Sync milestone status to documentation (update checkbox deliverables in `tracepipe-docs/docs/milestones/mvp/*.md`)

---

## Overview

This document outlines proposed GitHub Issues for the three Tracepipe MVP milestones:

1. **Pipelines MVP** (Milestone #1) — 19 issues
2. **Backend MVP** (Milestone #2) — 23 issues  
3. **Frontend MVP** (Milestone #3) — 11 issues

**Total**: 53 fine-grained issues

Each issue includes:
- **Status annotation**: `[CARRY-OVER]`, `[ADAPTATION]`, or `[NEW]`
- **Priority**: `P0` (critical path), `P1` (high), `P2` (medium)
- **Description**: What needs to be done
- **Acceptance Criteria**: Measurable completion conditions
- **Predecessor Work**: References to autoactivity repos where applicable

---

## Milestone #2: Backend MVP

**Target Repo**: CRSS-AI/tracepipe-backend

### 1. Backend Infrastructure

#### Issue BE-01: Create Tracepipe Database Schema
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Create the Tracepipe database schema from scratch. This is a **new database** (not migrating from autoactivity). We are standing up a fresh `tracepipe` DB with the simplified data model: Capability Surface entities (Suite, Action, McpServer, Tool, ActionToolMap) plus execution entities (User, Session, Example, Model).

**Changes Required**:
- Create PostgreSQL database: `tracepipe`
- Create tables: `users`, `suites`, `actions`, `action_parameters`, `mcp_servers`, `tools`, `tool_parameters`, `action_tool_maps`, `action_tool_mappings`, `action_tool_parameter_mappings`, `models`, `sessions`, `examples`
- Create Alembic migrations for schema
- `sessions` table: `id` (UUID), `user_id` (FK), `suite_id` (FK), `description` (TEXT, nullable), `storage_path` (String), `created_at` (Timestamp)
- `examples` table: `id` (UUID), `session_id` (FK), `model_id` (FK), `action_tool_map_id` (FK), `model_configuration` (JSONB), `storage_path` (String), `status` (ENUM: pending, processing, completed, failed), `created_at` (Timestamp)

**Acceptance Criteria**:
- [ ] All tables created with correct schemas
- [ ] Foreign key constraints enforced
- [ ] Alembic migration script runs successfully
- [ ] Rollback migration works
- [ ] `Session.description` field exists (nullable TEXT)
- [ ] `Example.status` field exists (ENUM with 4 values)

**Reference**:
- See `tracepipe-docs/docs/data_model.md` for authoritative entity schemas

---

#### Issue BE-02: Port Core Application Scaffolding
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
The `tracepipe-backend` repo is currently **empty**. Port relevant application scaffolding from autoactivity-be to bootstrap the project: FastAPI app structure, domain/application/data layers, configuration management, and core utilities.

**Files to Port**:
- Port: FastAPI application setup (`main.py`, router registration)
- Port: Core configuration (`config.py`, environment variable management)
- Port: Database session management (`database.py`)
- Port: Domain service patterns
- Port: Repository patterns
- Port: API v1 structure (`api/v1/`)
- Skip: Any Task/Activity/Case/Instance code (doesn't exist in Tracepipe)

**Acceptance Criteria**:
- [ ] FastAPI application starts successfully
- [ ] Database connection works
- [ ] Environment configuration loads
- [ ] API versioning structure (`/v1/`) in place
- [ ] Health check endpoint responds
- [ ] Test suite structure exists

**Autoactivity Reference**: autoactivity-be provides the application architecture pattern

---

#### Issue BE-03: Azure Entra External ID Authentication Integration
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Integrate Azure Entra External ID (formerly Azure AD B2C) for authentication across the platform. This is the identity provider for **both** the frontend (user login/registration) and the backend (token validation). Backend must validate Entra ID tokens on protected endpoints.

**Requirements**:
- Configure Azure Entra External ID tenant
- Backend: Implement JWT token validation middleware
- Backend: Extract user identity from validated tokens
- Backend: Support both Entra ID tokens (for frontend) and API keys (for programmatic access)
- Protected endpoints require valid auth (token or API key)

**Implementation**:
- Use `azure-identity` or `msal` libraries for token validation
- Middleware validates `Authorization: Bearer <token>` headers
- Falls back to API key validation if no Bearer token present
- User context available to all protected endpoint handlers

**Acceptance Criteria**:
- [ ] Azure Entra External ID tenant configured
- [ ] Backend validates Entra ID JWT tokens
- [ ] Invalid/expired tokens return 401
- [ ] User identity extracted from valid tokens
- [ ] API key fallback works for programmatic access
- [ ] All protected endpoints use auth middleware

**Note**: This is cross-cutting — frontend issue FE-02 covers the client-side integration.

---

#### Issue BE-04: Docker & Docker Compose Configuration
**Status**: `[CARRY-OVER]` | **Priority**: `P1`

**Description**:
Port the Docker and Docker Compose setup from autoactivity-be. Update service names and environment variables for Tracepipe.

**Carry-Over Work**:
- `autoactivity-be/Dockerfile` (multi-stage build)
- `autoactivity-be/docker-compose.yml` (app + PostgreSQL)

**Changes Required**:
- Update image name: `tracepipe-backend`
- Update service names
- Environment variables: `DATABASE_URL`, `STORAGE_CONNECTION_STRING`, `OPENROUTER_API_KEY`
- Volume mounts for development

**Acceptance Criteria**:
- [ ] `Dockerfile` builds successfully
- [ ] `docker-compose.yml` starts backend + database
- [ ] Healthcheck endpoint returns 200
- [ ] Database migrations run on startup
- [ ] Hot reload works in development mode

**Autoactivity Reference**: autoactivity-be has working Docker setup

---

### 2. Session Service

#### Issue BE-05: Session Model & Repository
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Adapt the Session model from autoactivity-be to match the simplified Tracepipe data model. Session no longer references Instance; instead, it directly references User and Suite.

**Changes Required**:
- SQLAlchemy model: `id` (UUID), `user_id` (FK to users), `suite_id` (FK to suites), `storage_path` (String), `created_at` (Timestamp)
- Remove `instance_id` foreign key
- Repository layer: `create()`, `get_by_id()`, `list_by_user()`, `list_by_suite()`
- Domain service: Basic CRUD operations

**Acceptance Criteria**:
- [ ] `Session` SQLAlchemy model matches data model spec
- [ ] `SessionRepository` implements CRUD operations
- [ ] Unit tests for repository layer
- [ ] Foreign key constraints enforced

**Autoactivity Reference**: 
- autoactivity-be #59 (closed: "Update session data model")
- `autoactivity-be/src/autoactivity/data/models/session.py`

---

#### Issue BE-06: Session Upload Endpoint (POST /v1/sessions)
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Implement the Session upload endpoint. Accept **input trace files only** (not screenshots or network traffic). Store at the new storage path convention.

**Changes Required**:
- Endpoint: `POST /v1/sessions`
- Request: Multipart form with trace file(s) + `suite_id` field + optional `description` field
- Accepted files: Input trace data (e.g., `input_events.jsonl`)
- Storage path: `sessions/<session-id>/` 
- Upload to object storage (Azure Blob Storage)
- Create Session record in database

**Acceptance Criteria**:
- [ ] Endpoint accepts multipart/form-data
- [ ] Validates required trace file(s)
- [ ] Stores files at `sessions/<uuid>/` in object storage
- [ ] Creates Session record with `storage_path`, `suite_id`, and optional `description`
- [ ] Returns Session metadata (id, storage_path, created_at)
- [ ] Returns 400 for invalid suite_id
- [ ] Returns 401 for unauthenticated requests

**Note**: We are **only accepting input traces** — no screenshots, no network traffic.

---

#### Issue BE-07: Session Retrieval Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P1`

**Description**:
Implement Session retrieval endpoints for listing and getting individual sessions.

**Endpoints**:
- `GET /v1/sessions` — List sessions (filterable by `suite_id`)
- `GET /v1/sessions/{id}` — Get session metadata

**Changes Required**:
- Controller methods with query parameter support
- Pagination (limit/offset or cursor-based)
- Filter by suite_id
- Authorization: User can only see their own sessions

**Acceptance Criteria**:
- [ ] `GET /v1/sessions` returns array of session metadata
- [ ] Query param `?suite_id=<uuid>` filters results
- [ ] Pagination works (test with 100+ sessions)
- [ ] `GET /v1/sessions/{id}` returns single session
- [ ] Returns 404 for non-existent sessions
- [ ] Returns 403 if user doesn't own session

---

### 3. Capability Service

#### Issue BE-08: Suite Read-Only Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Implement read-only endpoints for Suites. **Suites are platform-controlled** — users do not create, update, or delete them. Users query the catalog of available Suites.

**Endpoints**:
- `GET /v1/suites` — List all suites
- `GET /v1/suites/{id}` — Get suite details

**Changes Required**:
- Repository: `get_by_id()`, `list_all()`
- Domain service: Read-only operations
- Controller: GET endpoints only

**Acceptance Criteria**:
- [ ] List endpoint returns all suites
- [ ] Get endpoint returns single suite with actions
- [ ] Returns 404 for non-existent suites
- [ ] No create/update/delete endpoints exist

**Autoactivity Reference**: 
- autoactivity-be/src/autoactivity/domain/suite/ (has partial implementation)

---

#### Issue BE-09: Action Read-Only Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Implement read-only endpoints for Actions. **Actions are platform-controlled** — users do not create or modify them. Users query the action catalog for a given Suite.

**Endpoints**:
- `GET /v1/suites/{suite_id}/actions` — List actions for a suite
- `GET /v1/actions/{id}` — Get action details with parameters

**Changes Required**:
- Repository: `get_by_id()`, `list_by_suite()`
- Domain service: Read-only operations
- Controller: GET endpoints only, nested under suites

**Acceptance Criteria**:
- [ ] List actions for a suite works
- [ ] Get action returns action with parameters
- [ ] Returns 404 for non-existent suite/action
- [ ] No create/update/delete endpoints exist

**Autoactivity Reference**: 
- autoactivity-be #109 (closed: "Implement action inventory endpoint")
- autoactivity-be/src/autoactivity/domain/action/

---

#### Issue BE-10: McpServer Read-Only Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P1`

**Description**:
Implement read-only endpoints for McpServer entities. **McpServers are platform-controlled** — users do not create or modify them. This may change in the future with "Bring Your Own MCP Server" (BYOMCP), but security implications need study first.

**Endpoints**:
- `GET /v1/mcp-servers` — List all MCP servers
- `GET /v1/mcp-servers/{id}` — Get MCP server with tools

**Acceptance Criteria**:
- [ ] List all MCP servers works
- [ ] Get MCP server returns server with nested tools
- [ ] Returns 404 for non-existent servers
- [ ] No create/update/delete endpoints exist

**Note**: Future BYOMCP support would require additional security review before enabling user-managed MCP servers.

---

#### Issue BE-11: Tool Read-Only Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P1`

**Description**:
Tools are always served with their MCP server. Implement read-only endpoint to list tools for a given MCP server. **Tools are platform-controlled** — users do not create loose tools.

**Endpoints**:
- `GET /v1/mcp-servers/{id}/tools` — List tools for an MCP server

**Acceptance Criteria**:
- [ ] List tools for MCP server works
- [ ] Returns tools with parameters
- [ ] Returns 404 for non-existent MCP server
- [ ] No individual tool query or create/update/delete endpoints exist

---

#### Issue BE-12: ActionToolMap Read-Only Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Implement read-only endpoints for ActionToolMaps. **ActionToolMaps are platform-controlled** — users cannot modify suite-to-MCP-server bindings. Users query available mappings.

**Endpoints**:
- `GET /v1/action-tool-maps` — List all maps
- `GET /v1/action-tool-maps/{id}` — Get map with nested mappings

**Acceptance Criteria**:
- [ ] List endpoint returns all maps
- [ ] Get endpoint returns map with full mapping tree (toolMappings, parameterMappings)
- [ ] Returns 404 for non-existent maps
- [ ] No create/update/delete endpoints exist

**Autoactivity Reference**: 
- autoactivity-be #215 (open: "Update action_tool_maps endpoint to retrieve mcp server's information")
- autoactivity-be/src/autoactivity/domain/action_tool_map/

---

### 4. Example Service

#### Issue BE-13: Example Model & Repository
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the Example entity — the output of pipeline processing. Links a Session to its generated training data.

**Schema**:
- `id` (UUID, PK)
- `session_id` (UUID, FK to sessions)
- `model_id` (UUID, FK to models)
- `action_tool_map_id` (UUID, FK to action_tool_maps)
- `model_configuration` (JSONB — provider-specific params like temperature)
- `storage_path` (String — path to JSONL file in object storage)
- `created_at` (Timestamp)

**Acceptance Criteria**:
- [ ] SQLAlchemy model created
- [ ] Repository with CRUD operations
- [ ] Unit tests for repository
- [ ] Foreign key constraints enforced

---

#### Issue BE-14: Example Listing Endpoint (GET /v1/examples)
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement endpoint to list Examples with filtering.

**Query Parameters**:
- `session_id` (UUID) — Filter by session
- `suite_id` (UUID) — Filter by suite (via session)
- `model_id` (UUID) — Filter by model
- `limit` / `offset` — Pagination

**Acceptance Criteria**:
- [ ] Returns array of Example metadata (no JSONL content)
- [ ] All filters work
- [ ] Pagination works
- [ ] User can only see their own examples (via session ownership)

---

#### Issue BE-15: Example Retrieval & Messages Endpoints
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement endpoints to retrieve Example metadata and stream JSONL training messages.

**Endpoints**:
- `GET /v1/examples/{id}` — Get metadata
- `GET /v1/examples/{id}/messages` — Stream JSONL file from object storage

**Acceptance Criteria**:
- [ ] Metadata endpoint returns Example record
- [ ] Messages endpoint streams file from `storage_path`
- [ ] Returns 404 for non-existent examples
- [ ] Returns 403 if user doesn't own example
- [ ] Messages endpoint sets correct Content-Type header (`application/x-ndjson`)

---

### 5. User Service

#### Issue BE-16: User Profile Endpoint (GET /v1/users/me)
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Implement endpoint for authenticated user to retrieve their profile.

**Response**:
```json
{
  "id": "uuid",
  "displayName": "string",
  "email": "string",
  "createdAt": "timestamp"
}
```

**Acceptance Criteria**:
- [ ] Returns authenticated user's profile
- [ ] Requires valid API key
- [ ] Returns 401 for unauthenticated requests

---

#### Issue BE-17: API Key Management Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P1`

**Description**:
Implement user-facing API key CRUD endpoints. AutoActivity has key validation but not user-facing management.

**Endpoints**:
- `POST /v1/api-keys` — Generate new key (returns key once)
- `GET /v1/api-keys` — List user's keys (masked)
- `DELETE /v1/api-keys/{id}` — Revoke key

**Acceptance Criteria**:
- [ ] Generate creates key with secure random value
- [ ] Returns full key only on creation
- [ ] List shows masked keys (`tp_live_****...****`)
- [ ] Delete marks key as revoked (soft delete)
- [ ] Revoked keys fail authentication

**Autoactivity Reference**: autoactivity-be #31 has backend validation only

---

### 6. Payment Models & Example Creation

#### Issue BE-18: Example Creation & Processing Endpoint with Payment Models
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement Example creation endpoint that triggers pipeline processing. Support multiple payment models:

1. **Human users with API key**: Card on file, usage billed monthly (tokens, storage×time)
2. **MCP with API key**: Same as human users — charges to card behind the API key
3. **Apple Pay 2 (AP2) agents** (P2 priority): Stateless payment model for agents that can't store cards

**Apple Pay 2 (AP2) Model**:
AP2 mandates that payment methods cannot be stored and charged on-demand. For AP2 agents, implement a deposit-based flow:
- Agent sends: trace file + configuration + AP2 payment token
- Backend charges 1.5x estimated compute cost as deposit
- Backend creates Example record with `status: pending`, returns example ID
- Pipeline processes asynchronously
- Agent polls for completion (Example held for 24 hours)
- Excess deposit refunded when agent retrieves the completed Example

**Endpoints**:
- `POST /v1/examples` — Create Example (for API key users: card on file)
- `POST /v1/ap2/examples` — Create Example (for AP2 agents: deposit model) [P2]

**Request** (`POST /v1/examples`):
```json
{
  "session_id": "uuid",
  "model_id": "uuid",
  "action_tool_map_id": "uuid",
  "model_configuration": {"temperature": 0.7, ...}
}
```

**Example Status Field**:
Examples have a `status` ENUM field:
- `pending`: Created, awaiting processing
- `processing`: Pipeline is running
- `completed`: JSONL ready for download
- `failed`: Processing error

**Acceptance Criteria**:
- [ ] `POST /v1/examples` creates Example with `status: pending`
- [ ] Triggers AzureML pipeline via endpoint
- [ ] Returns Example ID immediately (async processing)
- [ ] Supports optional callback URL for status updates
- [ ] AP2 endpoint (P2) accepts payment token and charges deposit
- [ ] AP2 flow refunds excess when agent retrieves completed Example
- [ ] All payment models track usage for billing

**Note**: This replaces the wrongly-scoped PL-11/PL-12 issues. Processing orchestration is triggered by the backend, not by the pipelines themselves.

---

#### Issue BE-19: MCP Server Interface
**Status**: `[NEW]` | **Priority**: `P2`

**Description**:
Add MCP (Model Context Protocol) server interface to expose Tracepipe operations as tools for LLM agents. Follow the pattern: MCPService as a sub-service with read-only endpoints for listing MCP servers and their tools.

**Pattern** (from reference project):
- Create `MCPService` class that wraps `MCPServerRepository`
- Expose as sub-service via composition in main service layer
- Provide async `list_mcp_servers()` and `get_mcp_server(id)` operations
- API endpoints: `GET /v1/mcp` and `GET /v1/mcp/{id}`

**Tools to Expose** (via MCP):
- `get_examples` — Retrieve training examples
- `get_session` — Retrieve session trace data
- `list_suites` — List available suites

**Acceptance Criteria**:
- [ ] MCPService class exists as sub-service
- [ ] `GET /v1/mcp` lists MCP servers
- [ ] `GET /v1/mcp/{id}` returns server with tools
- [ ] MCP-compatible tool definitions returned
- [ ] Integrates with existing repository layer

**Reference**: See agent-registry MCP service pattern for implementation approach.

---

### 7. API Documentation

#### Issue BE-20: OpenAPI Specification
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Generate and publish OpenAPI 3.0 specification for the Tracepipe API.

**Deliverables**:
- `openapi.json` file generated from FastAPI
- Served at `/v1/openapi.json`
- Swagger UI at `/v1/docs`
- ReDoc at `/v1/redoc`

**Acceptance Criteria**:
- [ ] All endpoints documented with descriptions
- [ ] Request/response schemas included
- [ ] Authentication documented (X-API-Key header)
- [ ] Examples provided for common operations
- [ ] Accessible without authentication

---

### 7. Database & Migrations

#### Issue BE-21: Model Entity Implementation
**Status**: `[CARRY-OVER]` | **Priority**: `P0`

**Description**:
Port the Model entity from autoactivity-be. Represents LLM/policy artifacts. **P0 because Examples depend on Models.**

**Schema**:
- `id` (UUID, PK)
- `provider` (Enum: OpenAI, Anthropic, etc.)
- `name` (String: e.g., "gpt-4", "claude-3-opus")

**Carry-Over Work**:
- Model entity exists in autoactivity-be with Provider enum
- Already tested and used

**Acceptance Criteria**:
- [ ] SQLAlchemy model created
- [ ] Provider enum defined
- [ ] Seeder script creates common models

**Autoactivity Reference**: autoactivity-be/src/autoactivity/data/models/model.py

---

#### Issue BE-22: Database Seeding Script
**Status**: `[ADAPTATION]` | **Priority**: `P2`

**Description**:
Create database seeding script for development/testing. Follow the SQL-based, idempotent pattern from the reference project.

**Approach**:
- SQL file: `scripts/seed.sql`
- Idempotent: Use `ON CONFLICT DO NOTHING` for all inserts
- Fixed UUIDs for test data (easy referencing in tests)
- Hierarchical seed: Models → Suites → Actions → McpServers → Tools → ActionToolMaps → Test User with API key

**Seed Data**:
- 2-3 Models (GPT-4, Claude-3)
- 2-3 Suites (Gmail, Google Calendar, GitHub)
- Actions for each Suite
- 2-3 McpServers with Tools
- ActionToolMaps binding Suites to McpServers
- Test User with known API key

**Acceptance Criteria**:
- [ ] `seed.sql` file exists
- [ ] All inserts are idempotent (`ON CONFLICT DO NOTHING`)
- [ ] Fixed UUIDs used for entities
- [ ] Runnable via: `psql -d tracepipe -f scripts/seed.sql`
- [ ] Creates complete capability surface

**Reference**: See agent-registry `scripts/seed.sql` for pattern.

---

#### Issue BE-23: OpenAPI Specification
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Generate and publish OpenAPI 3.0 specification for the Tracepipe API.

**Deliverables**:
- `openapi.json` file generated from FastAPI
- Served at `/v1/openapi.json`
- Swagger UI at `/v1/docs`
- ReDoc at `/v1/redoc`

**Acceptance Criteria**:
- [ ] All endpoints documented with descriptions
- [ ] Request/response schemas included
- [ ] Authentication documented (Bearer token + X-API-Key header)
- [ ] Examples provided for common operations
- [ ] Accessible without authentication

---

#### Issue BE-24: Integration Tests for End-to-End Flows
**Status**: `[ADAPTATION]` | **Priority**: `P1`

**Description**:
Port and adapt integration tests from autoactivity-be. Test complete user journeys.

**Test Scenarios**:
1. User uploads session → retrieves session metadata
2. User requests Example processing → polls status → downloads JSONL
3. Query capability surface (suites, actions, tools)
4. Generate API key → use key to authenticate → revoke key

**Acceptance Criteria**:
- [ ] All scenarios have integration tests
- [ ] Tests use TestClient (FastAPI)
- [ ] Tests use test database (not prod)
- [ ] Tests clean up after themselves
- [ ] Run in CI/CD pipeline

**Autoactivity Reference**: autoactivity-be/tests/ (9 integration test files)

---

## Milestone #1: Pipelines MVP

**Target Repo**: CRSS-AI/tracepipe-pipelines

### 1. Pipeline Foundation

#### Issue PL-01: Port Bronze Trace Loader
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Adapt the Bronze layer trace extraction from autoactivity-data. Update to work with the new Session storage convention and **Session.description field** (optional user context on what traces represent).

**Carry-Over Work**:
- autoactivity-data bronze extraction is complete and tested
- Handles input events and session metadata

**Changes Required**:
- Update storage path logic: `sessions/<session-id>/`
- Update Backend API integration: Call `/v1/sessions/{id}` to fetch Session including `description` field
- Remove Instance/Case metadata fetch (use Suite metadata from Session)
- Update Parquet schema to remove instance-related columns
- Include `Session.description` in metadata if present

**Acceptance Criteria**:
- [ ] Loads traces from new storage paths
- [ ] Validates JSONL structure
- [ ] Fetches Session (including `description`) and Suite metadata from Backend API
- [ ] Outputs Bronze Parquet with correct schema
- [ ] Generates metrics JSON

**Note**: Session now has an optional `description` field (user-provided context), replacing the removed `task_instructions`.

**Autoactivity Reference**: 
- autoactivity-data #1, #12 (closed)
- autoactivity-data/action_extraction/action_extraction/extraction.py

---

#### Issue PL-02: Port Silver Trace Normalizer
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Adapt the Silver layer event integration from autoactivity-data. Merge keystroke patterns and consolidate typing runs.

**Carry-Over Work**:
- autoactivity-data silver integration is complete
- Sophisticated pattern merging logic (keydown→input→keyup, etc.)
- Run consolidation for typing

**Changes Required**:
- Remove Instance-related columns from output schema
- Update Session metadata integration
- Simplify schema (no Task/Activity references)

**Acceptance Criteria**:
- [ ] All pattern merging works (typing, navigation, modifiers)
- [ ] Run consolidation works (merges character arrays)
- [ ] Outputs Silver Parquet with simplified schema
- [ ] Generates metrics with merge ratios

**Autoactivity Reference**: 
- autoactivity-data #7, #13 (closed/open)
- autoactivity-data/action_extraction/action_extraction/integration/

---

#### Issue PL-03: Pipeline Configuration YAML
**Status**: `[CARRY-OVER]` | **Priority**: `P0`

**Description**:
Port the pipeline YAML configurations from autoactivity-data. Update component paths and variable names for Tracepipe.

**Carry-Over Work**:
- autoactivity-data has AzureML-compatible YAML configs
- Local bash runner parses these

**Changes Required**:
- Rename pipelines: `session_to_example_pipeline.yaml`
- Update component names: `trace_loader`, `trace_normalizer`, etc.
- Update variable names to match Tracepipe model

**Acceptance Criteria**:
- [ ] Pipeline YAML is valid AzureML schema
- [ ] Local bash runner can parse and execute
- [ ] All stages defined with correct inputs/outputs

**Autoactivity Reference**: autoactivity-data/action_extraction/config/

---

#### Issue PL-04: Local Pipeline Runner
**Status**: `[CARRY-OVER]` | **Priority**: `P0`

**Description**:
Port the local pipeline runner from autoactivity-data. The bash script parses YAML and orchestrates stage execution.

**Carry-Over Work**:
- `autoactivity-data/run_pipeline.sh` is complete
- Handles DAG resolution, variable substitution, sequential execution

**Changes Required**:
- Update script name: `run_pipeline.sh` → same
- Update default pipeline reference
- Test with new YAML configs

**Acceptance Criteria**:
- [ ] Script parses Tracepipe pipeline YAML
- [ ] Executes stages in correct order
- [ ] Passes outputs as inputs to next stage
- [ ] Handles failures gracefully
- [ ] Logs execution to console

**Autoactivity Reference**: 
- autoactivity-data #3 (closed)
- autoactivity-data/run_pipeline.sh

---

### 2. Action Classification (Gold Layer)

#### Issue PL-05: Implement Window Classification Stage
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the Window Classification stage (currently a stub in autoactivity-data). Classify trace events by UI window/element context.

**Current State**: Stub passthrough in autoactivity-data

**Implementation**:
- Parse Chrome trace events for window context (URLs, titles)
- Group events by active window
- Attach window metadata to each event
- Use LLM (optional) for ambiguous contexts

**Acceptance Criteria**:
- [ ] Identifies window boundaries in trace
- [ ] Attaches window context to events
- [ ] Handles multi-window scenarios
- [ ] Outputs Gold Parquet with window columns

**Autoactivity Reference**: 
- autoactivity-data #11 (open: "Build classification pipeline window classification step")
- autoactivity-data/action_extraction/action_extraction/window_classification.py (stub)

---

#### Issue PL-06: Implement Parameter Extraction Stage
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the Parameter Extraction stage (currently a stub). Extract action parameters from trace events.

**Current State**: Stub passthrough in autoactivity-data

**Implementation**:
- Identify parameter-rich events (form inputs, clicks with targets)
- Extract text inputs, click coordinates, element IDs
- Normalize parameter values
- Map to action parameter types (string, number, boolean)

**Acceptance Criteria**:
- [ ] Extracts text from input events
- [ ] Extracts click targets
- [ ] Extracts form field values
- [ ] Outputs Gold Parquet with parameter columns

**Autoactivity Reference**: 
- autoactivity-data #8 (open)
- autoactivity-data/action_extraction/action_extraction/parameter_extraction.py (stub)

---

---

### 3. Example Generation Pipeline

#### Issue PL-07: Implement Example Extraction Stage
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the first stage of example generation: fetch agent definitions and action inventory.

**Current State**: Stub in autoactivity-data (reads parquet, writes parquet)

**Implementation**:
- Read classified action data from previous pipeline
- Fetch ActionToolMap for Session's Suite from Backend API
- Fetch Tool definitions for mapped McpServer
- Attach tool metadata to each classified action
- Output parquet with action→tool mappings

**Acceptance Criteria**:
- [ ] Fetches ActionToolMap from Backend API
- [ ] Fetches Tool definitions
- [ ] Maps each action_id to tool_id
- [ ] Outputs parquet with mapping columns

**Autoactivity Reference**: 
- autoactivity-data #12 (open: "Build example generation pipeline bronze step")
- autoactivity-data/example_generation/example_generation/extraction.py (stub)

---

#### Issue PL-08: Implement Action-to-Tool Mapping Stage
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the mapping stage: convert classified actions to MCP tool call format.

**Current State**: Stub (adds UUID column)

**Implementation**:
- For each classified action, look up ActionToolMapping
- Map action parameters to tool parameters using ActionToolParameterMapping
- Convert parameter values to tool-expected types
- Format as tool call structure: `{"name": "tool_name", "arguments": {...}}`

**Acceptance Criteria**:
- [ ] Maps actions to tools via ActionToolMapping
- [ ] Maps parameters via ActionToolParameterMapping
- [ ] Validates parameter types match
- [ ] Outputs parquet with tool_call column (JSON)

**Autoactivity Reference**: 
- autoactivity-data #13 (open: "Build example generation pipeline silver step")
- autoactivity-data/example_generation/example_generation/mapping.py (stub)

---

#### Issue PL-09: Implement JSONL Message Generator
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the final stage: format tool calls as LLM training conversation JSONL.

**Current State**: Stub passthrough

**Implementation**:
- Generate system prompt from Suite context
- Generate user message from trace context (simplified description)
- Generate assistant message with tool_calls
- Format as JSONL with roles: system, user, assistant
- Write to object storage at `examples/<example-id>/messages.jsonl`

**JSONL Format**:
```jsonl
{"role": "system", "content": "You are an assistant for Gmail..."}
{"role": "user", "content": "Compose email to alice@example.com"}
{"role": "assistant", "content": null, "tool_calls": [{"id": "call_1", "type": "function", "function": {"name": "compose_email", "arguments": "{\"to\": \"alice@example.com\", ...}"}}]}
```

**Acceptance Criteria**:
- [ ] Generates system message with Suite context
- [ ] Generates user message from trace summary
- [ ] Generates assistant message with tool_calls array
- [ ] Writes valid JSONL to object storage
- [ ] Creates Example record in Backend database

**Autoactivity Reference**: 
- autoactivity-data #14 (open: "Build example generation pipeline gold step")
- autoactivity-data/example_generation/example_generation/generation.py (stub)

---

### 4. Pipeline Orchestration

#### Issue PL-11: Implement Processing Orchestrator
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the orchestrator that coordinates the full Session→Example pipeline end-to-end.

**Responsibilities**:
- Listen for new Session events (webhook or polling)
- Trigger Bronze/Silver/Gold trace processing
- Trigger Example generation pipeline
- Track processing status per Session
- Handle retries and failures
- Update Example records in Backend on completion

**Technology Options**:
- Celery with Redis/RabbitMQ
- Simple Python queue with async workers
- Azure Functions (if using Azure)

**Acceptance Criteria**:
- [ ] Triggers on new Session creation
- [ ] Runs full pipeline end-to-end
- [ ] Tracks status: pending, processing, complete, failed
- [ ] Retries failed stages (configurable max retries)
- [ ] Updates Backend with processing status
- [ ] Creates Example record on successful completion

---

#### Issue PL-12: Processing Status API
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Implement API endpoints to query processing status for Sessions.

**Endpoints**:
- `GET /v1/processing/sessions/{id}/status` — Get status
- `POST /v1/processing/sessions/{id}/retry` — Retry failed processing

**Status Values**: `pending`, `processing`, `complete`, `failed`

**Acceptance Criteria**:
- [ ] Returns current processing status
- [ ] Returns error messages for failed stages
- [ ] Retry endpoint re-queues failed sessions
- [ ] User can only query their own sessions

---

### 5. Data Quality & Testing

#### Issue PL-13: Implement Trace Validation
**Status**: `[CARRY-OVER]` | **Priority**: `P1`

**Description**:
Port the trace validation logic from autoactivity-data bronze layer. Ensure uploaded traces meet format requirements.

**Validations**:
- JSONL structure (valid JSON per line)
- Required fields: timestamp, event_type
- Screenshot format: PNG, valid MIME type
- Timestamp ordering (monotonic)

**Acceptance Criteria**:
- [ ] Validates all trace formats
- [ ] Rejects invalid sessions with clear error messages
- [ ] Logs validation failures for debugging

**Autoactivity Reference**: autoactivity-data bronze extraction has comprehensive validation

---

#### Issue PL-11: Classification Confidence Scoring
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Implement confidence scoring for LLM action classifications. Flag low-confidence results for manual review.

**Implementation**:
- Parse confidence from LLM response (if available)
- Calculate confidence based on parameter completeness
- Threshold for auto-accept (e.g., > 0.8)
- Flag for review if below threshold

**Acceptance Criteria**:
- [ ] Assigns confidence score to each classification
- [ ] Flags low-confidence (<0.8) classifications
- [ ] Creates "needs_review" column in output
- [ ] Logs flagged classifications

---

#### Issue PL-12: Integration Tests for Pipeline Stages
**Status**: `[ADAPTATION]` | **Priority**: `P1`

**Description**:
Port and adapt integration tests from autoactivity-data. Test each pipeline stage with real trace data.

**Test Coverage**:
- Bronze: Load valid/invalid traces
- Silver: Event merging patterns
- Gold: Window classification, parameter extraction
- Example generation: Full pipeline with known actions

**Acceptance Criteria**:
- [ ] Each stage has integration tests
- [ ] Tests use sample trace data
- [ ] Tests verify output schema
- [ ] Tests run in CI/CD

**Autoactivity Reference**: autoactivity-data/action_extraction/tests/

---

### 5. Infrastructure

#### Issue PL-13: Pipeline Configuration Management
**Status**: `[NEW]` | **Priority**: `P2`

**Description**:
Implement configuration management for pipeline settings (LLM provider, API keys, storage paths).

**Configuration**:
- Backend API base URL
- Object storage connection string
- OpenRouter API key
- LLM model selection (per-suite)
- Confidence threshold
- Retry limits

**Deliverables**:
- `.env.example` file with all settings
- Pydantic settings model
- Environment-specific configs (dev, prod)

**Acceptance Criteria**:
- [ ] All settings configurable via environment variables
- [ ] Validation of required settings on startup
- [ ] Documented in README

---

#### Issue PL-14: Pipeline Metrics & Logging
**Status**: `[CARRY-OVER]` | **Priority**: `P2`

**Description**:
Port the metrics generation from autoactivity-data. Track processing stats and pipeline health.

**Metrics**:
- Events processed per stage
- Merge ratios (Silver layer)
- Classification confidence distribution
- Processing time per stage
- Storage size per Session

**Carry-Over Work**:
- autoactivity-data generates metrics JSON per run

**Changes Required**:
- Add metrics for new stages (Gold, Example generation)
- Aggregate metrics across multiple sessions
- Optional: Send metrics to monitoring service (Azure Monitor, Datadog)

**Acceptance Criteria**:
- [ ] Generates metrics JSON per pipeline run
- [ ] Metrics include all stages
- [ ] Logged to console and file

**Autoactivity Reference**: autoactivity-data outputs `metrics_{timestamp}.json`

---

#### Issue PL-15: AzureML Pipeline Runner (Optional)
**Status**: `[NEW]` | **Priority**: `P2` (Deferred)

**Description**:
Implement AzureML cloud runner for pipeline execution. This enables scalable cloud processing.

**Current State**: TODO in autoactivity-data

**Implementation**:
- AzureML workspace configuration
- Component registration
- Pipeline submission script
- Monitoring and logging

**Acceptance Criteria**:
- [ ] Pipeline YAML runs on AzureML
- [ ] All stages execute in cloud
- [ ] Outputs written to Azure Blob Storage
- [ ] Logs accessible via AzureML UI

**Note**: This is optional for MVP; AzureML handles deployment and orchestration natively.

**Autoactivity Reference**: 
- autoactivity-data #2, #4, #5 (open: AzureML setup issues)

**Dropped Issues**:
- PL-07 (LLM Action Classifier) — **DROPPED**: Redundant with PL-05 (Window Classification)
- PL-11 (Processing Orchestrator) — **MOVED TO BACKEND** as BE-18 (Example Creation & Processing Endpoint)
- PL-12 (Processing Status API) — **MOVED TO BACKEND** as part of BE-18 (Example status field)
- PL-18 (Docker & Deployment) — **DROPPED**: AzureML handles deployment

---

## Milestone #3: Frontend MVP

**Target Repo**: CRSS-AI/tracepipe-frontend

### 1. Project Setup

#### Issue FE-01: Next.js/Astro Project Scaffolding
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Initialize the frontend project with chosen framework (Next.js recommended for B2B SaaS).

**Technology Stack**:
- Next.js 14+ (App Router) or Astro
- TypeScript
- Tailwind CSS
- React 18+

**Deliverables**:
- `package.json` with dependencies
- `tsconfig.json` for TypeScript
- Directory structure: `src/app/`, `src/components/`, `src/lib/`
- Environment variable setup (`.env.example`)

**Acceptance Criteria**:
- [ ] `npm install` works
- [ ] `npm run dev` starts dev server
- [ ] TypeScript compilation works
- [ ] Hot reload works
- [ ] Base layout renders

---

#### Issue FE-02: Azure Entra External ID Client Integration
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Integrate Azure Entra External ID (formerly Azure AD B2C) for frontend user authentication. This is the **client-side** portion of cross-cutting auth — see BE-03 for backend token validation.

**Requirements**:
- User registration flow
- User login flow
- Session management (JWT tokens)
- Logout
- Protected routes (client-side and server-side)

**Implementation**:
- Use `@azure/msal-browser` or `@azure/msal-react`
- Configure against same Entra ID tenant as backend
- Implement auth provider component
- Store tokens securely (httpOnly cookies or secure storage)
- Pass Bearer tokens to backend in API requests

**Acceptance Criteria**:
- [ ] User can register new account
- [ ] User can log in with credentials
- [ ] Session persists across page refreshes
- [ ] User can log out
- [ ] Protected pages redirect to login if unauthenticated
- [ ] Tokens refresh automatically before expiry
- [ ] Frontend sends tokens to backend for validation

**Note**: This is cross-cutting with BE-03 (backend token validation). Azure Entra External ID is the platform identity provider.

---

### 2. Core Pages

#### Issue FE-03: Landing Page
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Create the landing page explaining Tracepipe and prompting registration/login.

**Content**:
- Hero section with value proposition
- Features overview (trace upload, training data generation)
- Usage-based pricing info (no subscription tiers)
- Call-to-action: "Get Started" → registration

**Acceptance Criteria**:
- [ ] Responsive design (mobile, tablet, desktop)
- [ ] Clean, professional UI
- [ ] "Get Started" button navigates to registration
- [ ] "Log In" link navigates to login

---

#### Issue FE-04: User Dashboard
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Create the main dashboard shown after login. Displays usage overview and quick actions.

**Content**:
- Welcome message with user name
- Summary cards: **Token usage (month), Storage (GB×time), Sessions uploaded, Examples generated**
- Quick actions: Upload trace, Generate API key, View docs
- Recent sessions list (table with session_id, suite, created_at)

**Acceptance Criteria**:
- [ ] Protected route (requires authentication)
- [ ] Fetches data from Backend API
- [ ] Summary cards display **token usage and storage** (not API calls)
- [ ] Recent sessions list is paginated
- [ ] Quick action buttons navigate correctly

**Note**: Cost units are **tokens** and **storage×time**, not API calls.

---

#### Issue FE-05: API Key Management Page
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Create the API key management page where users generate, view, and revoke keys.

**Features**:
- List of API keys (table with key prefix, created_at, last_used)
- "Generate New Key" button → shows key once in modal
- "Revoke" button per key → confirms, then revokes
- Copy-to-clipboard for new keys

**Acceptance Criteria**:
- [ ] Lists all user's API keys (masked: `tp_live_****...****`)
- [ ] Generate button calls Backend API, shows full key once
- [ ] Revoke button calls Backend API, removes key from list
- [ ] Copy button works for new keys
- [ ] User cannot see key again after modal closes

---

#### Issue FE-06: Trace Capture How-To Page
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Create a guide page explaining how to capture browser traces using `chrome://traces`.

**Content**:
- Step-by-step instructions with screenshots
- Which event categories to select
- How to start/stop recording
- How to export trace file
- Link to upload page

**Acceptance Criteria**:
- [ ] Clear, numbered steps
- [ ] Screenshots for each step
- [ ] Event category recommendations (input, screenshots, network)
- [ ] Link to session upload page
- [ ] Works on desktop and tablet

---

### 3. Payment Integration

#### Issue FE-07: Stripe Usage-Based Billing Integration
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Integrate Stripe for **usage-based monthly billing** (not subscriptions). Users add a card on file and are charged at the end of each month based on actual usage (tokens consumed, storage×time).

**Payment Model**:
- No subscriptions, no tiers, no recurring charges
- User adds payment method via Stripe SetupIntent
- Usage tracked throughout the month
- Backend reports usage to Stripe (metered billing / usage records)
- Stripe generates invoice at month-end and charges card on file

**Flow**:
1. User registers → prompted to add payment method
2. Frontend creates Stripe SetupIntent (via Backend API)
3. User enters card details (Stripe Elements)
4. Card saved to user's Stripe Customer (not charged yet)
5. Usage accrues during month
6. Stripe auto-invoices at month-end based on reported usage

**Deliverables**:
- "Add Payment Method" page/modal
- Stripe Elements integration for card input
- Setup confirmation flow
- Payment method display (card last 4 digits, expiry)
- "Update Payment Method" flow

**Acceptance Criteria**:
- [ ] User can add card via SetupIntent
- [ ] Card saved to Stripe Customer without charge
- [ ] Test mode works (Stripe test cards)
- [ ] User sees confirmation after adding card
- [ ] User can view/update payment method
- [ ] No subscription charges occur

**Note**: Backend (separate issue) will handle usage reporting to Stripe and invoice generation.

---

### 4. Usage Metrics

#### Issue FE-08: Usage Dashboard
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Display usage metrics for the current billing period. Show **tokens consumed** and **storage usage**, not API calls.

**Metrics**:
- **Tokens consumed** (count, by model)
- **Storage used** (GB×hours)
- Sessions uploaded (count)
- Examples generated (count)
- Current billing period dates
- Estimated cost for current period

**Visualization**:
- Line graphs for token usage over time
- Bar chart for storage growth
- Cost breakdown (tokens vs storage)

**Acceptance Criteria**:
- [ ] Fetches usage data from Backend API
- [ ] Displays current billing period (month-to-date)
- [ ] Shows **token consumption** (not API calls)
- [ ] Shows **storage usage** (GB×hours)
- [ ] Displays estimated cost
- [ ] Updates on page load (no auto-refresh needed for MVP)

**Note**: Cost units are tokens and storage×time, NOT API call counts.

---

### 5. Session Upload

#### Issue FE-09: Session Upload Page
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Create the page for uploading session trace bundles.

**Features**:
- File upload inputs: input_events.jsonl, network_traffic.jsonl, screenshots.zip
- Suite selector (dropdown fetched from Backend API)
- Upload button → sends multipart form to Backend API
- Progress indicator during upload
- Success/error messages

**Acceptance Criteria**:
- [ ] File inputs accept correct file types
- [ ] Suite dropdown populated from Backend API
- [ ] Upload button sends multipart form data
- [ ] Progress bar shows upload progress
- [ ] Success message shows session_id
- [ ] Error messages display validation errors
- [ ] Redirect to dashboard after successful upload

---

### 6. Testing & Deployment

#### Issue FE-10: Frontend Integration Tests
**Status**: `[NEW]` | **Priority**: `P2`

**Description**:
Implement integration tests for critical user flows.

**Test Scenarios**:
- User registration and login
- API key generation and revocation
- Session upload (mocked Backend API)
- Stripe checkout (test mode)

**Technology**:
- Playwright or Cypress for E2E tests
- React Testing Library for component tests

**Acceptance Criteria**:
- [ ] All critical flows have E2E tests
- [ ] Tests run in CI/CD pipeline
- [ ] Tests use mocked Backend API (no real data)
- [ ] Tests pass consistently

**Dropped/Replaced Issues**:
- **FE-07** (Stripe Checkout) — **REPLACED** with FE-07 (Stripe Usage-Based Billing)
- **FE-08** (Stripe Customer Portal) — **REPLACED** with FE-08 (Usage Dashboard with tokens/storage)

**Note**: Payment model changed from subscriptions to usage-based monthly billing. Cost tracking changed from API calls to tokens and storage×time.

---

## Cross-Cutting Issues

These issues span multiple milestones or affect the overall project infrastructure.

### CI/CD

#### Issue CC-01: GitHub Actions Workflow for Backend
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Set up CI/CD pipeline for tracepipe-backend.

**Workflow Steps**:
- Lint (ruff/pylint)
- Run tests (pytest)
- Build Docker image
- Push image to registry (Azure Container Registry or Docker Hub)
- Deploy to staging (optional for MVP)

**Acceptance Criteria**:
- [ ] Workflow runs on push to `main` and PRs
- [ ] Lint fails on style violations
- [ ] Tests must pass before merge
- [ ] Docker image built and pushed on main branch

---

#### Issue CC-02: GitHub Actions Workflow for Pipelines
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Set up CI/CD pipeline for tracepipe-pipelines.

**Workflow Steps**:
- Lint (ruff/pylint)
- Run tests (pytest)
- Build Docker image for workers
- Push image to registry

**Acceptance Criteria**:
- [ ] Workflow runs on push to `main` and PRs
- [ ] Tests must pass before merge
- [ ] Docker image built and pushed on main branch

---

#### Issue CC-03: GitHub Actions Workflow for Frontend
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Set up CI/CD pipeline for tracepipe-frontend.

**Workflow Steps**:
- Lint (ESLint)
- Type check (TypeScript)
- Run tests (Playwright/Cypress)
- Build production bundle
- Deploy to Vercel/Azure Static Web Apps

**Acceptance Criteria**:
- [ ] Workflow runs on push to `main` and PRs
- [ ] Lint and type check must pass
- [ ] Tests must pass before merge
- [ ] Production build successful
- [ ] Automatic deployment on main branch

---

### Documentation

#### Issue CC-04: Update Documentation for Tracepipe Model
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Update tracepipe-docs to reflect implementation decisions and any deviations from the initial design.

**Updates Needed**:
- API endpoint documentation (actual routes vs. planned)
- Authentication flow details
- Pipeline stage implementation details
- Deployment architecture
- Troubleshooting guides

**Acceptance Criteria**:
- [ ] All API endpoints documented with examples
- [ ] Pipeline stages documented with input/output schemas
- [ ] Frontend pages documented with screenshots
- [ ] Deployment guide complete
- [ ] Last reviewed dates updated

---

#### Issue CC-05: OpenAPI Documentation & SDK Generation
**Status**: `[NEW]` | **Priority**: `P2`

**Description**:
Generate client SDKs from OpenAPI spec for easier API consumption.

**SDKs to Generate**:
- Python SDK (via `openapi-generator`)
- TypeScript SDK (for frontend)
- CLI tool (optional, nice-to-have)

**Acceptance Criteria**:
- [ ] SDKs generated from openapi.json
- [ ] SDKs published to package registries (PyPI, npm)
- [ ] SDK usage examples in documentation
- [ ] SDKs include authentication helpers

---

### Integration Testing

#### Issue CC-06: End-to-End Integration Tests
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Create end-to-end integration tests that span all three components (Frontend, Backend, Pipelines).

**Test Scenarios**:
1. User registers → subscribes → generates API key → uploads session → views example
2. Pipeline processes session → creates example → user downloads JSONL
3. User revokes API key → API request fails with 401

**Test Environment**:
- Docker Compose with all services
- Test database (PostgreSQL)
- Test object storage (MinIO or Azure Storage Emulator)
- Test Stripe account (test mode)

**Acceptance Criteria**:
- [ ] All scenarios pass end-to-end
- [ ] Tests use Docker Compose for full stack
- [ ] Tests clean up after themselves
- [ ] Tests run in CI/CD (optional for MVP, can be manual)

---

## Summary

**Total Issues**: 51 (after corrections and consolidations)

### By Milestone
- **Backend MVP**: 24 issues (BE-01 through BE-24)
- **Pipelines MVP**: 15 issues (PL-01 through PL-15)
- **Frontend MVP**: 10 issues (FE-01 through FE-10)
- **Cross-Cutting**: 6 issues (CC-01 through CC-06)

### By Status

**Carry-Over** (Direct ports from autoactivity): ~6 issues
- BE-04 (Docker), BE-21 (Model entity), PL-01 (Bronze loader), PL-02 (Silver normalizer), PL-03 (Pipeline YAML), PL-04 (Local runner)

**Adaptation** (Exists but needs refactoring): ~15 issues
- BE-02 (Port scaffolding), BE-05 (Session model), BE-06 (Session upload), BE-07 (Session retrieval), BE-08 (Suite read-only), BE-09 (Action read-only), BE-10 (McpServer read-only), BE-11 (Tool read-only), BE-12 (ActionToolMap read-only), BE-17 (API key mgmt), BE-22 (Seeding), BE-24 (Integration tests), PL-10 (Trace validation), PL-12 (Pipeline tests)

**New** (Net-new for Tracepipe): ~30 issues
- Backend: BE-01, BE-03, BE-13, BE-14, BE-15, BE-16, BE-18, BE-19, BE-23
- Pipelines: PL-05, PL-06, PL-07, PL-08, PL-09, PL-11, PL-13, PL-14, PL-15
- Frontend: FE-01, FE-02, FE-03, FE-04, FE-05, FE-06, FE-07, FE-08, FE-09, FE-10
- Cross-cutting: CC-01 through CC-06

### Major Changes from Original Draft

**Dropped Issues** (6):
- PL-07 (LLM Action Classifier) — redundant with PL-05
- PL-11 (Processing Orchestrator) — moved to BE-18
- PL-12 (Processing Status API) — merged into BE-18
- PL-18 (Docker/Deployment) — AzureML handles this
- Old FE-07 (Stripe Checkout subscriptions) — replaced with usage-based billing
- Old FE-08 (Stripe Customer Portal) — replaced with usage dashboard

**New/Modified Issues**:
- BE-18: Major rewrite for Example creation with AP2 payment model + status field
- Session.description field added (PL-01)
- Example.status field added (BE-01, BE-18)
- Changed from subscriptions to usage-based monthly billing (FE-07)
- Changed cost tracking from API calls to tokens + storage×time (FE-04, FE-08)
- All Capability Surface endpoints (Suite, Action, McpServer, Tool, ActionToolMap) are now read-only

---

## Next Steps

1. **Run milestone sync** — Create milestones in subrepos via `sync-milestones.py`
2. **Create labels** — Set up status, priority, component, and type labels in each subrepo
3. **File issues** — Use `gh issue create` to file in native repos with milestone assignment
4. **Add to Project** — Aggregate all issues in centralized GitHub Project
5. **Link dependencies** — Add cross-repo issue references (e.g., `CRSS-AI/tracepipe-backend#XX`)
6. **Begin implementation** — Start with Backend MVP (P0 issues first)

---

_Document generated: 2026-02-11_  
_Last updated: 2026-02-13_  
_Target milestones: Backend MVP, Pipelines MVP, Frontend MVP_  
_Total issues: 51 (fine-grained decomposition)_
