#!/bin/bash
# script takes a URL, sends a GET request to URL, displays body of response
curl -sI -H "X-HolbertonSchool-User-Id: 98" "$1"
