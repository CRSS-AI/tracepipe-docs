# Tracepipe Documentation

_Last reviewed: 2026-02-11_

Welcome to the canonical documentation for the Tracepipe platform. This repository serves as the source of truth for platform architecture, data models, and milestone planning.

## What is Tracepipe?

Tracepipe transforms raw browser interaction traces into high-quality training data for language models. Built for ML engineers and anyone building training datasets, Tracepipe uses action classification to convert user traces into structured examples suitable for model fine-tuning.

**The Core Value**: Upload a `chrome://traces` recording of a user interacting with a web application, and get back JSONL-formatted training messages that map those interactions to canonical actions in your capability surface.

## How It Works

1. **Capture**: Users record browser traces via `chrome://traces` (input events, network traffic, screenshots)
2. **Upload**: Submit trace bundles through the Tracepipe API (Sessions)
3. **Process**: Pipelines classify actions and extract parameters from multimodal trace evidence
4. **Retrieve**: Download structured training data (Examples) in JSONL format, ready for model training

## Lineage

Tracepipe is derived from the [AutoActivity](https://github.com/CRSS-AI/autoactivity-docs) platform. The Capability Surface models—Suite, Action, Tool, and their mappings—are preserved intact. The execution layer has been simplified: raw trace data arrives as Sessions and is processed into Examples suitable for model training. The Task/Activity/Case/Instance orchestration hierarchy from AutoActivity has been removed.

## System Overview

```mermaid
graph LR
    User[User] -->|uploads traces| API[Backend API]
    API -->|stores| Sessions[(Sessions)]
    Sessions -->|processed by| Pipelines[Data Pipelines]
    Pipelines -->|produces| Examples[(Examples)]
    
    subgraph Frontend
        Storefront[Storefront]
        Storefront -->|payments| Stripe[Stripe/Link]
        Storefront -->|issues| APIKeys[API Keys]
    end
    
    User -->|registers| Storefront
    APIKeys -->|authenticates| API
```

## Subsystems

- [Frontend](frontend/overview.md) — Storefront, user accounts, payments, and API key management.
- [Backend](backend/overview.md) — Session ingestion API and Capability Surface management.
- [Data Pipelines](pipelines/overview.md) — Session-to-Example processing.
- [Data Model](data_model.md) — Authoritative entity schemas and relationships.

## Milestones

Active MVP initiatives:

- [Frontend MVP](milestones/mvp/frontend.md) — Storefront with Stripe payments, API key provisioning, and trace capture how-to.
- [Backend MVP](milestones/mvp/backend.md) — Session ingestion and Capability Surface APIs.
- [Pipelines MVP](milestones/mvp/pipelines.md) — Session-to-Example transformation pipeline.

## Repository Architecture

| Repository | Purpose |
|------------|---------|
| [tracepipe](https://github.com/CRSS-AI/tracepipe) | **Top-level index** — submodules all repos, centralized milestones & project board |
| [tracepipe-docs](https://github.com/CRSS-AI/tracepipe-docs) | Platform documentation |
| [tracepipe-frontend](https://github.com/CRSS-AI/tracepipe-frontend) | Storefront web application |
| [tracepipe-backend](https://github.com/CRSS-AI/tracepipe-backend) | API services |
| [tracepipe-pipelines](https://github.com/CRSS-AI/tracepipe-pipelines) | Data processing pipelines |

## How to Contribute

1. Locate the relevant subsystem and review existing documentation.
2. Update the "Last reviewed" date when meaningfully changing a page.
3. Use Mermaid for diagrams to keep them versionable.
4. Keep commits focused on a single topic.
5. Ensure milestone documents stay synchronized with GitHub milestones.
