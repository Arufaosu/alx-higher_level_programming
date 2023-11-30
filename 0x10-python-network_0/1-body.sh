#!/bin/bash
# takes in a URL, sends a GET request

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read -r status_code
    if [ "$status_code" -eq 200 ]; then
        curl -s "$1"
    fi
}
