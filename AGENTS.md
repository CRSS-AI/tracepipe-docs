# Agent Instructions: Tracepipe Documentation

## Lineage

Tracepipe is derived from the AutoActivity platform. The Capability Surface models (Suite, Action, Tool, and their mappings) are preserved. The Activity Execution layer has been simplified: Sessions now represent raw trace uploads from users, and Examples represent processed training data. The Task/Activity/Case/Instance hierarchy from AutoActivity has been removed.

For historical context, see [CRSS-AI/autoactivity-docs](https://github.com/CRSS-AI/autoactivity-docs).

## Operational Philosophy

**Quality Priority**: Prioritize correctness and clarity over speed. Documentation is the source of truth for the Tracepipe platform.

**Deliberation**: Analyze requirements thoroughly before writing. Cross-reference related documents to maintain consistency.

## File Access

All files in this repository are accessible. The primary working areas are:

- `docs/` — Platform documentation
- `docs/milestones/` — Milestone documents synced with GitHub milestones
- `scripts/` — Automation for GitHub synchronization

## Project Specification

**Purpose**: Document the Tracepipe platform for browser trace capture, processing, and canonical action classification.

**Repositories**:

| Repository | Purpose |
|------------|---------|
| [tracepipe-docs](https://github.com/CRSS-AI/tracepipe-docs) | Platform documentation and milestones |
| [tracepipe-frontend](https://github.com/CRSS-AI/tracepipe-frontend) | Storefront, payments (Stripe/Link), API key management |
| [tracepipe-backend](https://github.com/CRSS-AI/tracepipe-backend) | Session ingestion API, Capability Surface management |
| [tracepipe-pipelines](https://github.com/CRSS-AI/tracepipe-pipelines) | Session-to-Example processing pipelines |

## Documentation Structure

```
docs/
├── index.md                    # Landing page with system overview
├── data_model.md               # Authoritative entity schemas
├── frontend/
│   └── overview.md             # Storefront architecture
├── backend/
│   └── overview.md             # API services architecture
├── pipelines/
│   └── overview.md             # Data pipeline architecture
└── milestones/
    ├── frontend-poc.md         # Frontend PoC milestone
    ├── backend-poc.md          # Backend PoC milestone
    └── pipelines-poc.md        # Pipelines PoC milestone
```

## GitHub Integration

### Milestone Synchronization

Milestone documents in `docs/milestones/` correspond 1:1 with GitHub milestones in `tracepipe-docs`. Each milestone document includes YAML front matter linking to its GitHub milestone number.

**Front matter format**:
```yaml
---
github_milestone: 1
github_repo: CRSS-AI/tracepipe-docs
---
```

### CLI Commands

**List milestones**:
```bash
gh milestone list --repo CRSS-AI/tracepipe-docs --state all
```

**Create milestone**:
```bash
gh api repos/CRSS-AI/tracepipe-docs/milestones \
  --method POST \
  -f title="Milestone Title" \
  -f description="Milestone description"
```

**List issues for milestone**:
```bash
gh issue list --repo CRSS-AI/tracepipe-docs --milestone "Milestone Title"
```

**Create issue in milestone**:
```bash
gh issue create --repo CRSS-AI/tracepipe-docs \
  --title "Issue title" \
  --body "Issue body" \
  --milestone "Milestone Title"
```

### Sync Scripts

Use `scripts/sync-milestones.sh` to validate that all milestone documents have corresponding GitHub milestones:

```bash
./scripts/sync-milestones.sh
```

Use `scripts/list-milestone-issues.sh` to generate a markdown summary of issues per milestone:

```bash
./scripts/list-milestone-issues.sh > milestone-issues.md
```

## Quality Assurance

### Before Commit

1. **Validate links**: Ensure all cross-references resolve
2. **Check front matter**: Milestone docs must have valid `github_milestone` numbers
3. **Update "Last reviewed"**: Change the date when meaningfully editing a document

### Documentation Standards

- Use sentence case for headings
- Wrap file paths, commands, and identifiers in backticks
- Use Mermaid for diagrams (versionable)
- Lead with context before implementation details
- Include "Last reviewed" date near top of each document

## Milestone Document Template

```markdown
---
github_milestone: <number>
github_repo: CRSS-AI/tracepipe-docs
---

# <Milestone Title>

_Last reviewed: YYYY-MM-DD_

## Goal

<One-paragraph objective statement>

## Scope

<Bounded list of deliverables>

## Deliverables

- [ ] Deliverable 1
- [ ] Deliverable 2

## Success Criteria

<Measurable acceptance conditions>

## Dependencies

<Prerequisite work or external dependencies>

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| ... | ... |
```

## Cross-Repository Coordination

When a milestone spans multiple repositories (e.g., Backend PoC requires both `tracepipe-backend` and `tracepipe-docs` changes):

1. Create the milestone in `tracepipe-docs` (source of truth)
2. Create issues in the relevant implementation repos referencing the milestone doc
3. Link issues using GitHub's cross-repo reference format: `CRSS-AI/tracepipe-docs#123`

## Tool Usage Protocols

### Subagents

Delegate research-intensive tasks (reading multiple files, gathering context) to subagents to maintain focus.

### Terminal Commands

Always use absolute paths when running commands. Prefer `gh` CLI for GitHub operations.

### File Operations

Read large sections at once rather than many small reads. Use semantic search for discovery, grep for exact matches.
