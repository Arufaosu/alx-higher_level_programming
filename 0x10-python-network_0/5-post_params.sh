#!/bin/bash
# sends a POST request

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
