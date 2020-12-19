#!/bin/bash
# script takes a URL, sends a GET request to URL, displays body of response
curl -s -o /dev/null -w "%{http_code}" "$1" 
