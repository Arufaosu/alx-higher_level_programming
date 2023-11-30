#!/bin/bash
# sends a request to a URL
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || curl -s -o /dev/null -w "%{http_code}" "$1"
