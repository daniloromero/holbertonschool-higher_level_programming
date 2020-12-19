#!/bin/bash
# script sends DELETE request 2 URL passed as argument,displays body response
curl -s -H "Content-Type: application/json" "$1" -X POST -T "$2"
