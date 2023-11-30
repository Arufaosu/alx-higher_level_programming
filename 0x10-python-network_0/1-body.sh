#!/bin/bash
# takes in a URL, sends a GET request

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -w "%{http_code}" "$1")
status_code=$(echo "$response" | tail -c 4)

if [ "$status_code" -eq 200 ]; then
    body=$(echo "$response" | sed '$s/.*\r\n\r\n//')
    echo "$body"
fi
