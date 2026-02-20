# UX/UI Brief

_Last reviewed: 2026-02-20_

This document provides the context a UX/UI designer needs to understand Tracepipe's product, users, features, and intended experience. It is the starting point for all design work.

## What is Tracepipe?

Tracepipe turns recordings of people using web applications into training data for AI models.

A user records themselves performing tasks in a web browser (clicking, typing, navigating). They upload that recording to Tracepipe. Tracepipe's processing pipeline analyzes the recording, figures out what the user was doing (e.g., "compose an email", "add item to cart"), and produces structured training data that ML engineers can feed directly into their model training workflows.

**In one sentence**: Upload a browser recording, get back AI training data.

## Who are our users?

### Primary: ML engineers and AI product teams

People building AI agents that interact with web applications. They need large volumes of high-quality training data showing how humans perform tasks in browsers. They are technical, comfortable with APIs, and prefer programmatic access over clicking through UIs.

### Secondary: Training data builders

Teams or contractors who record browser interactions and upload them. Less technical than ML engineers, but comfortable following step-by-step instructions.

### Key insight for design

Our primary users are **API-first**. They will interact with Tracepipe mainly through the API, not through a web dashboard. The web UI exists primarily for account setup (registration, payment, API keys) and secondarily for monitoring and convenience features (usage dashboard, session browsing). Design the web UI as a **support tool** for the API workflow, not as the primary product surface.

## Features

### Account management

- **Registration and login** — via Azure Entra External ID (Microsoft's identity service)
- **Profile management** — view and update account information

### Payments

- **Add payment method** — user provides a credit card via Stripe; card is stored on file but not immediately charged
- **Usage-based billing** — users are charged at the end of each month based on actual usage:
  - **Tokens consumed** — the amount of AI processing used
  - **Storage × time** — how much data is stored and for how long (measured in GB×hours)
- **No subscriptions, no tiers** — everyone pays the same rates; you only pay for what you use
- **Invoice history** — view past monthly invoices
- **Payment method management** — update or change card on file

### API keys

- **Generate API key** — creates a key (`tp_live_...`) shown once, then never again
- **List keys** — view active keys (masked, showing only prefix/suffix)
- **Revoke key** — immediately disable a key

### Trace upload (Sessions)

- **Upload via API** — submit a browser input event recording file:
  - `input_events.jsonl` — keyboard, mouse, and touch events
- **Upload via web UI** — file upload form with suite selector and progress indicator
- **Session metadata** — each upload is scoped to a "Suite" (the application being recorded, e.g., Gmail) and can include an optional description

### Processing

Processing is fully automated and invisible to the user. After upload:

1. **Validation** — checks that uploaded files are well-formed
2. **Normalization** — cleans and standardizes raw trace data
3. **Action classification** — AI identifies what the user was doing (e.g., "clicked compose", "typed email address")
4. **Example synthesis** — converts classified actions into structured training messages

Users can check processing status but cannot intervene.

### Training data retrieval (Examples)

- **List examples** — filter by session, model, or suite
- **View example metadata** — processing status, model used, creation date
- **Download training data** — retrieve JSONL-formatted training messages ready for model consumption

### Usage monitoring

- **Current billing period** — tokens consumed, storage used, estimated cost
- **Historical usage** — usage trends over time
- **Cost breakdown** — tokens vs. storage costs

## Selling points

These are the messages that should inform marketing copy and landing page design:

1. **No manual labeling** — Tracepipe uses AI to automatically classify what the user was doing in the recording. No human annotators needed.

2. **Input event analysis** — interprets keyboard, mouse, and touch events to understand user intent. No manual labeling needed.

3. **Canonical action mapping** — traces are mapped to a structured vocabulary of actions defined in your Suite, not raw browser events. The output is clean, consistent, and meaningful.

4. **Production-ready output** — training data comes out in JSONL format compatible with standard model training pipelines. No post-processing needed.

5. **Pay only for what you use** — no subscriptions, no tiers, no commitments. Pure usage-based pricing (tokens + storage).

6. **API-first** — everything available through the API. Integrate into your existing workflows programmatically.

## User experience vision

### P0 — API-first flow (primary)

This is the critical path. Every step must work before any UI-only features are built.

```
Register → Add payment method → Get API key → Read Quickstart → Use API Reference → Upload traces → Retrieve training data → Check usage/costs
```

**Step-by-step**:

1. **Register** — user creates an account (Azure Entra External ID)
2. **Add payment method** — user adds a credit card via Stripe (no charge yet)
3. **Generate API key** — user creates an API key and copies it (shown once)
4. **Read Quickstart** — user follows a short guide to make their first API call
5. **Explore API Reference** — user browses the full endpoint documentation to understand capabilities
6. **Upload traces** — user uploads browser recordings via `POST /v1/sessions`
7. **Retrieve training data** — user downloads processed examples via `GET /v1/examples/{id}/messages`
8. **Check usage and costs** — user queries `GET /v1/usage` to see current consumption and estimated costs

**Design implications**: The web UI for steps 1–3 must be fast, minimal, and frictionless. The documentation (steps 4–5) must be excellent — it is part of the product experience. Steps 6–8 happen entirely in the API.

### P1 — Web UI flow (secondary)

These features provide convenience and monitoring for users who want a visual interface.

- **Dashboard** — summary cards (tokens used, storage, sessions uploaded, examples generated), recent sessions list, quick action buttons
- **Session upload page** — file upload form, suite selector, progress bar
- **Usage dashboard** — charts for token usage over time, storage growth, cost breakdown
- **Session browsing** — paginated list of uploaded sessions with metadata
- **Example browsing** — paginated list of generated examples with status indicators

**Design implications**: These pages consume the same API the external users call. Design them as read-heavy monitoring views, not as the primary workflow tool.

### P2 — Future features (deferred)

- Organization/team management
- Role-based access control
- Admin dashboards
- MCP server interface for AI agents

## Priority framework

| Priority | Meaning | Examples |
|----------|---------|----------|
| **P0** | Required for the API-first flow to work end-to-end | Auth, payment, API keys, session upload API, example retrieval API, usage API, OpenAPI spec |
| **P1** | Important but not blocking the primary flow | Dashboard, web upload, usage charts, landing page, session browsing |
| **P2** | Nice to have; deferred | Integration tests, CI/CD, SDK generation, MCP server, admin features |

This framework is reflected in the [GitHub Projects priority field](https://github.com/orgs/CRSS-AI/projects/40) for all Tracepipe issues.

## Glossary

These terms appear throughout the platform. Designers should understand them at a conceptual level.

| Term | Plain-language meaning |
|------|----------------------|
| **Suite** | An application the user records themselves using (e.g., "Gmail", "Shopify Admin"). Think of it as a project or workspace. |
| **Action** | A named thing a user can do within a Suite (e.g., "compose email", "add product"). Part of the Suite's vocabulary. |
| **Tool** | The machine-readable equivalent of an Action — how an AI agent would perform the same task. Actions map to Tools. |
| **MCP Server** | A server that exposes Tools to AI agents. Think of it as "the AI's interface" to an application. |
| **Session** | A single recording upload. Contains the raw browser input event trace file. Scoped to one Suite. |
| **Example** | A piece of processed training data derived from a Session. Contains structured messages in JSONL format. |
| **JSONL** | A file format where each line is a JSON object. The standard format for model training data. |
| **Token** | A unit of AI processing. Roughly corresponds to a word or piece of a word. Used as the billing unit for processing costs. |

## Related documents

- [API Reference](api-reference.md) — static endpoint documentation for building against
- [Frontend Overview](frontend/overview.md) — technical frontend architecture
- [Backend Overview](backend/overview.md) — API services architecture
- [Data Model](data_model.md) — entity schemas and relationships
- [Frontend MVP](milestones/mvp/frontend.md) — current frontend milestone
- [Backend MVP](milestones/mvp/backend.md) — current backend milestone
