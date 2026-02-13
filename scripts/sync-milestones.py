#!/usr/bin/env python3
"""
Sync milestone markdown files to GitHub Milestones.

This script:
1. Recursively finds all *.md files in docs/milestones/
2. Parses YAML front matter for title and github_milestone
3. Creates new GitHub Milestones for docs with github_milestone: null
4. Updates existing GitHub Milestones if title/description changed
5. Closes GitHub Milestones that no longer have a corresponding doc
6. Writes back assigned milestone numbers to the markdown files
"""

import os
import re
import json
import subprocess
import sys
from pathlib import Path

import yaml

MILESTONES_DIR = Path("docs/milestones")

# Regex to match YAML front matter
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def gh_api(repo: str, endpoint: str, method: str = "GET", data: dict | None = None) -> dict | list | None:
    """Call GitHub API via gh CLI."""
    # Substitute {repo} placeholder in endpoint if present
    endpoint = endpoint.replace("{repo}", repo)
    cmd = ["gh", "api", endpoint, "-X", method]
    if data:
        for key, value in data.items():
            if isinstance(value, bool):
                cmd.extend(["-F", f"{key}={str(value).lower()}"])
            elif isinstance(value, (int, float)):
                cmd.extend(["-F", f"{key}={value}"])
            else:
                cmd.extend(["-f", f"{key}={value}"])
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        if "404" in result.stderr:
            return None
        print(f"Error calling GitHub API: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    
    if not result.stdout.strip():
        return None
    return json.loads(result.stdout)


def parse_milestone_file(path: Path) -> dict | None:
    """Parse a milestone markdown file, returning front matter and body."""
    content = path.read_text()
    match = FRONT_MATTER_RE.match(content)
    if not match:
        print(f"Warning: No front matter in {path}, skipping")
        return None
    
    try:
        front_matter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        print(f"Warning: Invalid YAML in {path}: {e}, skipping")
        return None
    
    if "title" not in front_matter:
        print(f"Warning: No title in {path}, skipping")
        return None
    
    if "repo" not in front_matter:
        print(f"Warning: No repo in {path}, skipping")
        return None
    
    body = content[match.end():].strip()
    
    return {
        "path": path,
        "title": front_matter["title"],
        "repo": front_matter["repo"],
        "github_milestone": front_matter.get("github_milestone"),
        "body": body,
        "raw_front_matter": match.group(1),
        "full_content": content,
    }


def update_milestone_number(path: Path, old_content: str, new_number: int) -> None:
    """Update the github_milestone field in a markdown file."""
    # Replace github_milestone: null with github_milestone: <number>
    new_content = re.sub(
        r"(github_milestone:)\s*(?:null|~|\d+)",
        f"\\1 {new_number}",
        old_content,
    )
    path.write_text(new_content)
    print(f"  Updated {path} with milestone number {new_number}")


def get_github_milestones(repo: str) -> dict[int, dict]:
    """Get all GitHub milestones for a repo, keyed by number."""
    milestones = gh_api(repo, f"repos/{repo}/milestones?state=all&per_page=100") or []
    return {m["number"]: m for m in milestones}


def create_milestone(repo: str, title: str, body: str) -> int:
    """Create a new GitHub milestone, return its number."""
    result = gh_api(
        repo,
        f"repos/{repo}/milestones",
        method="POST",
        data={"title": title, "description": body},
    )
    return result["number"]


def update_milestone(repo: str, number: int, title: str, body: str) -> None:
    """Update an existing GitHub milestone."""
    gh_api(
        repo,
        f"repos/{repo}/milestones/{number}",
        method="PATCH",
        data={"title": title, "description": body},
    )


def close_milestone(repo: str, number: int) -> None:
    """Close a GitHub milestone."""
    gh_api(
        repo,
        f"repos/{repo}/milestones/{number}",
        method="PATCH",
        data={"state": "closed"},
    )


def main():
    if not MILESTONES_DIR.exists():
        print(f"Milestones directory {MILESTONES_DIR} does not exist")
        sys.exit(1)

    # Find all milestone files
    milestone_files = list(MILESTONES_DIR.rglob("*.md"))
    print(f"Found {len(milestone_files)} milestone file(s)")

    # Parse all files
    docs = []
    for path in milestone_files:
        doc = parse_milestone_file(path)
        if doc:
            docs.append(doc)

    # Group docs by repo
    repos_to_docs = {}
    for doc in docs:
        repo = doc["repo"]
        if repo not in repos_to_docs:
            repos_to_docs[repo] = []
        repos_to_docs[repo].append(doc)

    # Process each repo
    for repo, repo_docs in repos_to_docs.items():
        print(f"\n=== Processing repo: {repo} ===")
        
        # Get current GitHub milestones for this repo
        gh_milestones = get_github_milestones(repo)
        print(f"Found {len(gh_milestones)} existing GitHub milestone(s)")

        # Track which GitHub milestones are still referenced
        referenced_numbers = set()

        # Process each doc in this repo
        for doc in repo_docs:
            title = doc["title"]
            body = doc["body"]
            number = doc["github_milestone"]

            if number is None:
                # Create new milestone
                print(f"Creating milestone: {title}")
                new_number = create_milestone(repo, title, body)
                update_milestone_number(doc["path"], doc["full_content"], new_number)
                referenced_numbers.add(new_number)
            else:
                referenced_numbers.add(number)
                if number in gh_milestones:
                    gh_m = gh_milestones[number]
                    # Check if update needed
                    if gh_m["title"] != title or (gh_m.get("description") or "") != body:
                        print(f"Updating milestone #{number}: {title}")
                        update_milestone(repo, number, title, body)
                    else:
                        print(f"Milestone #{number} is up to date: {title}")
                else:
                    # Milestone number in doc but doesn't exist in GitHub - recreate
                    print(f"Milestone #{number} not found in GitHub, creating: {title}")
                    new_number = create_milestone(repo, title, body)
                    update_milestone_number(doc["path"], doc["full_content"], new_number)
                    referenced_numbers.add(new_number)
                    referenced_numbers.discard(number)

        # Close orphaned milestones in this repo
        for number, gh_m in gh_milestones.items():
            if number not in referenced_numbers and gh_m["state"] == "open":
                print(f"Closing orphaned milestone #{number}: {gh_m['title']}")
                close_milestone(repo, number)

    print("\n=== Sync complete ===")


if __name__ == "__main__":
    main()
