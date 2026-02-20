# Frontend Overview

_Last reviewed: 2026-02-19_

## Purpose

The Tracepipe frontend is a B2B SaaS storefront enabling users to register accounts, configure payment methods, and obtain API keys for accessing Tracepipe services.

## Architecture

```mermaid
graph TD
    User[User] --> Storefront[Storefront Web App]
    Storefront --> Auth[Authentication]
    Storefront --> Billing[Billing]
    Storefront --> Keys[API Key Management]
    
    Auth --> AuthProvider[Auth Provider]
    Billing --> Stripe[Stripe/Link]
    Keys --> Backend[Backend API]
```

## Key Capabilities

### User Accounts

- Registration and login via standard auth provider
- Profile management
- Organization/team support (future)

### Payments

- Stripe integration for usage-based monthly billing
- Users add a payment method via Stripe SetupIntent (card on file)
- Usage tracked throughout the month (tokens consumed, storage×time)
- Stripe generates invoice at month-end based on reported usage
- No subscriptions, no tiers, no recurring fixed charges
- Invoice history and payment method management

### API Key Management

- Generate and revoke API keys
- Key scoping by Suite
- Usage monitoring dashboard
- Rate limit visibility

## Design Principles

- **Minimal moving parts**: Standard SaaS patterns, no custom infrastructure
- **Stripe-first**: Leverage Stripe SetupIntent for payment method capture and metered billing for month-end invoicing
- **API-driven**: Frontend consumes Backend API for all operations

## Related Documents

- [Backend Overview](../backend/overview.md) — API that powers the storefront
- [Data Model](../data_model.md) — User entity schema
- [Frontend MVP](../milestones/mvp/frontend.md) — Current milestone
