# Tracepipe MVP GitHub Issues

**Status**: Draft — not yet filed in GitHub  
**Target Repository**: CRSS-AI/tracepipe (centralized milestone management)  
**Generated**: 2026-02-11

---

## Instructions for Filing Issues in GitHub

This section provides guidance for creating these issues in the CRSS-AI/tracepipe repository.

### Repository & Milestone Setup

**Target Repository**: `CRSS-AI/tracepipe`  
**Rationale**: Centralized milestone management per AGENTS.md — all issues tracked in parent repo even though work happens in submodules.

**Existing GitHub Milestones** (already created):
- Milestone #1: "Pipelines PoC" (use for Pipelines MVP issues)
- Milestone #2: "Backend PoC" (use for Backend MVP issues)
- Milestone #3: "Frontend PoC" (use for Frontend MVP issues)

**Note**: GitHub milestones say "PoC" but documentation says "MVP" — both terms refer to the same deliverables.

### Issue Naming Convention

**Format**: `[Component] Brief Title`

**Examples**:
- `[Backend] Database Schema Migration from AutoActivity` (Issue BE-01)
- `[Pipelines] Port Bronze Trace Loader` (Issue PL-01)
- `[Frontend] Next.js Project Scaffolding` (Issue FE-01)
- `[CI/CD] GitHub Actions Workflow for Backend` (Issue CC-01)

**Component Prefixes**:
- `[Backend]` — Backend API issues (BE-XX)
- `[Pipelines]` — Data pipeline issues (PL-XX)
- `[Frontend]` — Storefront UI issues (FE-XX)
- `[CI/CD]` — DevOps/automation issues (CC-XX)
- `[Docs]` — Documentation issues (CC-XX)
- `[Integration]` — End-to-end testing issues (CC-XX)

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

| Issue Prefix | Milestone Number | Milestone Name |
|--------------|------------------|----------------|
| BE-01 through BE-23 | #2 | Backend PoC |
| PL-01 through PL-19 | #1 | Pipelines PoC |
| FE-01 through FE-11 | #3 | Frontend PoC |
| CC-01 (Backend CI/CD) | #2 | Backend PoC |
| CC-02 (Pipelines CI/CD) | #1 | Pipelines PoC |
| CC-03 (Frontend CI/CD) | #3 | Frontend PoC |
| CC-04, CC-05, CC-06 | No milestone (cross-cutting) | Leave unassigned or create "Infrastructure" milestone |

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

### Automation Recommendations

**Using GitHub CLI** (`gh`):

```bash
# Create an issue with labels and milestone
gh issue create \
  --repo CRSS-AI/tracepipe \
  --title "[Backend] Database Schema Migration from AutoActivity" \
  --body-file issue-be-01.md \
  --milestone "Backend PoC" \
  --label "status: adaptation,priority: P0,component: backend,type: refactor"

# Bulk create issues from a script
for issue in issues/*.md; do
  gh issue create --repo CRSS-AI/tracepipe --body-file "$issue" --label "..." --milestone "..."
done
```

**Scripting Approach** (optional):
- Extract each issue from this document into separate markdown files
- Parse metadata (status, priority, component) to generate labels
- Use GitHub CLI or API to create issues programmatically
- Link issues automatically (e.g., "Depends on #XX") after creation

### Post-Filing Steps

After all issues are filed:

1. **Review dependencies** — Add "Depends on #XX" or "Blocks #YY" to issue bodies
2. **Assign issues** — Assign to team members based on expertise
3. **Create project board** — Organize issues in GitHub Projects with columns: Backlog, In Progress, Review, Done
4. **Set up automation** — Configure GitHub Actions to update issue status based on PR merges
5. **Link PRs to issues** — Use "Closes #XX" in PR descriptions to auto-close issues

### Cross-Repository Tracking

Since work happens in submodules but issues are tracked in the parent repo:

**In Pull Requests** (in submodule repos):
- Reference parent repo issues: `Closes CRSS-AI/tracepipe#XX`
- This will auto-close the issue in the parent repo when PR merges

**Example PR Title** (in tracepipe-backend):
```
[Backend] Implement Session Upload Endpoint (CRSS-AI/tracepipe#XX)
```

**In Commit Messages** (in submodules):
```
feat(session): implement upload endpoint

Implements multipart form upload for session traces.

Closes CRSS-AI/tracepipe#XX
```

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

**GitHub Milestone**: #2 "Backend PoC"  
**Target Repo**: CRSS-AI/tracepipe-backend

### 1. Backend Infrastructure

#### Issue BE-01: Database Schema Migration from AutoActivity
**Status**: `[ADAPTATION]` | **Priority**: `P0`  
**Predecessor**: autoactivity-be has full SQLAlchemy models + Alembic migrations

**Description**:
Refactor the autoactivity-be database schema to align with the Tracepipe data model. Remove Task/Activity/Case/Instance orchestration entities and add simplified Session and Example entities.

**Changes Required**:
- Remove tables: `activities`, `activity_edges`, `tasks`, `cases`, `instances`, `human_instances`, `agent_instances`, `instance_actions`
- Keep tables: `users`, `suites`, `actions`, `action_parameters`, `mcp_servers`, `tools`, `tool_parameters`, `action_tool_maps`, `action_tool_mappings`, `action_tool_parameter_mappings`, `models`, `providers` (if separate table)
- Modify `sessions` table: Remove foreign keys to `instances`, add `suite_id` foreign key, update `storage_path` convention
- Add `examples` table with columns: `id`, `session_id`, `model_id`, `action_tool_map_id`, `model_configuration` (JSONB), `storage_path`, `created_at`
- Simplify `traces` table (if it exists) to reference sessions only

**Acceptance Criteria**:
- [ ] Alembic migration script created for schema changes
- [ ] All removed tables are dropped
- [ ] `sessions` table matches new data model (see `tracepipe-docs/docs/data_model.md`)
- [ ] `examples` table created with all required columns and foreign keys
- [ ] Migration runs successfully on empty database
- [ ] Rollback migration works

**Autoactivity Reference**: 
- `autoactivity-be/alembic/versions/` (4 existing migrations)
- `autoactivity-be/src/autoactivity/data/models/` (SQLAlchemy models)

---

#### Issue BE-02: Remove Orchestration Layer Code
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Remove all code related to Task/Activity/Case/Instance orchestration that doesn't exist in the Tracepipe model. Clean up imports, tests, and dependencies.

**Files to Remove/Modify**:
- Remove: `src/autoactivity/domain/task/`, `domain/activity/`, `domain/case/`, `domain/instance/`
- Remove: `src/autoactivity/application/task.py`, `application/case.py`, `application/instance.py`
- Remove: `src/autoactivity/api/v1/controllers/task.py`, `controllers/case.py`, `controllers/instance.py`
- Remove: `src/autoactivity/data/repositories/task_repository.py`, `case_repository.py`, `instance_repository.py`
- Update: `main.py` to remove orchestration route registrations
- Remove: All tests for removed entities

**Acceptance Criteria**:
- [ ] No references to Task/Activity/Case/Instance in codebase
- [ ] Application starts without errors
- [ ] Test suite passes (orchestration tests removed)
- [ ] No orphaned imports or dependencies

**Autoactivity Reference**: autoactivity-be has ~60+ closed issues for Case/Instance CRUD

---

#### Issue BE-03: API Key Authentication Middleware Integration
**Status**: `[CARRY-OVER]` | **Priority**: `P0`

**Description**:
Port the existing API key authentication middleware from autoactivity-be. Ensure it works with the Tracepipe User model and validates `X-API-Key` headers.

**Carry-Over Work**:
- `autoactivity-be/src/autoactivity/core/security.py` has `verify_api_key()` dependency
- Authentication already implemented and tested

**Changes Required**:
- Copy `core/security.py` authentication logic
- Verify User model compatibility (UUID ids, api_keys relationship)
- Apply to all protected endpoints via FastAPI dependencies

**Acceptance Criteria**:
- [ ] `verify_api_key()` dependency function exists
- [ ] Validates API keys against `users` table
- [ ] Returns 401 for missing/invalid keys
- [ ] Returns User context for valid keys
- [ ] All protected endpoints use this dependency

**Autoactivity Reference**: autoactivity-be #31 (closed: "API key handling")

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
**Status**: `[ADAPTATION]` | **Priority**: `P0**Description**:
Implement the Session upload endpoint. Accept multipart form data with trace bundles (input_events.jsonl, network_traffic.jsonl, screenshots.zip) and store at the new storage path convention.

**Changes Required**:
- Endpoint: `POST /v1/sessions`
- Request: Multipart form with files + `suite_id` field
- Storage path: `sessions/<session-id>/` (not instance-based like autoactivity)
- Upload to object storage (Azure Blob Storage)
- Create Session record in database

**Acceptance Criteria**:
- [ ] Endpoint accepts multipart/form-data
- [ ] Validates required files (input_events.jsonl, network_traffic.jsonl, screenshots.zip)
- [ ] Stores files at `sessions/<uuid>/` in object storage
- [ ] Creates Session record with correct `storage_path`
- [ ] Returns Session metadata (id, storage_path, created_at)
- [ ] Returns 400 for invalid suite_id
- [ ] Returns 401 for unauthenticated requests

**Autoactivity Reference**: 
- autoactivity-be #58 (closed: "Update session storage logic")
- autoactivity-be/src/autoactivity/application/session.py

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

#### Issue BE-08: Suite CRUD Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Extend the existing Suite service from autoactivity-be to support full CRUD operations. Currently only list is implemented.

**Current State** (autoactivity-be):
- `GET /suites/` — ✅ Implemented
- `GET /suites/{id}` — ❌ NotImplementedError
- `POST /suites/` — ❌ NotImplementedError
- `PUT /suites/{id}` — ❌ NotImplementedError
- `DELETE /suites/{id}` — ❌ NotImplementedError

**Changes Required**:
- Implement `get_by_id()`, `create()`, `update()`, `delete()` in domain service
- Add controller methods for each endpoint
- Request/response DTOs for create/update

**Acceptance Criteria**:
- [ ] All 5 CRUD endpoints implemented
- [ ] Create validates required fields (name)
- [ ] Update allows partial updates
- [ ] Delete cascades to actions and action_tool_maps
- [ ] Returns 404 for non-existent suites

**Autoactivity Reference**: 
- autoactivity-be/src/autoactivity/domain/suite/ (partial implementation)

---

#### Issue BE-09: Action CRUD Endpoints
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Extend the existing Action service to support full CRUD operations. Currently only get_by_id is implemented.

**Current State** (autoactivity-be):
- `GET /actions/{id}` — ✅ Implemented
- `GET /suites/{suite_id}/actions` — ❌ NotImplementedError
- `POST /suites/{suite_id}/actions` — ❌ NotImplementedError
- `PUT /actions/{id}` — ❌ NotImplementedError
- `DELETE /actions/{id}` — ❌ NotImplementedError

**Changes Required**:
- Implement missing methods in domain service
- Nested routes under `/suites/{suite_id}/actions`
- ActionParameter handling (nested creation)

**Acceptance Criteria**:
- [ ] List actions for a suite
- [ ] Create action with parameters
- [ ] Update action and parameters
- [ ] Delete action (cascades to parameters and mappings)
- [ ] Returns 404 for non-existent suite/action

**Autoactivity Reference**: 
- autoactivity-be #109 (closed: "Implement action inventory endpoint")
- autoactivity-be/src/autoactivity/domain/action/

---

#### Issue BE-10: McpServer CRUD Endpoints
**Status**: `[CARRY-OVER]` | **Priority**: `P1`

**Description**:
Implement CRUD endpoints for McpServer entities. This is similar to Suite but for the agent-facing tool catalog.

**Endpoints**:
- `GET /v1/mcp-servers` — List all MCP servers
- `GET /v1/mcp-servers/{id}` — Get MCP server with tools
- `POST /v1/mcp-servers` — Create MCP server
- `PUT /v1/mcp-servers/{id}` — Update MCP server
- `DELETE /v1/mcp-servers/{id}` — Delete MCP server

**Acceptance Criteria**:
- [ ] All CRUD operations work
- [ ] Create validates required fields (name)
- [ ] Get returns nested tools
- [ ] Delete cascades to tools and action_tool_maps

---

#### Issue BE-11: Tool CRUD Endpoints (Nested under McpServer)
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Implement nested CRUD for Tools under McpServers.

**Endpoints**:
- `GET /v1/mcp-servers/{id}/tools` — List tools
- `POST /v1/mcp-servers/{id}/tools` — Create tool
- `PUT /v1/tools/{id}` — Update tool
- `DELETE /v1/tools/{id}` — Delete tool

**Acceptance Criteria**:
- [ ] List filters by mcp_server_id
- [ ] Create validates mcp_server_id exists
- [ ] Tool parameters are included in responses
- [ ] Delete cascades to parameters and mappings

---

#### Issue BE-12: ActionToolMap CRUD Endpoints
**Status**: `[CARRY-OVER]` | **Priority**: `P0`

**Description**:
Port the ActionToolMap CRUD implementation from autoactivity-be. This entity binds Suites to McpServers.

**Carry-Over Work**:
- Full CRUD already implemented in autoactivity-be
- Includes nested ActionToolMapping creation

**Changes Required**:
- Copy implementation from autoactivity-be
- Verify compatibility with simplified data model
- Ensure cascading deletes work

**Acceptance Criteria**:
- [ ] All CRUD operations work
- [ ] Can create with nested tool mappings
- [ ] Can create with nested parameter mappings
- [ ] GET includes full mapping tree
- [ ] Delete cascades correctly

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

### 6. A2P & MCP Integration

#### Issue BE-18: A2P (Agent-to-Platform) Endpoint
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Implement the Agent-to-Platform protocol endpoint for agents to submit requests to the platform.

**Endpoint**: `POST /v1/a2p/requests`

**Request Body**:
```json
{
  "agentId": "string",
  "payload": {...}
}
```

**Acceptance Criteria**:
- [ ] Endpoint accepts A2P requests
- [ ] Validates agent authentication
- [ ] Returns structured response
- [ ] Logs requests for audit

**Note**: Detailed A2P protocol spec TBD — this is scaffolding.

---

#### Issue BE-19: MCP Server Endpoint
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Implement an MCP (Model Context Protocol) server endpoint that exposes Tracepipe tools to LLM agents.

**Endpoints**:
- `GET /v1/mcp/tools` — List available tools
- `POST /v1/mcp/execute` — Execute a tool

**Tools to Expose**:
- `get_examples` — Retrieve training examples
- `get_session_trace` — Retrieve session trace data
- `list_suites` — List available suites

**Acceptance Criteria**:
- [ ] MCP-compatible tool listing
- [ ] Tool execution works via POST
- [ ] Integrates with existing services (no duplication)
- [ ] Returns MCP-standard responses

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

### 8. Database & Migrations

#### Issue BE-21: Model Entity Implementation
**Status**: `[CARRY-OVER]` | **Priority**: `P2`

**Description**:
Port the Model entity from autoactivity-be. Represents LLM/policy artifacts.

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
Create database seeding script for development/testing with sample data.

**Seed Data**:
- 2-3 Suites (Gmail, Google Calendar, GitHub)
- Actions for each Suite
- 2-3 McpServers with Tools
- ActionToolMaps binding Suites to McpServers
- Test User with API key
- Sample Models (GPT-4, Claude-3)

**Acceptance Criteria**:
- [ ] Script runs idempotently
- [ ] Creates all capability surface entities
- [ ] Creates test user with known API key
- [ ] Runnable via CLI: `python -m scripts.seed_db`

**Autoactivity Reference**: autoactivity-be #68 (closed: "Implement scripting to add Gmail action inventory to db")

---

#### Issue BE-23: Integration Tests for End-to-End Flows
**Status**: `[ADAPTATION]` | **Priority**: `P1`

**Description**:
Port and adapt integration tests from autoactivity-be. Test complete user journeys.

**Test Scenarios**:
1. User uploads session → retrieves session metadata
2. Create suite → create actions → create action-tool-map
3. Pipeline creates example → user retrieves example messages
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

**GitHub Milestone**: #1 "Pipelines PoC"  
**Target Repo**: CRSS-AI/tracepipe-pipelines

### 1. Pipeline Foundation

#### Issue PL-01: Port Bronze Trace Loader
**Status**: `[ADAPTATION]` | **Priority**: `P0`

**Description**:
Adapt the Bronze layer trace extraction from autoactivity-data. Update to work with the new Session storage convention (`sessions/<id>/` instead of instance-based paths).

**Carry-Over Work**:
- autoactivity-data bronze extraction is complete and tested
- Handles input events, screenshots, session metadata

**Changes Required**:
- Update storage path logic: `sessions/<session-id>/` instead of `raw/<session-uuid>/`
- Update Backend API integration: Call `/v1/sessions/{id}` instead of instance endpoints
- Remove Instance/Case metadata fetch (use Suite metadata from Session)
- Update Parquet schema to remove instance-related columns

**Acceptance Criteria**:
- [ ] Loads traces from new storage paths
- [ ] Validates JSONL structure
- [ ] Extracts screenshots with timestamps
- [ ] Fetches Session and Suite metadata from Backend API
- [ ] Outputs Bronze Parquet with correct schema
- [ ] Generates metrics JSON

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

#### Issue PL-07: Implement LLM-Based Action Classifier
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Implement the core action classification stage using LLM to map trace evidence to canonical Actions.

**Implementation**:
- Assemble multimodal trace context (events + screenshots)
- Fetch Suite-specific action inventory from Backend API
- Prompt LLM with trace evidence and action candidates
- Parse LLM response to extract action_id and parameters
- Assign confidence score

**Prompt Structure**:
```
You are analyzing a browser trace to identify user actions.

Suite: Gmail
Available Actions:
1. compose_email (to: string, subject: string, body: string)
2. send_email ()
3. reply_to_email (body: string)

Trace Evidence:
[Events + Screenshots]

Identify which action was performed and extract parameters.
```

**Acceptance Criteria**:
- [ ] Integrates with OpenRouter or LLM API
- [ ] Fetches action inventory from Backend API
- [ ] Sends multimodal context (events + base64 screenshots)
- [ ] Parses structured LLM response
- [ ] Assigns confidence score (0.0-1.0)
- [ ] Handles low-confidence classifications (flag for review)

**Autoactivity Reference**: 
- autoactivity-data #6 (open: "Build PoC for LLM-based action sequence classification")

---

### 3. Example Generation Pipeline

#### Issue PL-08: Implement Example Extraction Stage
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

#### Issue PL-09: Implement Action-to-Tool Mapping Stage
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

#### Issue PL-10: Implement JSONL Message Generator
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

#### Issue PL-14: Classification Confidence Scoring
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

#### Issue PL-15: Integration Tests for Pipeline Stages
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

### 6. Infrastructure

#### Issue PL-16: Pipeline Configuration Management
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

#### Issue PL-17: Pipeline Metrics & Logging
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

#### Issue PL-18: Docker & Deployment Configuration
**Status**: `[NEW]` | **Priority**: `P2`

**Description**:
Create Docker and deployment configs for the pipeline workers.

**Deliverables**:
- `Dockerfile` for pipeline workers
- `docker-compose.yml` with worker + queue + storage
- Kubernetes manifests (optional, future)

**Acceptance Criteria**:
- [ ] Dockerfile builds successfully
- [ ] Docker Compose starts worker + dependencies
- [ ] Worker connects to Backend API
- [ ] Worker connects to object storage

---

#### Issue PL-19: AzureML Pipeline Runner (Optional)
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

**Note**: This is optional for MVP; local runner is sufficient.

**Autoactivity Reference**: 
- autoactivity-data #2, #4, #5 (open: AzureML setup issues)

---

## Milestone #3: Frontend MVP

**GitHub Milestone**: #3 "Frontend PoC"  
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

#### Issue FE-02: Azure AD B2C Authentication Integration
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Integrate Azure AD B2C (Microsoft Entra External ID) for user authentication.

**Requirements**:
- User registration flow
- User login flow
- Session management (JWT tokens)
- Logout
- Protected routes (client-side and server-side)

**Implementation**:
- Use `@azure/msal-browser` or `@azure/msal-react`
- Configure Azure AD B2C tenant
- Implement auth provider component
- Store tokens securely (httpOnly cookies or secure storage)

**Acceptance Criteria**:
- [ ] User can register new account
- [ ] User can log in with credentials
- [ ] Session persists across page refreshes
- [ ] User can log out
- [ ] Protected pages redirect to login if unauthenticated
- [ ] Tokens refresh automatically before expiry

---

### 2. Core Pages

#### Issue FE-03: Landing Page
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Create the landing page explaining Tracepipe and prompting registration/login.

**Content**:
- Hero section with value proposition
- Features overview (trace upload, training data generation)
- Pricing tiers (linked to Stripe plans)
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
- Summary cards: Sessions uploaded, Examples generated, API calls this month
- Quick actions: Upload trace, Generate API key, View docs
- Recent sessions list (table with session_id, suite, created_at)

**Acceptance Criteria**:
- [ ] Protected route (requires authentication)
- [ ] Fetches data from Backend API
- [ ] Summary cards display correct counts
- [ ] Recent sessions list is paginated
- [ ] Quick action buttons navigate correctly

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

### 3. Stripe Integration

#### Issue FE-07: Stripe Checkout Integration
**Status**: `[NEW]` | **Priority**: `P0`

**Description**:
Integrate Stripe Checkout for subscription payments.

**Flow**:
1. User clicks "Subscribe" on dashboard or pricing page
2. Frontend creates Stripe Checkout session (via Backend API)
3. User redirected to Stripe-hosted checkout page
4. On success, redirected back to dashboard with success message
5. Backend webhook updates user subscription status

**Deliverables**:
- "Subscribe" button component
- Checkout session creation (calls Backend API)
- Success/cancel redirect handlers
- Subscription status display in dashboard

**Acceptance Criteria**:
- [ ] Subscribe button creates checkout session
- [ ] User redirected to Stripe checkout
- [ ] Test mode payments work (Stripe test cards)
- [ ] Success redirect shows confirmation message
- [ ] Subscription status updates in dashboard

---

#### Issue FE-08: Stripe Customer Portal Integration
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Integrate Stripe Customer Portal for subscription and billing management.

**Features**:
- Link to "Manage Billing" in user dropdown/dashboard
- Redirects to Stripe-hosted portal
- User can update payment method, view invoices, cancel subscription

**Implementation**:
- Button calls Backend API to create portal session
- Redirect to portal URL
- Return URL points back to dashboard

**Acceptance Criteria**:
- [ ] "Manage Billing" link works
- [ ] User redirected to Stripe portal
- [ ] User can view invoices in portal
- [ ] User can update payment method
- [ ] Return link brings user back to dashboard

---

### 4. Usage Metrics

#### Issue FE-09: Usage Dashboard
**Status**: `[NEW]` | **Priority**: `P1`

**Description**:
Display usage metrics and quota consumption for the current billing period.

**Metrics**:
- Sessions uploaded (count)
- Examples generated (count)
- API calls made (count)
- Storage used (GB)
- Quota limits (if applicable)

**Visualization**:
- Bar charts or line graphs for time-series data
- Progress bars for quota usage

**Acceptance Criteria**:
- [ ] Fetches usage data from Backend API
- [ ] Displays current billing period dates
- [ ] Shows usage counts with units
- [ ] Visual indicators for quota limits (if applicable)
- [ ] Updates on page load (no auto-refresh needed for MVP)

---

### 5. Session Upload

#### Issue FE-10: Session Upload Page
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

#### Issue FE-11: Frontend Integration Tests
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

## Summary by Status

### Carry-Over (Direct ports from autoactivity)
- **Total**: 9 issues
- BE-03 (Auth middleware), BE-04 (Docker), BE-12 (ActionToolMap), BE-21 (Model entity), PL-01 (Bronze loader), PL-02 (Silver normalizer), PL-03 (Pipeline YAML), PL-04 (Local runner), PL-17 (Metrics)

### Adaptation (Exists but needs refactoring)
- **Total**: 14 issues
- BE-01 (DB migration), BE-02 (Remove orchestration), BE-05 (Session model), BE-06 (Session upload), BE-07 (Session retrieval), BE-08 (Suite CRUD), BE-09 (Action CRUD), BE-17 (API key mgmt), BE-22 (Seeding), BE-23 (Integration tests), PL-13 (Trace validation), PL-15 (Pipeline tests)

### New (Net-new for Tracepipe)
- **Total**: 30 issues
- 11 Backend issues (BE-10, BE-11, BE-13, BE-14, BE-15, BE-16, BE-18, BE-19, BE-20)
- 8 Pipelines issues (PL-05 through PL-12, PL-14, PL-16, PL-18, PL-19)
- 11 Frontend issues (FE-01 through FE-11)
- 6 Cross-cutting issues (CC-01 through CC-06)

---

## Next Steps

1. **Review this document** with the team to confirm scope and priorities
2. **File issues in GitHub** at CRSS-AI/tracepipe with appropriate labels and milestones
3. **Prioritize issues** within each milestone (P0 first, then P1, then P2)
4. **Assign issues** to team members
5. **Begin implementation** starting with Backend MVP (foundation for Pipelines and Frontend)

---

_Document generated: 2026-02-11_  
_Target milestones: Backend MVP (#2), Pipelines MVP (#1), Frontend MVP (#3)_  
_Total issues: 53 (fine-grained decomposition)_
