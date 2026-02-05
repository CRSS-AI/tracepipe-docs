# Tracepipe Documentation

Platform documentation for Tracepipe — browser trace capture, processing, and canonical action classification.

## Lineage

Tracepipe is derived from the [AutoActivity](https://github.com/CRSS-AI/autoactivity-docs) platform.

## Documentation

See [docs/index.md](docs/index.md) for the documentation entry point.

## Repositories

| Repository | Purpose |
|------------|---------|
| [tracepipe-docs](https://github.com/CRSS-AI/tracepipe-docs) | Documentation and milestones |
| [tracepipe-frontend](https://github.com/CRSS-AI/tracepipe-frontend) | Storefront web application |
| [tracepipe-backend](https://github.com/CRSS-AI/tracepipe-backend) | API services |
| [tracepipe-pipelines](https://github.com/CRSS-AI/tracepipe-pipelines) | Data processing pipelines |

## Scripts

Utility scripts for GitHub synchronization:

```bash
# Validate milestone documents against GitHub
./scripts/sync-milestones.sh

# Generate markdown summary of milestone issues
./scripts/list-milestone-issues.sh

# Create a GitHub milestone from a document
./scripts/create-milestone.sh docs/milestones/my-milestone.md
```

## Contributing

See [AGENTS.md](AGENTS.md) for contribution guidelines and GitHub integration protocols.
