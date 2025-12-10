#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
HEADER_SOURCE="$SCRIPT_DIR/../LICENSE"
PROJECT_ROOT="$SCRIPT_DIR/.."
TEMP_HEADER="/tmp/agpl_python_header.tmp"

{
    read -r first_line <"$HEADER_SOURCE"
    echo "# SurfQ $first_line"

    tail -n +2 "$HEADER_SOURCE" | while IFS= read -r line || [[ -n "$line" ]]; do
        echo "# $line"
    done
} >"$TEMP_HEADER"

find "$PROJECT_ROOT" \
    -path '*/.git' -prune -o \
    -path '*/__pycache__' -prune -o \
    -path '*/.venv' -prune -o \
    -path '*/build' -prune -o \
    -name "*.py" -print | while read -r file; do

    if [[ "$file" == "$PROJECT_ROOT/src/"* ]] ||
        [[ "$file" == "$PROJECT_ROOT/tests/"* ]] ||
        [[ "$file" == "$PROJECT_ROOT/scripts/"* ]]; then

        FIRST_LINE_CHECK="# SurfQ $(head -n 1 "$HEADER_SOURCE")"

        if ! grep -Fxq "$FIRST_LINE_CHECK" "$file"; then

            cat "$TEMP_HEADER" "$file" >"$file.tmp" && mv "$file.tmp" "$file"
            echo "Added header to: $file"

        else
            echo "Header already present in: $file (Skipped)"
        fi
    fi
done

rm "$TEMP_HEADER"
