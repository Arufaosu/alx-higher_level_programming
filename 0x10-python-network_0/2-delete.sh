#!/bin/bash
# sends a DELETE request
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || curl -sX DELETE "$1"
