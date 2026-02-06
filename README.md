# Tracepipe Documentation

Platform documentation for Tracepipe — browser trace capture, processing, and canonical action classification.

## Lineage

Tracepipe is derived from the [AutoActivity](https://github.com/CRSS-AI/autoactivity-docs) platform.

## Documentation

See [docs/index.md](docs/index.md) for the documentation entry point.

## Repository Architecture

| Repository | Purpose |
|------------|---------|
| [tracepipe](https://github.com/CRSS-AI/tracepipe) | **Top-level index** — submodules all repos, centralized milestones & project board |
| [tracepipe-docs](https://github.com/CRSS-AI/tracepipe-docs) | Platform documentation |
| [tracepipe-frontend](https://github.com/CRSS-AI/tracepipe-frontend) | Storefront web application |
| [tracepipe-backend](https://github.com/CRSS-AI/tracepipe-backend) | API services |
| [tracepipe-pipelines](https://github.com/CRSS-AI/tracepipe-pipelines) | Data processing pipelines |

## Submodule Structure

- `tracepipe` contains submodules for all repos at top level
- Each subrepo contains a `tracepipe-docs` submodule with a symlink to its docs folder

## Milestone Management

Milestones are defined as markdown files in `docs/milestones/` (arbitrarily nested). They sync automatically to GitHub Milestones in `CRSS-AI/tracepipe` on push to main.

**Front matter format**:
```yaml
---
title: "Milestone Title"
github_milestone: null    # auto-populated after first sync
target_repos:
  - CRSS-AI/tracepipe-backend
---
```

## Scripts

```bash
# Sync milestones to GitHub (also runs via GitHub Actions)
python scripts/sync-milestones.py

# Generate markdown summary of milestone issues
./scripts/list-milestone-issues.sh > milestone-issues.md
```

## Contributing

See [AGENTS.md](AGENTS.md) for contribution guidelines and GitHub integration protocols.

## Cloning with Submodules

To clone this repository with its first-level submodules:

```bash
git clone --recurse-submodules https://github.com/CRSS-AI/tracepipe-docs.git
```

If you've already cloned without submodules, initialize them:

```bash
git submodule update --init
```

To pull updates including submodule changes:

```bash
git pull --recurse-submodules
```

Or configure git to always recurse submodules on pull:

```bash
git config submodule.recurse true
```
