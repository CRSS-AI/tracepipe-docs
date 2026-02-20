# API Reference

_Last reviewed: 2026-02-20_

This is a static API reference for the Tracepipe platform. It describes every endpoint, request/response schema, and authentication mechanism. Use this as the contract to design and build against.

**Base URL**: `https://api.tracepipe.com/v1`

---

## Quickstart

### 1. Get an API key

After registering and adding a payment method through the [Tracepipe storefront](https://tracepipe.example.com), generate an API key from the API Keys page. The key is shown **once** — copy it immediately.

Your key looks like: `tp_live_abcdef123456789...`

### 2. Make your first API call

Verify your key works by fetching your profile:

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/users/me \
  -H "X-API-Key: tp_live_abcdef123456789..."
```

**Python**:
```python
import requests

response = requests.get(
    "https://api.tracepipe.example.com/v1/users/me",
    headers={"X-API-Key": "tp_live_abcdef123456789..."},
)
print(response.json())
```

**Response**:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "display_name": "Jane Smith"
}
```

### 3. Upload your first trace

```bash
curl -X POST https://api.tracepipe.example.com/v1/sessions \
  -H "X-API-Key: tp_live_..." \
  -F "suite_id=<suite-uuid>" \
  -F "input_events=@input_events.jsonl"
```

### 4. Trigger processing

```bash
curl -X POST https://api.tracepipe.example.com/v1/examples \
  -H "X-API-Key: tp_live_..." \
  -H "Content-Type: application/json" \
  -d '{"session_id": "<session-uuid>", "model_id": "<model-uuid>", "model_configuration": {"temperature": 0.7}}'
```

### 5. Retrieve your training data

Once processing completes, download the JSONL training messages:

```bash
curl https://api.tracepipe.example.com/v1/examples/<example-id>/messages \
  -H "X-API-Key: tp_live_..." \
  -o training_data.jsonl
```

---

## Authentication

All API requests require an API key in the `X-API-Key` header.

**Header format**:
```
X-API-Key: tp_live_abcdef123456789...
```

API keys are:
- Generated through the storefront UI
- Scoped to your user account
- Revocable at any time
- Shown only once at creation — store securely

**Unauthenticated requests** return `401 Unauthorized`.

**Requests with a revoked or invalid key** return `401 Unauthorized`.

---

## Sessions

Sessions represent uploaded trace recordings. Each Session belongs to a Suite (the application being recorded) and contains raw trace files stored in object storage.

### Upload a session

```
POST /v1/sessions
Content-Type: multipart/form-data
```

Upload an input event trace for processing.

**Request** (multipart form):

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `suite_id` | uuid | Yes | The Suite this trace belongs to |
| `description` | string | No | Free-text description of what the trace captures |
| `input_events` | file | Yes | JSONL file of user input events (keyboard, mouse, touch) |

**curl**:
```bash
curl -X POST https://api.tracepipe.example.com/v1/sessions \
  -H "X-API-Key: tp_live_..." \
  -F "suite_id=550e8400-e29b-41d4-a716-446655440000" \
  -F "description=Recording of composing and sending an email in Gmail" \
  -F "input_events=@input_events.jsonl"
```

**Response** `201 Created`:
```json
{
  "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "suite_id": "550e8400-e29b-41d4-a716-446655440000",
  "description": "Recording of composing and sending an email in Gmail",
  "storage_path": "sessions/7c9e6679-7425-40de-944b-e07fc1f90ae7/",
  "created_at": "2026-02-19T10:30:00Z"
}
```

### Get a session

```
GET /v1/sessions/{id}
```

Retrieve metadata for a single session.

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/sessions/7c9e6679-7425-40de-944b-e07fc1f90ae7 \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "suite_id": "550e8400-e29b-41d4-a716-446655440000",
  "description": "Recording of composing and sending an email in Gmail",
  "storage_path": "sessions/7c9e6679-7425-40de-944b-e07fc1f90ae7/",
  "created_at": "2026-02-19T10:30:00Z"
}
```

### List sessions

```
GET /v1/sessions
```

List sessions for the authenticated user.

**Query parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `suite_id` | uuid | No | Filter by Suite |
| `page` | integer | No | Page number (default: 1) |
| `per_page` | integer | No | Results per page (default: 20, max: 100) |

**curl**:
```bash
curl "https://api.tracepipe.example.com/v1/sessions?suite_id=550e8400-e29b-41d4-a716-446655440000" \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "items": [
    {
      "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "user_id": "550e8400-e29b-41d4-a716-446655440000",
      "suite_id": "550e8400-e29b-41d4-a716-446655440000",
      "description": "Recording of composing and sending an email in Gmail",
      "storage_path": "sessions/7c9e6679-...",
      "created_at": "2026-02-19T10:30:00Z"
    }
  ],
  "total": 42,
  "page": 1,
  "per_page": 20
}
```

---

## Examples

Examples are processed training data derived from Sessions. Each Example contains JSONL-formatted messages suitable for model training.

### List examples

```
GET /v1/examples
```

**Query parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `session_id` | uuid | No | Filter by source Session |
| `suite_id` | uuid | No | Filter by Suite |
| `model_id` | uuid | No | Filter by Model used during processing |
| `status` | string | No | Filter by status: `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED` |
| `page` | integer | No | Page number (default: 1) |
| `per_page` | integer | No | Results per page (default: 20, max: 100) |

**curl**:
```bash
curl "https://api.tracepipe.example.com/v1/examples?session_id=7c9e6679-...&status=COMPLETED" \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "items": [
    {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "session_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "model_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "model_configuration": {
        "temperature": 0.7,
        "provider": "OPENAI"
      },
      "storage_path": "examples/a1b2c3d4-.../",
      "status": "COMPLETED",
      "created_at": "2026-02-19T11:00:00Z"
    }
  ],
  "total": 3,
  "page": 1,
  "per_page": 20
}
```

### Create an example

```
POST /v1/examples
Content-Type: application/json
```

Triggers pipeline processing for a session. Creates an Example with status `PENDING` and begins asynchronous processing. Poll the Example status to check for completion.

**Request body**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `session_id` | uuid | Yes | The Session to process |
| `model_id` | uuid | Yes | The Model to use for classification |
| `model_configuration` | object | No | Provider-specific settings (e.g., temperature) |

**curl**:
```bash
curl -X POST https://api.tracepipe.example.com/v1/examples \
  -H "X-API-Key: tp_live_..." \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "model_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "model_configuration": {"temperature": 0.7}
  }'
```

**Response** `201 Created`:
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "session_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "model_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "model_configuration": {
    "temperature": 0.7
  },
  "storage_path": "examples/a1b2c3d4-.../",
  "status": "PENDING",
  "created_at": "2026-02-19T11:00:00Z"
}
```

> **Note**: Processing is asynchronous. Poll `GET /v1/examples/{id}` to check status. When status is `COMPLETED`, retrieve messages via `GET /v1/examples/{id}/messages`.

### Get an example

```
GET /v1/examples/{id}
```

Retrieve metadata for a single example.

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/examples/a1b2c3d4-e5f6-7890-abcd-ef1234567890 \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "session_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "model_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
  "model_configuration": {
    "temperature": 0.7,
    "provider": "OPENAI"
  },
  "storage_path": "examples/a1b2c3d4-.../",
  "status": "COMPLETED",
  "created_at": "2026-02-19T11:00:00Z"
}
```

### Get example messages

```
GET /v1/examples/{id}/messages
```

Download the JSONL training messages for a completed example. Returns the raw JSONL file.

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/examples/a1b2c3d4-.../messages \
  -H "X-API-Key: tp_live_..." \
  -o training_data.jsonl
```

**Response** `200 OK` (`Content-Type: application/jsonl`):
```jsonl
{"role": "system", "content": "You are an assistant for Gmail. You can compose emails, manage inbox, and organize labels."}
{"role": "user", "content": "Compose a new email to alice@example.com with subject 'Meeting Tomorrow'"}
{"role": "assistant", "content": null, "tool_calls": [{"id": "call_1", "type": "function", "function": {"name": "compose_email", "arguments": "{\"to\": \"alice@example.com\", \"subject\": \"Meeting Tomorrow\"}"}}]}
```

> **Note**: Returns `409 Conflict` if the example status is not `COMPLETED`.

---

## Suites, Actions, MCP servers, and Tools

These entities define the vocabulary of actions and tools that Tracepipe uses to classify traces. Most API users will **read** these entities, not create them. They are typically set up by platform administrators.

### Suites

A Suite represents a human-facing application (e.g., Gmail, Shopify Admin).

#### List suites

```
GET /v1/suites
```

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/suites \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "items": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "Gmail"
    }
  ],
  "total": 5,
  "page": 1,
  "per_page": 20
}
```

#### Get a suite

```
GET /v1/suites/{id}
```

Returns the Suite with its list of Actions.

**Response** `200 OK`:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Gmail",
  "actions": [
    {
      "id": "d4e5f6a7-b8c9-0123-def4-567890123456",
      "name": "compose_email",
      "parameters": [
        {
          "id": "e5f6a7b8-c9d0-1234-ef45-678901234567",
          "name": "to",
          "type": "STRING",
          "required": true
        },
        {
          "id": "f6a7b8c9-d0e1-2345-f456-789012345678",
          "name": "subject",
          "type": "STRING",
          "required": true
        },
        {
          "id": "a7b8c9d0-e1f2-3456-4567-890123456789",
          "name": "body",
          "type": "STRING",
          "required": false
        }
      ]
    }
  ]
}
```

### Actions

Actions are canonical action definitions scoped to a Suite.

#### List actions for a suite

```
GET /v1/suites/{suite_id}/actions
```

#### Get an action

```
GET /v1/suites/{suite_id}/actions/{id}
```

### MCP servers

MCP Servers are agent-facing tool servers that expose Tools.

#### List MCP servers

```
GET /v1/mcp-servers
```

**Response** `200 OK`:
```json
{
  "items": [
    {
      "id": "b8c9d0e1-f2a3-4567-8901-234567890123",
      "name": "gmail-mcp-server"
    }
  ],
  "total": 3,
  "page": 1,
  "per_page": 20
}
```

#### Get an MCP server

```
GET /v1/mcp-servers/{id}
```

Returns the MCP Server with its list of Tools.

### Tools

Tools are operations invokable by an AI agent, exposed through an MCP Server.

#### List tools for an MCP server

```
GET /v1/mcp-servers/{mcp_server_id}/tools
```

#### Get a tool

```
GET /v1/mcp-servers/{mcp_server_id}/tools/{id}
```

**Response** `200 OK`:
```json
{
  "id": "c9d0e1f2-a3b4-5678-9012-345678901234",
  "mcp_server_id": "b8c9d0e1-f2a3-4567-8901-234567890123",
  "name": "compose_email",
  "parameters": [
    {
      "id": "d0e1f2a3-b4c5-6789-0123-456789012345",
      "name": "to",
      "type": "STRING",
      "required": true
    },
    {
      "id": "e1f2a3b4-c5d6-7890-1234-567890123456",
      "name": "subject",
      "type": "STRING",
      "required": true
    }
  ]
}
```

---

## Usage & billing

Usage is tracked throughout each billing period (calendar month) and invoiced at month-end. Costs are based on two metrics: **tokens consumed** (AI processing) and **storage × time** (data retention measured in GB×hours).

### Get current usage

```
GET /v1/usage
```

Returns usage metrics for the current billing period.

**Query parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `suite_id` | uuid | No | Filter usage by Suite |

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/usage \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "billing_period": {
    "start": "2026-02-01T00:00:00Z",
    "end": "2026-02-28T23:59:59Z"
  },
  "tokens": {
    "total": 1250000,
    "by_model": {
      "openai/gpt-4o": 800000,
      "anthropic/claude-3.5-sonnet": 450000
    }
  },
  "storage": {
    "gb_hours": 156.4,
    "current_gb": 2.3
  },
  "sessions_uploaded": 47,
  "examples_generated": 132,
  "estimated_cost": {
    "tokens": 12.50,
    "storage": 3.20,
    "total": 15.70,
    "currency": "USD"
  }
}
```

### List invoices

```
GET /v1/invoices
```

Returns past billing period invoices.

**Query parameters**:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | No | Page number (default: 1) |
| `per_page` | integer | No | Results per page (default: 12, max: 100) |

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/invoices \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "items": [
    {
      "id": "inv_a1b2c3d4e5f6",
      "billing_period": {
        "start": "2026-01-01T00:00:00Z",
        "end": "2026-01-31T23:59:59Z"
      },
      "tokens_consumed": 3400000,
      "storage_gb_hours": 412.8,
      "total_amount": 47.20,
      "currency": "USD",
      "status": "paid",
      "paid_at": "2026-02-01T06:00:00Z",
      "stripe_invoice_url": "https://invoice.stripe.com/i/..."
    }
  ],
  "total": 3,
  "page": 1,
  "per_page": 12
}
```

---

## Users & API keys

### Get current user

```
GET /v1/users/me
```

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/users/me \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "display_name": "Jane Smith"
}
```

### Generate API key

```
POST /v1/api-keys
```

Creates a new API key. The full key is returned **only in this response** — it cannot be retrieved later.

**curl**:
```bash
curl -X POST https://api.tracepipe.example.com/v1/api-keys \
  -H "X-API-Key: tp_live_..."
```

**Response** `201 Created`:
```json
{
  "id": "f6a7b8c9-d0e1-2345-f456-789012345678",
  "key": "tp_live_sk_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
  "prefix": "tp_live_sk_a1b2...o5p6",
  "created_at": "2026-02-19T10:00:00Z",
  "last_used_at": null
}
```

> **Important**: Copy the `key` value immediately. It will not be shown again.

### List API keys

```
GET /v1/api-keys
```

Returns all active API keys for the authenticated user. Keys are masked.

**curl**:
```bash
curl https://api.tracepipe.example.com/v1/api-keys \
  -H "X-API-Key: tp_live_..."
```

**Response** `200 OK`:
```json
{
  "items": [
    {
      "id": "f6a7b8c9-d0e1-2345-f456-789012345678",
      "prefix": "tp_live_sk_a1b2...o5p6",
      "created_at": "2026-02-19T10:00:00Z",
      "last_used_at": "2026-02-19T14:23:00Z"
    }
  ]
}
```

### Revoke API key

```
DELETE /v1/api-keys/{id}
```

Immediately revokes an API key. Subsequent requests using this key will return `401`.

**curl**:
```bash
curl -X DELETE https://api.tracepipe.example.com/v1/api-keys/f6a7b8c9-... \
  -H "X-API-Key: tp_live_..."
```

**Response** `204 No Content`

---

## Schemas

TypeScript-style type definitions for all request and response objects.

```typescript
// --- Core types ---

type UUID = string; // Format: "550e8400-e29b-41d4-a716-446655440000"
type Timestamp = string; // ISO 8601: "2026-02-19T10:30:00Z"

type ParameterType = "STRING" | "NUMBER" | "BOOLEAN" | "OBJECT" | "ARRAY";
type Provider = "OPENAI" | "ANTHROPIC" | "VERTEXAI" | "CUSTOM";
type ExampleStatus = "PENDING" | "PROCESSING" | "COMPLETED" | "FAILED";

// --- Paginated response wrapper ---

type PaginatedResponse<T> = {
  items: T[];
  total: number;
  page: number;
  per_page: number;
};

// --- User ---

type User = {
  id: UUID;
  display_name: string;
};

// --- API Key ---

type ApiKey = {
  id: UUID;
  prefix: string; // Masked key: "tp_live_sk_a1b2...o5p6"
  created_at: Timestamp;
  last_used_at: Timestamp | null;
};

type ApiKeyCreated = ApiKey & {
  key: string; // Full key, shown only at creation
};

// --- Session ---

type Session = {
  id: UUID;
  user_id: UUID;
  suite_id: UUID;
  description: string | null;
  storage_path: string;
  created_at: Timestamp;
};

// --- Example ---

type Example = {
  id: UUID;
  session_id: UUID;
  model_id: UUID;
  model_configuration: Record<string, unknown>;
  storage_path: string;
  status: ExampleStatus;
  created_at: Timestamp;
};

// --- Suites, Actions, MCP Servers, Tools ---

type Suite = {
  id: UUID;
  name: string;
  actions?: Action[];
};

type Action = {
  id: UUID;
  suite_id: UUID;
  name: string;
  parameters: ActionParameter[];
};

type ActionParameter = {
  id: UUID;
  action_id: UUID;
  name: string;
  type: ParameterType;
  required: boolean;
};

type McpServer = {
  id: UUID;
  name: string;
  tools?: Tool[];
};

type Tool = {
  id: UUID;
  mcp_server_id: UUID;
  name: string;
  parameters: ToolParameter[];
};

type ToolParameter = {
  id: UUID;
  tool_id: UUID;
  name: string;
  type: ParameterType;
  required: boolean;
};

// --- Model ---

type Model = {
  id: UUID;
  provider: Provider;
  name: string;
};

// --- Usage & Billing ---

type Usage = {
  billing_period: {
    start: Timestamp;
    end: Timestamp;
  };
  tokens: {
    total: number;
    by_model: Record<string, number>;
  };
  storage: {
    gb_hours: number;
    current_gb: number;
  };
  sessions_uploaded: number;
  examples_generated: number;
  estimated_cost: {
    tokens: number;
    storage: number;
    total: number;
    currency: string;
  };
};

type Invoice = {
  id: string;
  billing_period: {
    start: Timestamp;
    end: Timestamp;
  };
  tokens_consumed: number;
  storage_gb_hours: number;
  total_amount: number;
  currency: string;
  status: "draft" | "open" | "paid" | "void";
  paid_at: Timestamp | null;
  stripe_invoice_url: string | null;
};

// --- Errors ---

type ErrorResponse = {
  error: {
    code: string;
    message: string;
    details?: Record<string, unknown>;
  };
};

// --- Training messages (JSONL lines) ---

type TrainingMessage =
  | { role: "system"; content: string }
  | { role: "user"; content: string }
  | {
      role: "assistant";
      content: null;
      tool_calls: ToolCall[];
    };

type ToolCall = {
  id: string;
  type: "function";
  function: {
    name: string;
    arguments: string; // JSON-encoded string
  };
};
```

---

## Error handling

All errors return a consistent JSON structure:

```json
{
  "error": {
    "code": "not_found",
    "message": "Session with id '7c9e6679-...' not found",
    "details": {}
  }
}
```

### Error codes

| HTTP Status | Code | Description |
|-------------|------|-------------|
| `400` | `bad_request` | Malformed request, missing required fields, or invalid field values |
| `401` | `unauthorized` | Missing, invalid, or revoked API key |
| `403` | `forbidden` | Valid key but insufficient permissions for this resource |
| `404` | `not_found` | Resource does not exist or is not accessible to the authenticated user |
| `409` | `conflict` | Resource is in an incompatible state (e.g., downloading messages for a non-completed example) |
| `413` | `payload_too_large` | Upload exceeds maximum file size |
| `422` | `validation_error` | Request is well-formed but contains invalid data (e.g., invalid UUID format) |
| `429` | `rate_limited` | Too many requests; retry after the duration in `Retry-After` header |
| `500` | `internal_error` | Unexpected server error |

---

## Rate limits

API requests are rate-limited per API key.

| Endpoint group | Limit |
|---------------|-------|
| Session upload (`POST /sessions`) | 10 requests/minute |
| Read endpoints | 100 requests/minute |
| API key management | 10 requests/minute |

Rate limit information is included in response headers:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 97
X-RateLimit-Reset: 1708352400
```

When rate-limited, the response includes a `Retry-After` header (seconds).

---

## Endpoint summary

| Method | Path | Description |
|--------|------|-------------|
| **Sessions** | | |
| `POST` | `/v1/sessions` | Upload a trace bundle |
| `GET` | `/v1/sessions/{id}` | Get session metadata |
| `GET` | `/v1/sessions` | List sessions |
| **Examples** | | |
| `POST` | `/v1/examples` | Create example (trigger processing) |
| `GET` | `/v1/examples` | List examples |
| `GET` | `/v1/examples/{id}` | Get example metadata |
| `GET` | `/v1/examples/{id}/messages` | Download training messages (JSONL) |
| **Suites, Actions, MCP Servers, Tools** | | |
| `GET` | `/v1/suites` | List suites |
| `GET` | `/v1/suites/{id}` | Get suite with actions |
| `GET` | `/v1/suites/{suite_id}/actions` | List actions for a suite |
| `GET` | `/v1/suites/{suite_id}/actions/{id}` | Get an action |
| `GET` | `/v1/mcp-servers` | List MCP servers |
| `GET` | `/v1/mcp-servers/{id}` | Get MCP server with tools |
| `GET` | `/v1/mcp-servers/{mcp_server_id}/tools` | List tools for an MCP server |
| `GET` | `/v1/mcp-servers/{mcp_server_id}/tools/{id}` | Get a tool |
| **Usage & billing** | | |
| `GET` | `/v1/usage` | Get current billing period usage |
| `GET` | `/v1/invoices` | List past invoices |
| **Users & API keys** | | |
| `GET` | `/v1/users/me` | Get current user profile |
| `POST` | `/v1/api-keys` | Generate a new API key |
| `GET` | `/v1/api-keys` | List active API keys |
| `DELETE` | `/v1/api-keys/{id}` | Revoke an API key |

---

## Related documents

- [UX/UI Brief](ux-brief.md) — product features, selling points, and user experience vision
- [Backend Overview](backend/overview.md) — technical API architecture
- [Data Model](data_model.md) — authoritative entity schemas
- [Backend MVP](milestones/mvp/backend.md) — current backend milestone
