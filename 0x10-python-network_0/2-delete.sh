#!/bin/bash
# sends a DELETE request

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sX DELETE "$1"
