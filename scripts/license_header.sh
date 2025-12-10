#!/bin/bash

SCRIPT_DIR="$(dirname "$(realpath "${BASH_SOURCE[0]}")")"
HEADER="$SCRIPT_DIR/HEADER_AGPL.txt"
SRC_DIR="$SCRIPT_DIR/../src/surfq"

find "$SRC_DIR" -name "*.py" | while read -r file; do
    if ! grep -Fxq "$(head -n 1 "$HEADER")" "$file"; then
        cat "$HEADER" "$file" >"$file.tmp" && mv "$file.tmp" "$file"
    fi
done
