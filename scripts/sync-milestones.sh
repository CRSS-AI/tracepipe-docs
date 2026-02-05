#!/bin/bash
# sync-milestones.sh
# Validates that milestone documents have corresponding GitHub milestones
# and reports any discrepancies.

set -euo pipefail

REPO="CRSS-AI/tracepipe-docs"
MILESTONES_DIR="docs/milestones"

echo "Fetching GitHub milestones for $REPO..."
gh_milestones=$(gh api "repos/$REPO/milestones" --jq '.[] | "\(.number):\(.title)"')

echo "Checking milestone documents in $MILESTONES_DIR..."
echo ""

errors=0

for doc in "$MILESTONES_DIR"/*.md; do
    if [[ ! -f "$doc" ]]; then
        continue
    fi
    
    filename=$(basename "$doc")
    
    # Extract github_milestone from front matter
    milestone_num=$(grep -E '^github_milestone:' "$doc" | head -1 | sed 's/github_milestone: *//' || echo "")
    
    if [[ -z "$milestone_num" ]]; then
        echo "❌ $filename: Missing github_milestone in front matter"
        errors=$((errors + 1))
        continue
    fi
    
    # Extract title from document (first # heading)
    doc_title=$(grep -E '^# ' "$doc" | head -1 | sed 's/^# //')
    
    # Check if milestone exists in GitHub
    gh_title=$(echo "$gh_milestones" | grep "^$milestone_num:" | cut -d: -f2- || echo "")
    
    if [[ -z "$gh_title" ]]; then
        echo "❌ $filename: GitHub milestone #$milestone_num not found"
        errors=$((errors + 1))
    elif [[ "$gh_title" != "$doc_title" ]]; then
        echo "⚠️  $filename: Title mismatch"
        echo "   Document: '$doc_title'"
        echo "   GitHub:   '$gh_title'"
    else
        echo "✓ $filename: Synced with GitHub milestone #$milestone_num"
    fi
done

echo ""
if [[ $errors -gt 0 ]]; then
    echo "Found $errors error(s)"
    exit 1
else
    echo "All milestone documents are synchronized"
fi
