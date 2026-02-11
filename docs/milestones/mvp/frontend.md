---
title: "Frontend MVP"
github_milestone: 3
target_repos:
  - CRSS-AI/tracepipe-frontend
---

_Last reviewed: 2026-02-11_

## Goal

Deliver a functional storefront where users can register accounts, set up payment methods via Stripe/Link, and obtain API keys for accessing Tracepipe services.

## Scope

- User registration and authentication
- Stripe integration with working payments
- API key generation and management UI
- Basic usage dashboard

## Deliverables

- [ ] Landing page with product overview
- [ ] User registration and login flow
- [ ] Stripe Checkout integration for subscriptions
- [ ] Stripe Customer Portal for billing management
- [ ] API key generation page
- [ ] API key list with revocation capability
- [ ] Basic usage metrics display
- [ ] **Trace capture how-to page** — guide users through recording traces via `chrome://traces`

## Success Criteria

1. New user can register, subscribe, and generate an API key in under 5 minutes
2. Payment processing works end-to-end with Stripe test mode
3. API keys authenticate successfully against Backend API
4. User can view and revoke their API keys
5. Trace capture how-to page clearly explains `chrome://traces` usage and event category selections

## Dependencies

- Backend MVP: User and API key endpoints must be available
- Stripe account configuration
- Azure AD B2C (Microsoft Entra External ID) tenant configuration

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| Stripe integration complexity | Use Stripe Checkout (hosted) to minimize custom code |
| Auth provider configuration | Use Azure AD B2C (Microsoft Entra External ID) with existing Azure infrastructure |
| Scope creep to admin features | Defer organization/team management to future milestone |

## Implementation Notes

### Technology Choices

- Prefer static-first architecture (Next.js, Astro, or similar)
- Use Stripe's hosted checkout and customer portal
- Use Azure AD B2C (Microsoft Entra External ID) for authentication
- Minimal backend requirements—most state lives in Stripe and Backend API

### API Key Flow

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant Stripe
    
    User->>Frontend: Register
    Frontend->>Backend: Create user
    User->>Frontend: Subscribe
    Frontend->>Stripe: Checkout session
    Stripe->>Frontend: Success redirect
    Frontend->>Backend: Verify subscription
    User->>Frontend: Generate API key
    Frontend->>Backend: POST /api-keys
    Backend->>Frontend: Return key (shown once)
```

## Related Documents

- [Frontend Overview](../../frontend/overview.md)
- [Backend MVP](backend.md)
- [Data Model](../../data_model.md) — User entity
