#!/bin/bash
# sends a GET request
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; } || curl -s -H "X-School-User-Id: 98" "$1"
