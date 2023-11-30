#!/bin/bash
# takes in a URL, sends a request to that UR

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

size=$(curl -s "$1" | wc -w)
echo "$size"
