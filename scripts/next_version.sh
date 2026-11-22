#!/usr/bin/env bash
set -euo pipefail

last=$(git describe --tags --abbrev=0 --match 'v*' 2>/dev/null || echo v0.0.0)
if [ "$last" = v0.0.0 ]; then range=HEAD; else range="$last..HEAD"; fi
log=$(git log "$range" --format='%s%n%b')

IFS=. read -r major minor patch <<< "${last#v}"

if echo "$log" | grep -qE '^[a-z]+(\(.+\))?!:|BREAKING CHANGE'; then
  major=$((major+1)); minor=0; patch=0
elif echo "$log" | grep -qE '^feat(\(.+\))?:'; then
  minor=$((minor+1)); patch=0
elif echo "$log" | grep -qE '^fix(\(.+\))?:'; then
  patch=$((patch+1))
else
  echo "No feat/fix commit since $last: no release."
  exit 0
fi

echo "next=v$major.$minor.$patch" >> "$GITHUB_OUTPUT"