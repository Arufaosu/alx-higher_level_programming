#!/bin/bash
# takes in a URL, sends a request to that UR
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || size=$(curl -s -H "Accept-Encoding: gzip, deflate" "$1" | wc -c); echo "$size"
