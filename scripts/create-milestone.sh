#!/bin/bash
# create-milestone.sh
# Creates a GitHub milestone from a milestone document.
# Usage: ./create-milestone.sh docs/milestones/my-milestone.md

set -euo pipefail

REPO="CRSS-AI/tracepipe-docs"

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 <milestone-doc.md>"
    exit 1
fi

doc="$1"

if [[ ! -f "$doc" ]]; then
    echo "Error: File not found: $doc"
    exit 1
fi

# Extract title from document (first # heading)
title=$(grep -E '^# ' "$doc" | head -1 | sed 's/^# //')

if [[ -z "$title" ]]; then
    echo "Error: No title found in document"
    exit 1
fi

# Extract description (first paragraph after ## Goal, or first paragraph)
description=$(awk '/^## Goal/{found=1; next} found && /^[^#]/ && !/^$/{print; exit}' "$doc")

if [[ -z "$description" ]]; then
    description="See documentation for details."
fi

echo "Creating milestone: $title"
echo "Description: $description"
echo ""

result=$(gh api "repos/$REPO/milestones" \
    --method POST \
    -f title="$title" \
    -f description="$description" \
    -f state="open" \
    --jq '.number')

echo "✓ Created milestone #$result"
echo ""
echo "Update the document front matter:"
echo "---"
echo "github_milestone: $result"
echo "github_repo: $REPO"
echo "---"
