#!/bin/bash
# takes in a URL, sends a GET request
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || { body=$(curl -s -i "$1" | awk '/^HTTP/ {print $2}'); [ "$body" -eq 200 ] && curl -s "$1"; }
