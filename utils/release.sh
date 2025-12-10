#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."
DIST_ROOT="${PROJECT_ROOT}/dist"

for cmd in uv git; do
    command -v $cmd >/dev/null || {
        echo "$cmd is required"
        exit 1
    }
done

[ -d "$PROJECT_ROOT" ] || {
    echo "Project root not found: $PROJECT_ROOT"
    exit 1
}
mkdir -p "$DIST_ROOT"

ver=$(uv version | awk '{print $2}')
[ -n "$ver" ] || {
    echo "Failed to read version"
    exit 1
}

[ -f "${PROJECT_ROOT}/.env" ] || {
    echo ".env file not found"
    exit 1
}
set -a
source "${PROJECT_ROOT}/.env"
set +a

rm -rf "$DIST_ROOT"

uv build || {
    echo "Build failed"
    exit 1
}
uv publish || {
    echo "Publish failed"
    exit 1
}

git tag -a "v$ver" -m "release v$ver" || {
    echo "Tag failed"
    exit 1
}
git push origin "v$ver" || {
    echo "Push failed"
    exit 1
}
