#!/bin/bash
# displays all HTTP methods

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -sI -X OPTIONS "$1")
methods=$(echo "$response" | awk '/Allow:/ {print substr($0, index($0,$2))}')
echo "$methods"
