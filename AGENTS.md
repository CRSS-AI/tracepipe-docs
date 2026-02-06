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
- `docs/milestones/` — Milestone documents (arbitrarily nested, synced with GitHub milestones)
- `scripts/` — Automation for GitHub synchronization
- `.github/workflows/` — GitHub Actions for milestone and submodule sync
- `.github/workflow-templates/` — Templates to install in subrepos

## Project Specification

**Purpose**: Document the Tracepipe platform for browser trace capture, processing, and canonical action classification.

**Repository Architecture**:

| Repository | Purpose |
|------------|---------|
| [tracepipe](https://github.com/CRSS-AI/tracepipe) | **Top-level index** — submodules all repos, centralized milestones & project board |
| [tracepipe-docs](https://github.com/CRSS-AI/tracepipe-docs) | Platform documentation |
| [tracepipe-frontend](https://github.com/CRSS-AI/tracepipe-frontend) | Storefront, payments (Stripe/Link), API key management |
| [tracepipe-backend](https://github.com/CRSS-AI/tracepipe-backend) | Session ingestion API, Capability Surface management |
| [tracepipe-pipelines](https://github.com/CRSS-AI/tracepipe-pipelines) | Session-to-Example processing pipelines |

**Submodule Structure**:

- `tracepipe` contains submodules: `tracepipe-docs`, `tracepipe-backend`, `tracepipe-frontend`, `tracepipe-pipelines`
- Each subrepo contains a `tracepipe-docs` submodule with a symlink: `docs → tracepipe-docs/docs/{subsystem}`

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
└── milestones/                 # Arbitrarily nested milestone docs
    └── poc/
        ├── frontend.md
        ├── backend.md
        └── pipelines.md
```

## GitHub Integration

### Milestone Synchronization

Milestone documents in `docs/milestones/` are synced to GitHub Milestones in `CRSS-AI/tracepipe` via GitHub Actions. The markdown is authoritative — changes made directly in GitHub UI will be overwritten on the next sync.

**Front matter format**:
```yaml
---
title: "Milestone Title"          # Required: becomes GitHub Milestone title
github_milestone: null            # null for new milestones; auto-populated after sync
target_repos:                     # Optional: repos this milestone affects
  - CRSS-AI/tracepipe-backend
---
```

Everything after the front matter closing `---` becomes the GitHub Milestone description verbatim.

**Lifecycle**:
1. Create a new `.md` file anywhere under `docs/milestones/` with `github_milestone: null`
2. Push to `main` — the sync workflow creates the GitHub Milestone and commits the assigned number back
3. Edit the markdown to update the milestone — changes sync on push
4. Delete the markdown file — the GitHub Milestone is closed/archived

### Submodule Synchronization

All submodules are kept up-to-date automatically via GitHub Actions:

- When a subrepo pushes to `main`, it dispatches to `tracepipe` to update its submodule
- When `tracepipe-docs` pushes to `main`, it dispatches to all subrepos to update their docs submodule
- Syncs are idempotent — no commit if already up-to-date

### CLI Commands

**List milestones**:
```bash
gh api repos/CRSS-AI/tracepipe/milestones --jq '.[] | {number, title, state}'
```

**List issues for milestone**:
```bash
gh issue list --repo CRSS-AI/tracepipe --milestone "Milestone Title"
```

**Create issue in milestone**:
```bash
gh issue create --repo CRSS-AI/tracepipe \
  --title "Issue title" \
  --body "Issue body" \
  --milestone "Milestone Title"
```

### Scripts

**Sync milestones** (called by GitHub Actions, can run locally):
```bash
python scripts/sync-milestones.py
```

**Generate markdown summary of milestone issues**:
```bash
./scripts/list-milestone-issues.sh > milestone-issues.md
```

## Quality Assurance

### Before Commit

1. **Validate links**: Ensure all cross-references resolve
2. **Check front matter**: Milestone docs must have `title` field; `github_milestone` can be null for new milestones
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
title: "Milestone Title"
github_milestone: null
target_repos:
  - CRSS-AI/tracepipe-backend
---

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

All milestones live in `CRSS-AI/tracepipe` which has visibility into all subrepos via submodules. Issues can reference across repos using GitHub's cross-repo format: `CRSS-AI/tracepipe-backend#123`.

The centralized project board in `tracepipe` aggregates issues from all repos.

## Tool Usage Protocols

### Subagents

Delegate research-intensive tasks (reading multiple files, gathering context) to subagents to maintain focus.

### Terminal Commands

Always use absolute paths when running commands. Prefer `gh` CLI for GitHub operations.

### File Operations

Read large sections at once rather than many small reads. Use semantic search for discovery, grep for exact matches.

## PAT Setup

The automation requires a Personal Access Token with the following scopes:

- **Contents**: Read and write (for committing milestone numbers back)
- **Issues**: Read and write (for creating/updating milestones)
- **Metadata**: Read

Create the PAT at https://github.com/settings/tokens?type=beta with repository access to all Tracepipe repos, then set the secret:

```bash
for repo in tracepipe tracepipe-docs tracepipe-backend tracepipe-frontend tracepipe-pipelines; do
  gh secret set PAT_TOKEN --repo CRSS-AI/$repo --body "<your-pat>"
done
```
