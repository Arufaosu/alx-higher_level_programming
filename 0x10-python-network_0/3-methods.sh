#!/bin/bash
# displays all HTTP methods
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || methods=$(curl -sI -X OPTIONS "$1" | awk '/Allow:/ {print substr($0, index($0,$2))}'); echo "$methods"
