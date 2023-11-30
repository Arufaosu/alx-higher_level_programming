#!/bin/bash
# sends a JSON POST request
[ -z "$1" ] || [ -z "$2" ] && { echo "Usage: $0 <URL> <filename>"; exit 1; } || json_data=$(cat "$2"); response=$(curl -s -X POST -H "Content-Type: application/json" -d "$json_data" "$1"); echo "$response"
