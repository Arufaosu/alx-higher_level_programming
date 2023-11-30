#!/bin/bash
# displays all HTTP methods

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

methods=$(curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print $2}')
echo "$methods"
