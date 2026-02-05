#!/bin/bash
# list-milestone-issues.sh
# Generates a markdown summary of issues per milestone.

set -euo pipefail

REPO="CRSS-AI/tracepipe-docs"

echo "# Milestone Issues"
echo ""
echo "_Generated: $(date -u +"%Y-%m-%d %H:%M UTC")_"
echo ""

# Fetch all milestones
milestones=$(gh api "repos/$REPO/milestones" --jq '.[] | "\(.number)|\(.title)|\(.open_issues)|\(.closed_issues)"')

if [[ -z "$milestones" ]]; then
    echo "No milestones found."
    exit 0
fi

while IFS='|' read -r number title open closed; do
    echo "## $title"
    echo ""
    echo "**Progress:** $closed closed, $open open"
    echo ""
    
    # Fetch issues for this milestone
    issues=$(gh issue list --repo "$REPO" --milestone "$title" --state all --json number,title,state --jq '.[] | "- [\(.state)] #\(.number): \(.title)"')
    
    if [[ -z "$issues" ]]; then
        echo "_No issues yet_"
    else
        echo "$issues"
    fi
    echo ""
done <<< "$milestones"
