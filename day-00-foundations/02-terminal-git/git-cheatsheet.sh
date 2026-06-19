#!/usr/bin/env bash
set -e
DEMO=$(mktemp -d); cd "$DEMO"
echo "Working in: $DEMO"
git init -q
echo "# Hello" > README.md
git add README.md
git -c user.email=you@example.com -c user.name=You commit -q -m "first commit"
echo "- a note" >> README.md
git add README.md
git -c user.email=you@example.com -c user.name=You commit -q -m "add a note"
echo "--- history ---"; git log --oneline
echo "Demo repo at: $DEMO (safe to delete)"
