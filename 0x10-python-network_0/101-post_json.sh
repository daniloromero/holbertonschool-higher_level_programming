#!/bin/bash
# script sends DELETE request 2 URL passed as argument,displays body response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
